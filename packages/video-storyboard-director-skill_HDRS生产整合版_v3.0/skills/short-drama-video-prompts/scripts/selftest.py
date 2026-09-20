#!/usr/bin/env python3
"""Offline self-test for standalone video and music prompt tooling."""

from __future__ import annotations

import copy
import sys

from music_spec_check import SKILL_ROOT, ValidationError, load_jsonl, validate_records

MINIMUM_PYTHON = (3, 9)
if sys.version_info < MINIMUM_PYTHON:
    raise SystemExit("selftest.py requires Python 3.9 or newer")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def fail(records: list[dict], marker: str) -> None:
    try:
        validate_records(records)
    except ValidationError as exc:
        require(marker in str(exc), f"expected {marker!r}, got {exc!s}")
    else:
        raise AssertionError(f"expected failure containing {marker!r}")


def main() -> int:
    flow_reference = SKILL_ROOT / "references" / "emotion-flow-execution.md"
    require(flow_reference.is_file(), "emotion-flow execution reference is missing")
    seedance_reference = SKILL_ROOT / "references" / "seedance-chinese-execution-profile.md"
    repair_reference = SKILL_ROOT / "references" / "qa-and-minimal-repair.md"
    require(seedance_reference.is_file(), "Seedance Chinese execution profile is missing")
    require(repair_reference.is_file(), "minimal repair reference is missing")
    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    require("单镜如无必要不超过3秒" in skill_text, "commercial shot-duration rule is missing")
    require("emotion-flow-execution.md" in skill_text, "emotion-flow execution reference is not routed")
    require("seedance-chinese-execution-profile.md" in skill_text, "Seedance profile is not routed")
    require("qa-and-minimal-repair.md" in skill_text, "repair reference is not routed")
    require("连续两个半角连字符" in skill_text, "copyable prompt punctuation rule is missing")

    records = load_jsonl(SKILL_ROOT / "examples/minimal-music-specs.jsonl")
    require(validate_records(records)["music_specs"] == 1, "valid fixture count")
    header, spec = records[0], records[1]
    require(spec["source_refs"][0]["src"] == "screenplay", "fixture uses a source key")

    # A file that was written before sources declarations existed still carries
    # the snapshot on every reference, and still validates.
    expanded = copy.deepcopy(spec)
    expanded["source_refs"] = [
        {**header["sources"]["screenplay"], "record_id": "EP001-SC001"}
    ]
    require(validate_records([expanded])["music_specs"] == 1, "inline snapshot accepted")

    undeclared = copy.deepcopy(spec)
    undeclared["source_refs"] = [{"src": "screenplai", "record_id": "EP001-SC001"}]
    fail([header, undeclared], "REF_SRC_IS_NOT_DECLARED")

    unbound = copy.deepcopy(spec)
    unbound["source_refs"] = [{"record_id": "EP001-SC001"}]
    fail([header, unbound], "REF_HAS_NO_UPSTREAM_BINDING")

    duplicate = [header, spec, copy.deepcopy(spec)]
    fail(duplicate, "duplicate music_id")

    leaked = [header, copy.deepcopy(spec)]
    leaked[1]["model"] = "example"
    fail(leaked, "provider execution fields")

    song_without_lyrics = [header, copy.deepcopy(spec)]
    song_without_lyrics[1]["mode"] = "song"
    fail(song_without_lyrics, "lyrics")

    invalid_scope = [header, copy.deepcopy(spec)]
    invalid_scope[1]["scope"]["end_seconds"] = 0
    fail(invalid_scope, "0 <= start < end")

    unsupported = [header, copy.deepcopy(spec)]
    unsupported[1]["token"] = "not provider-neutral"
    fail(unsupported, "unsupported fields")

    # A source entry now names an upstream artifact and nothing else; a stray
    # byte digest is an unsupported field rather than a malformed hash.
    stale_source = [copy.deepcopy(header), spec]
    stale_source[0]["sources"]["screenplay"]["hash"] = "not-a-sha256"
    fail(stale_source, "unsupported fields")

    print("18 self-tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
