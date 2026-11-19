"""Safety and integrity checks for delivery tooling; these are not auth tests."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "scripts"))
from check_sprint2 import OWN_DOCS, TEAM_DOCS


class DeliveryToolsTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="tutorbridge-delivery-test-")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "scripts").mkdir()
        for name in ("build_delivery.py", "check_sprint2.py"):
            shutil.copyfile(SOURCE / "scripts" / name, self.root / "scripts" / name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Delivery Test")
        self.git("config", "user.email", "delivery@example.test")
        self.git("config", "commit.gpgsign", "false")
        (self.root / "binary.dat").write_bytes(bytes(range(256)))
        self.commit()

    def git(self, *args):
        return subprocess.check_output(["git", "-c", "core.hooksPath=/dev/null", *args],
                                       cwd=self.root, stderr=subprocess.STDOUT, text=True).strip()

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "Synthetic fixture")

    def run_tool(self, tool, *args):
        return subprocess.run([sys.executable, str(self.root / "scripts" / tool), *args],
                              cwd=self.root, capture_output=True, text=True, timeout=20)

    def artifact_paths(self, include_team=True):
        for name in OWN_DOCS + (TEAM_DOCS if include_team else []):
            path = self.root / "docs/sprint-2" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Synthetic artifact\n")

    def tag_main(self):
        self.git("tag", "v0.2.0-sprint2")
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")

    def build(self, *args):
        return self.run_tool("build_delivery.py", *args, "--output-dir", str(self.root / "output"))

    def test_preview_preserves_commit_binary_and_draft_status(self):
        result = self.build("--ref", "HEAD", "--preview")
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(next((self.root / "output").glob("*.zip"))) as archive:
            self.assertEqual(archive.read("TutorBridge/binary.dat"), bytes(range(256)))
            manifest = json.loads(archive.read("TutorBridge/DELIVERY-MANIFEST.json"))
            self.assertEqual(manifest["commit"], self.git("rev-parse", "HEAD"))
            self.assertTrue(manifest["status"].startswith("DRAFT"))
            self.assertTrue(manifest["missing_proposed_team_paths"])

    def test_final_rejects_untagged_commit(self):
        self.assertNotEqual(self.build("--ref", "HEAD").returncode, 0)
        self.assertFalse((self.root / "output").exists())

    def test_final_rejects_missing_team_artifacts(self):
        self.tag_main()
        self.assertNotEqual(self.build("--ref", "v0.2.0-sprint2").returncode, 0)
        self.assertFalse((self.root / "output").exists())

    def test_preview_rejects_tracked_private_configuration(self):
        (self.root / ".env").write_text("# synthetic nonsecret file\n")
        self.commit()
        self.assertNotEqual(self.build("--ref", "HEAD", "--preview").returncode, 0)
        self.assertFalse((self.root / "output").exists())

    def test_tag_matching_main_can_build_structural_package(self):
        self.artifact_paths()
        self.commit()
        self.tag_main()
        result = self.build("--ref", "v0.2.0-sprint2")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_final_rejects_tag_main_mismatch(self):
        self.artifact_paths()
        self.commit()
        self.tag_main()
        self.git("update-ref", "refs/remotes/origin/main", "HEAD~1")
        self.assertNotEqual(self.build("--ref", "v0.2.0-sprint2").returncode, 0)
        self.assertFalse((self.root / "output").exists())

    def test_document_checker_rejects_broken_tracked_link(self):
        self.artifact_paths(include_team=False)
        (self.root / "README.md").write_text("[Missing](docs/missing.md)\n")
        result = self.run_tool("check_sprint2.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing/untracked link target", result.stdout)

    def test_document_checker_does_not_treat_presence_as_release_readiness(self):
        self.artifact_paths(include_team=False)
        result = self.run_tool("check_sprint2.py")
        self.assertEqual(result.returncode, 0, result.stdout)
        release = self.run_tool("check_sprint2.py", "--release-ready")
        self.assertNotEqual(release.returncode, 0)
        self.assertIn("integration is incomplete", release.stdout)


if __name__ == "__main__":
    unittest.main()
