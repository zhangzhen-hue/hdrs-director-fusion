from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PROJECT_TOKENS = {
    "Vivian",
    "Julian",
    "Ava Monroe",
    "Hawthorne",
    "Vera Durant",
    "Claire",
    "Oliver",
}
MOJIBAKE_MARKERS = {"ф║", "шз", "хИ", "щЫ", "╜", "╛"}
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")


class PackageIntegrityTests(unittest.TestCase):
    def test_exact_skill_set_and_frontmatter(self) -> None:
        expected = {
            "short-drama-emotion-translate",
            "short-drama-storyboard",
            "short-drama-video-prompts",
        }
        actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
        self.assertEqual(actual, expected)
        for name in expected:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"))
            self.assertIn(f"name: {name}", text)
            self.assertIn("description:", text)

    def test_markdown_links_resolve(self) -> None:
        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for target in LINK_PATTERN.findall(text):
                if target.startswith(("http://", "https://")):
                    continue
                self.assertTrue((path.parent / target).is_file(), f"broken link: {path}: {target}")

    def test_no_project_specific_names_or_mojibake(self) -> None:
        checked_paths = list(SKILLS.rglob("*")) + [ROOT / "PACKAGE.md"]
        for path in checked_paths:
            relative = str(path.relative_to(ROOT))
            self.assertFalse(any(marker in relative for marker in MOJIBAKE_MARKERS), relative)
            if path.is_file() and path.suffix in {".md", ".yaml", ".json", ".jsonl", ".py"}:
                text = path.read_text(encoding="utf-8")
                for token in PROJECT_TOKENS:
                    self.assertNotIn(token, text, f"project leakage in {relative}: {token}")

    def test_no_cache_or_compiled_artifacts(self) -> None:
        forbidden = [
            path
            for path in ROOT.rglob("*")
            if path.name == "__pycache__" or path.suffix in {".pyc", ".pyo"}
        ]
        self.assertEqual(forbidden, [])

    def test_single_master_has_no_duplicate_selected_skills_tree(self) -> None:
        self.assertFalse((ROOT / "selected-skills").exists())
        self.assertFalse((ROOT / "drama-skills-v0.6.1").exists())


if __name__ == "__main__":
    unittest.main()
