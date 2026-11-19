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
            content = re.sub(r"```.*?```|~~~~.*?~~~~", "", (ROOT / path).read_text(), flags=re.S)
            for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
                link = link.split(' "', 1)[0].strip("<>")
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
        if str(path).startswith("docs/sprint-2/") and path.suffix in {".png", ".svg", ".pdf"}:
            candidates = [path.with_suffix(ext) for ext in (".mmd", ".puml", ".drawio")]
            if not any(candidate in files for candidate in candidates):
                errors.append("Sprint 2 diagram export needs same-stem editable source: " + str(path))
    missing = [name for name in TEAM_DOCS if Path("docs/sprint-2", name) not in files]
    if missing:
        print("READINESS pending (proposed paths; adapt to agreed filenames): " + ", ".join(missing))
        if args.release_ready:
            errors.append("Team artifact integration is incomplete")
    for error in errors:
        print("FAIL: " + error)
    if errors:
        return 1
    print("PASS: DevOps documents, tracked local links, SVG XML, diagram source pairs and runtime-file hygiene.")
    print("Not checked: prose completeness, anchors, remote link access, diagram rendering, secrets in arbitrary text, Figma, human review or release readiness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
