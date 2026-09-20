#!/usr/bin/env python3
import sys
from pathlib import Path


MINIMUM_PYTHON = (3, 9)
if sys.version_info < MINIMUM_PYTHON:
    raise SystemExit("selftest.py requires Python 3.9 or newer")


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    ROOT / "SKILL.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "references" / "emotion-budget-and-structures.md",
    ROOT / "references" / "emotion-flow-architecture.md",
    ROOT / "references" / "performance-and-camera.md",
    ROOT / "references" / "continuity-and-execution.md",
    ROOT / "references" / "workflow-and-qa.md",
    ROOT / "references" / "localization.md",
)


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        raise SystemExit("missing required skill files: " + ", ".join(missing))

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    required_markers = (
        "name: short-drama-emotion-translate",
        "禁止二次放大",
        "单镜如无必要不超过3秒",
        "emotion-flow-architecture.md",
        "short-drama-storyboard",
        "short-drama-video-prompts",
        "物理母状态",
        "关系权力",
    )
    absent = [marker for marker in required_markers if marker not in skill]
    if absent:
        raise SystemExit("missing integration markers: " + ", ".join(absent))

    print("short-drama-emotion-translate selftest: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
