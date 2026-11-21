"""Check tracked documentation structure/hygiene, not runtime or human approvals."""
import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OWN_DOCS = ["Local-Development-and-Delivery.md", "Deployment-and-Recovery.md",
            "Submission-Checklist.md", "Verification-Report.md"]
TEAM_DOCS = ["SRS.md", "NFR-and-Quality-Measures.md", "UI-UX.md", "Architecture.md",
             "Review-and-Test-Plan.md", "Team-and-Process.md", "Traceability.md"]
SPRINT = Path("docs/sprint-2")
DIAGRAM_DIRS = {"diagrams", "architecture", "flows", "user-flows"}
FIGMA_DIRS = {"figma", "screens", "screenshots", "ui", "ui-ux", "prototypes"}
EXPORT_SUFFIXES = {".png", ".svg", ".pdf"}


def markdown_links(path):
    content = re.sub(r"```.*?```|~~~~.*?~~~~", "", (ROOT / path).read_text(), flags=re.S)
    return [(bool(image), link.split(' "', 1)[0].strip("<>"))
            for image, link in re.findall(r"(!?)\[[^\]]*\]\(([^)]+)\)", content)]


def local_target(document, link):
    parts = urlsplit(link)
    if parts.scheme or not parts.path:
        return None
    try:
        return ((ROOT / document).parent / unquote(parts.path)).resolve().relative_to(ROOT)
    except ValueError:
        return None


def check_artifact_sources(files, errors, release_ready=False):
    """Use artifact purpose, not every PNG/PDF suffix, to select source rules."""
    diagrams, screens = set(), set()
    ui_doc = SPRINT / "UI-UX.md"
    ui_links = markdown_links(ui_doc) if ui_doc in files else []
    for path in files:
        if SPRINT not in path.parents or path.suffix.lower() not in EXPORT_SUFFIXES:
            continue
        directories = set(path.relative_to(SPRINT).parts[:-1])
        if directories & FIGMA_DIRS:
            screens.add(path)
        elif directories & DIAGRAM_DIRS:
            diagrams.add(path)
    # Screens may also live beside UI-UX.md; ordinary linked PDF reports are
    # not implicitly diagrams. Explicit diagram directories cover PDF diagrams.
    for image, link in ui_links:
        target = local_target(ui_doc, link)
        if (target in files and target.suffix.lower() in EXPORT_SUFFIXES
                and (image or target.suffix.lower() != ".pdf")):
            screens.add(target)
    for doc_name in ("Architecture.md", "User-Flows.md"):
        doc = SPRINT / doc_name
        if doc in files:
            for image, link in markdown_links(doc):
                target = local_target(doc, link)
                if image and target in files and target.suffix.lower() in EXPORT_SUFFIXES:
                    diagrams.add(target)
    for path in sorted(diagrams - screens):
        if not any(path.with_suffix(ext) in files for ext in (".mmd", ".puml", ".drawio")):
            errors.append("Sprint 2 diagram export needs same-stem editable source: " + str(path))
    if screens or (release_ready and ui_doc in files):
        # Prototype-only URLs are previews, not an editable Figma file source.
        figma_url = False
        local_fig = False
        for _, link in ui_links:
            parts = urlsplit(link)
            segments = parts.path.strip("/").split("/")
            if (parts.scheme == "https" and parts.netloc in {"figma.com", "www.figma.com"}
                    and len(segments) >= 2 and segments[0] in {"design", "file"} and segments[1]):
                figma_url = True
            target = local_target(ui_doc, link)
            if target in files and target.suffix.lower() == ".fig" and (ROOT / target).stat().st_size:
                local_fig = True
        if not (figma_url or local_fig):
            errors.append("Figma outputs need an editable figma.com/design or /file link, or a linked nonempty .fig file, in docs/sprint-2/UI-UX.md")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-ready", action="store_true",
                        help="also fail on missing proposed team document paths; manual release gates still apply")
    args = parser.parse_args()
    paths = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT).decode().split("\0")
    files = {Path(name) for name in paths if name and (ROOT / name).is_file()}
    errors = []
    for name in OWN_DOCS:
        if Path("docs/sprint-2", name) not in files:
            errors.append("Missing DevOps document: " + name)
    for path in sorted(files):
        if (path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example")
                or path.suffix in {".db", ".sqlite", ".sqlite3", ".pyc", ".pem", ".key"}
                or path.name.endswith(("-wal", "-shm", "-journal"))
                or any(part in {"data", "uploads", ".venv", "__pycache__"} for part in path.parts)):
            errors.append("Runtime/private file is tracked: " + str(path))
        if path.suffix == ".md":
            for _, link in markdown_links(path):
                parts = urlsplit(link)
                if parts.scheme:
                    if parts.scheme in {"http", "https"} and not parts.netloc:
                        errors.append(f"Malformed URL in {path}")
                    continue  # External reachability/permissions need a real access review.
                if not parts.path:
                    continue
                target = ((ROOT / path).parent / unquote(parts.path)).resolve()
                try:
                    relative = target.relative_to(ROOT)
                except ValueError:
                    errors.append(f"Link escapes repository in {path}: {link}")
                    continue
                if relative not in files:
                    errors.append(f"Missing/untracked link target in {path}: {link}")
        if path.suffix == ".svg":
            try:
                ET.parse(ROOT / path)
            except ET.ParseError:
                errors.append("Invalid SVG XML: " + str(path))
        if path.suffix in {".puml", ".mmd"}:
            text = (ROOT / path).read_text().strip()
            if not text or (path.suffix == ".puml" and not ("@startuml" in text and "@enduml" in text)):
                errors.append("Empty/malformed diagram source: " + str(path))
    check_artifact_sources(files, errors, args.release_ready)
    missing = [name for name in TEAM_DOCS if Path("docs/sprint-2", name) not in files]
    if missing:
        print("READINESS pending (proposed paths; adapt to agreed filenames): " + ", ".join(missing))
        if args.release_ready:
            errors.append("Team artifact integration is incomplete")
    for error in errors:
        print("FAIL: " + error)
    if errors:
        return 1
    print("PASS: DevOps documents, tracked local links, SVG XML, diagram source pairs, Figma source references and runtime-file hygiene.")
    print("Not checked: prose completeness, anchors, remote link access, diagram rendering, secrets in arbitrary text, Figma source validity/permissions, human review or release readiness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
