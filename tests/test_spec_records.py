"""Record integrity of the case corpus and the shared development log (one id, one row)."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cases():
    return {case["id"]: case for case in json.loads((ROOT / "cases/cases.json").read_text())["cases"]}


def test_dev_log_ids_are_unique_and_increasing():
    # Ids held by other unpublished spec branches leave gaps (authoring/shared-dev-log.md).
    ids = [int(n) for n in re.findall(r"^\| DL-(\d+) \|", (ROOT / "authoring/shared-dev-log.md").read_text(), re.M)]
    assert ids == sorted(set(ids))


def test_dev_log_rows_name_existing_cases():
    known = cases()
    for row in re.findall(r"^\| DL-\d+ \| ([^|]+)\|", (ROOT / "authoring/shared-dev-log.md").read_text(), re.M):
        for case_id in re.findall(r"C\d+", row):
            assert case_id in known, (case_id, row)


def test_c66_sealed_attempt_case_is_owned_by_review_lifecycle():
    case = cases()["C66"]
    assert case["surface"] == "review-lifecycle"
    assert "R-BIND" in case["rule"]
    assert case["tests"].get("A", "").strip() and case["tests"].get("B", "").strip()
