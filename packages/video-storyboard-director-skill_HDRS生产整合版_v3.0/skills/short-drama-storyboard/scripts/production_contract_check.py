#!/usr/bin/env python3
"""Validate cross-shot production contracts for short-drama storyboards."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


MINIMUM_PYTHON = (3, 9)
FLOW_ROLES = {"stimulus", "reception", "choice", "counteraction", "aftermath", "connection"}
SOUND_TYPES = {"dialogue", "vo", "os", "sfx", "ambience", "music"}
STATE_SECTIONS = ("characters", "props", "environment")


class ContractError(ValueError):
    """Raised when a production contract violates one or more invariants."""


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ContractError(f"LINE{line_number}: INVALID_JSON: {exc.msg}") from exc
        if not isinstance(value, dict):
            raise ContractError(f"LINE{line_number}: RECORD_IS_NOT_OBJECT")
        records.append(value)
    return records


def _is_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _state_errors(shot_id: str, label: str, state: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(state, dict):
        return [f"{shot_id}: {label.upper()}_IS_NOT_OBJECT"]
    for section in STATE_SECTIONS:
        if not isinstance(state.get(section), dict):
            errors.append(f"{shot_id}: {label.upper()}_{section.upper()}_IS_NOT_OBJECT")
    return errors


def validate_records(records: Iterable[dict[str, Any]]) -> dict[str, int]:
    items = list(records)
    errors: list[str] = []
    if not items:
        raise ContractError("CONTRACT_IS_EMPTY")

    header = items[0]
    if header.get("record_type") != "contract_header":
        errors.append("FIRST_RECORD_MUST_BE_CONTRACT_HEADER")
    if not _is_nonempty_text(header.get("contract_version")):
        errors.append("HEADER_CONTRACT_VERSION_IS_MISSING")
    mother_state = header.get("mother_state")
    if not isinstance(mother_state, dict):
        errors.append("HEADER_MOTHER_STATE_IS_NOT_OBJECT")
        mother_state = {}
    if header.get("relationship_before") == header.get("relationship_after"):
        errors.append("SCENE_RELATIONSHIP_DOES_NOT_CHANGE")

    shots = items[1:]
    if not shots:
        errors.append("CONTRACT_HAS_NO_SHOTS")

    seen_shot_ids: set[str] = set()
    seen_event_ids: set[str] = set()
    previous: dict[str, Any] | None = None

    for index, shot in enumerate(shots, 1):
        shot_id = shot.get("shot_id")
        label = shot_id if _is_nonempty_text(shot_id) else f"SHOT_AT_INDEX_{index}"
        if shot.get("record_type") != "shot":
            errors.append(f"{label}: RECORD_TYPE_MUST_BE_SHOT")
        if not _is_nonempty_text(shot_id):
            errors.append(f"{label}: SHOT_ID_IS_MISSING")
        elif shot_id in seen_shot_ids:
            errors.append(f"{label}: DUPLICATE_SHOT_ID")
        else:
            seen_shot_ids.add(shot_id)

        event_id = shot.get("event_id")
        if not _is_nonempty_text(event_id):
            errors.append(f"{label}: EVENT_ID_IS_MISSING")
        elif event_id in seen_event_ids:
            errors.append(f"{label}: EVENT_ALREADY_EXECUTED")
        else:
            seen_event_ids.add(event_id)

        if shot.get("flow_role") not in FLOW_ROLES:
            errors.append(f"{label}: INVALID_FLOW_ROLE")
        if not _is_nonempty_text(shot.get("shot_function")):
            errors.append(f"{label}: SHOT_FUNCTION_IS_MISSING")
        if not _is_nonempty_text(shot.get("relationship_delta")):
            errors.append(f"{label}: RELATIONSHIP_DELTA_IS_MISSING")
        source_refs = shot.get("source_refs")
        if not isinstance(source_refs, list) or not source_refs or not all(_is_nonempty_text(x) for x in source_refs):
            errors.append(f"{label}: SOURCE_REFS_ARE_MISSING")

        duration = shot.get("duration_seconds")
        if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration <= 0:
            errors.append(f"{label}: INVALID_DURATION")
        elif duration > 3:
            if not _is_nonempty_text(shot.get("long_shot_reason")):
                errors.append(f"{label}: LONG_SHOT_REASON_IS_MISSING")
            attention_events = shot.get("attention_events")
            if not isinstance(attention_events, list) or not attention_events:
                errors.append(f"{label}: LONG_SHOT_ATTENTION_EVENTS_ARE_MISSING")

        main_actions = shot.get("main_actions")
        if not isinstance(main_actions, list) or len(main_actions) != 1 or not _is_nonempty_text(main_actions[0]):
            errors.append(f"{label}: EXACTLY_ONE_MAIN_ACTION_REQUIRED")
        reactions = shot.get("secondary_reactions", [])
        if not isinstance(reactions, list) or len(reactions) > 1 or any(not _is_nonempty_text(x) for x in reactions):
            errors.append(f"{label}: AT_MOST_ONE_SECONDARY_REACTION_ALLOWED")
        camera = shot.get("camera_ideas")
        if not isinstance(camera, list) or len(camera) != 1 or not _is_nonempty_text(camera[0]):
            errors.append(f"{label}: EXACTLY_ONE_CAMERA_IDEA_REQUIRED")

        errors.extend(_state_errors(label, "start_state", shot.get("start_state")))
        errors.extend(_state_errors(label, "end_state", shot.get("end_state")))

        if shot.get("mother_state") != mother_state:
            errors.append(f"{label}: MOTHER_STATE_DRIFT")

        sounds = shot.get("sound")
        if not isinstance(sounds, list):
            errors.append(f"{label}: SOUND_MUST_BE_LIST")
        else:
            for sound_index, sound in enumerate(sounds, 1):
                if not isinstance(sound, dict) or sound.get("type") not in SOUND_TYPES:
                    errors.append(f"{label}: SOUND_{sound_index}_HAS_INVALID_TYPE")
                    continue
                if sound.get("type") in {"dialogue", "vo", "os"} and not _is_nonempty_text(sound.get("text")):
                    errors.append(f"{label}: SOUND_{sound_index}_TEXT_IS_MISSING")
                if sound.get("type") == "dialogue" and not _is_nonempty_text(sound.get("speaker")):
                    errors.append(f"{label}: DIALOGUE_SPEAKER_IS_MISSING")
                if sound.get("type") == "vo" and sound.get("visible_mouths_closed") is not True:
                    errors.append(f"{label}: VO_REQUIRES_VISIBLE_MOUTHS_CLOSED")

        if shot.get("empty_shot") is True:
            start_characters = (shot.get("start_state") or {}).get("characters")
            end_characters = (shot.get("end_state") or {}).get("characters")
            proof = shot.get("empty_shot_proof")
            expected_proof = {"human_presence": False, "human_shadow": False, "human_reflection": False}
            if start_characters or end_characters or proof != expected_proof:
                errors.append(f"{label}: EMPTY_SHOT_CONTAINS_HUMAN_TRACE")

        if previous is not None and previous.get("end_state") != shot.get("start_state"):
            errors.append(f"{label}: START_STATE_DOES_NOT_MATCH_PREVIOUS_END")
        previous = shot

    if errors:
        raise ContractError("\n".join(errors))
    return {"shots": len(shots), "events": len(seen_event_ids)}


def main(argv: list[str] | None = None) -> int:
    if sys.version_info < MINIMUM_PYTHON:
        raise SystemExit("production_contract_check.py requires Python 3.9 or newer")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    args = parser.parse_args(argv)
    try:
        summary = validate_records(load_jsonl(args.contract))
    except (OSError, ContractError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps({"valid": True, **summary}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
