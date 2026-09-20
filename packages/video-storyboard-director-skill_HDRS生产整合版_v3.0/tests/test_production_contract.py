from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "skills" / "short-drama-storyboard" / "scripts" / "production_contract_check.py"
FIXTURE = ROOT / "skills" / "short-drama-storyboard" / "assets" / "shot-contract.example.jsonl"
SPEC = importlib.util.spec_from_file_location("production_contract_check", CHECKER)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProductionContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.records = MODULE.load_jsonl(FIXTURE)

    def assert_contract_error(self, records, marker: str) -> None:
        with self.assertRaises(MODULE.ContractError) as raised:
            MODULE.validate_records(records)
        self.assertIn(marker, str(raised.exception))

    def test_valid_contract(self) -> None:
        self.assertEqual(MODULE.validate_records(self.records), {"shots": 3, "events": 3})

    def test_long_shot_needs_reason_and_attention_events(self) -> None:
        records = copy.deepcopy(self.records)
        records[1]["duration_seconds"] = 4.2
        self.assert_contract_error(records, "LONG_SHOT_REASON_IS_MISSING")
        self.assert_contract_error(records, "LONG_SHOT_ATTENTION_EVENTS_ARE_MISSING")

    def test_one_main_action_and_one_camera_idea(self) -> None:
        records = copy.deepcopy(self.records)
        records[1]["main_actions"].append("人物A同时转身离开")
        records[1]["camera_ideas"].append("同时快速环绕")
        self.assert_contract_error(records, "EXACTLY_ONE_MAIN_ACTION_REQUIRED")
        self.assert_contract_error(records, "EXACTLY_ONE_CAMERA_IDEA_REQUIRED")

    def test_mother_state_cannot_disappear_in_reaction_shot(self) -> None:
        records = copy.deepcopy(self.records)
        records[2]["mother_state"] = {"weather": "无雨", "ground": "干燥"}
        self.assert_contract_error(records, "MOTHER_STATE_DRIFT")

    def test_next_start_must_equal_previous_end(self) -> None:
        records = copy.deepcopy(self.records)
        records[2]["start_state"]["props"]["文件夹"]["holder"] = "人物B"
        self.assert_contract_error(records, "START_STATE_DOES_NOT_MATCH_PREVIOUS_END")

    def test_vo_requires_closed_visible_mouths(self) -> None:
        records = copy.deepcopy(self.records)
        records[3]["sound"][0]["visible_mouths_closed"] = False
        self.assert_contract_error(records, "VO_REQUIRES_VISIBLE_MOUTHS_CLOSED")

    def test_completed_event_cannot_repeat(self) -> None:
        records = copy.deepcopy(self.records)
        records[3]["event_id"] = records[2]["event_id"]
        self.assert_contract_error(records, "EVENT_ALREADY_EXECUTED")

    def test_empty_shot_rejects_any_human_trace(self) -> None:
        records = copy.deepcopy(self.records)
        records[1]["empty_shot"] = True
        records[1]["empty_shot_proof"] = {
            "human_presence": False,
            "human_shadow": False,
            "human_reflection": False,
        }
        self.assert_contract_error(records, "EMPTY_SHOT_CONTAINS_HUMAN_TRACE")


if __name__ == "__main__":
    unittest.main()
