#!/usr/bin/env python3
"""Run the offline validation suite for the v3 short-drama skill package."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = (
    "short-drama-emotion-translate",
    "short-drama-storyboard",
    "short-drama-video-prompts",
)


def run(command: list[str], cwd: Path) -> None:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(command, cwd=cwd, env=environment, check=True)


def main() -> int:
    for skill_name in SKILL_NAMES:
        skill_root = ROOT / "skills" / skill_name
        run([sys.executable, "scripts/selftest.py"], skill_root)
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], ROOT)
    print("v3 package validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
