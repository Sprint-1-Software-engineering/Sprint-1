"""Build an exact-commit local ZIP. Does not tag, merge, approve or upload."""
import argparse
import copy
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

from check_sprint2 import OWN_DOCS, TEAM_DOCS

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True, help="reviewed Sprint 2 tag; a commit is allowed only with --preview")
    parser.add_argument("--preview", action="store_true", help="clearly mark an incomplete branch snapshot DRAFT")
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    if args.ref.startswith("-"):
        parser.error("ref cannot be an option")
    revision = git("rev-parse", "--verify", args.ref + "^{commit}").decode().strip()
    if not args.preview:
        if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+-sprint2", args.ref):
            parser.error("final delivery requires an unused-version Sprint 2 tag such as v0.2.0-sprint2")
        tagged = git("rev-parse", "--verify", "refs/tags/" + args.ref + "^{commit}").decode().strip()
        main_sha = git("rev-parse", "--verify", "refs/remotes/origin/main^{commit}").decode().strip()
        if tagged != revision or tagged != main_sha:
            parser.error("tag must resolve to the fetched final origin/main commit; refresh refs before building")
    archive = zipfile.ZipFile(io.BytesIO(git("archive", "--format=zip", revision)))
    names = {item.filename for item in archive.infolist() if not item.is_dir()}
    for name in names:
        path = Path(name)
        if (path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example")
                or path.suffix in {".db", ".sqlite", ".sqlite3", ".pyc", ".pem", ".key"}
                or path.name.endswith(("-wal", "-shm", "-journal"))
                or any(part in {"data", "uploads", ".venv", "__pycache__"} for part in path.parts)):
            parser.error("ref contains runtime/private file; no package written: " + name)
    missing = ["docs/sprint-2/" + name for name in OWN_DOCS + TEAM_DOCS
               if "docs/sprint-2/" + name not in names]
    if missing and not args.preview:
        parser.error("tag is missing proposed delivery paths; resolve team filenames/readiness first: " + ", ".join(missing))
    label = "DRAFT-" + revision[:12] if args.preview else args.ref
    destination = args.output_dir.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    output = destination / ("TutorBridge-" + label + ".zip")
    checksum = output.with_suffix(".zip.sha256")
    if output.exists() or checksum.exists():
        parser.error("output already exists; choose a fresh output directory")
    manifest = {
        "status": "DRAFT - incomplete, not a final submission" if args.preview else "Tagged source package - manual release gates still require verification",
        "ref": args.ref, "commit": revision, "missing_proposed_team_paths": missing,
        "files": {name: hashlib.sha256(archive.read(name)).hexdigest() for name in sorted(names)},
        "limits": "No proof of human approvals, Figma access, prose quality or Teams upload; no public asset upload performed",
    }
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
        for item in archive.infolist():
            if not item.is_dir():
                packaged = copy.copy(item)
                packaged.filename = "TutorBridge/" + item.filename
                bundle.writestr(packaged, archive.read(item.filename))
        bundle.writestr("TutorBridge/DELIVERY-MANIFEST.json", json.dumps(manifest, indent=2) + "\n")
    checksum.write_text(hashlib.sha256(output.read_bytes()).hexdigest() + "  " + output.name + "\n")
    with zipfile.ZipFile(output) as verification:
        if verification.testzip() is not None:
            raise RuntimeError("ZIP integrity verification failed")
        for name, digest in manifest["files"].items():
            if hashlib.sha256(verification.read("TutorBridge/" + name)).hexdigest() != digest:
                raise RuntimeError("packaged source hash mismatch")
    print(str(output))
    print(str(checksum))
    print("Verified source commit: " + revision)
    print(manifest["status"])


if __name__ == "__main__":
    main()
