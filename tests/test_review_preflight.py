"""Offline CLI safety tests; never invoke a model provider."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "codex_review.py"

class ReviewPreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (ROOT / ".build").mkdir(exist_ok=True)

    def invoke(self, args=(), env=None):
        clean = {k: v for k, v in os.environ.items() if not k.startswith("RELAYPILOT_")}
        return subprocess.run([sys.executable, str(SCRIPT), *args], env={**clean, **(env or {})}, capture_output=True, text=True, encoding="utf-8", timeout=15)

    def test_no_opt_in_never_launches_model(self):
        p = self.invoke()
        self.assertEqual(p.returncode, 2)
        self.assertIn("--execute", p.stderr)

    def test_missing_configuration_fails_without_artifacts(self):
        with tempfile.TemporaryDirectory(dir=ROOT / ".build") as tmp:
            p = self.invoke(["--check"], {"RELAYPILOT_WORK_DIR": tmp})
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("Missing configuration", p.stderr)
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_invalid_commit_fails_before_launch(self):
        with tempfile.TemporaryDirectory(dir=ROOT / ".build") as tmp:
            p = self.invoke(["--check"], {
                "RELAYPILOT_WORK_DIR": tmp, "RELAYPILOT_REPO_DIR": tmp,
                "RELAYPILOT_CODEX_EXE": sys.executable, "RELAYPILOT_MODEL": "example-model",
                "RELAYPILOT_TASK_ID": "DEMO-001", "RELAYPILOT_REVIEW_COMMIT": "not-a-sha",
                "RELAYPILOT_PLAN_SESSION": "example-plan"
            })
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("40-character", p.stderr)
            self.assertEqual(list(Path(tmp).iterdir()), [])

if __name__ == "__main__":
    unittest.main()
