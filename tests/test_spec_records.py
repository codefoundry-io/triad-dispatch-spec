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


def test_c68_threat_model_case_cites_its_rule():
    case = cases()["C68"]
    assert "R-THREAT" in case["rule"]


def _footer_ids(label):
    text = (ROOT / "authoring/shared-dev-log.md").read_text()
    line = next(l for l in text.splitlines() if l.startswith(label))
    return set(re.findall(r"DL-\d+", line))


def _status_ids(pattern):
    ids = set()
    for line in (ROOT / "authoring/shared-dev-log.md").read_text().splitlines():
        m = re.match(r"^\| (DL-\d+) \|", line)
        if m and re.search(pattern, line.rstrip().rstrip("|").rsplit(" | ", 1)[1]):
            ids.add(m[1])
    return ids


def test_dev_log_footer_matches_the_status_cells():
    assert _footer_ids("Rows with B work open:") == _status_ids(r"OPEN \(B")
    assert _footer_ids("Rows with A work open:") == _status_ids(r"OPEN \(A")
    assert _footer_ids("Checks suggested for B:") == _status_ids(r"CHECK-B")
    assert _footer_ids("Rows awaiting the owner:") == _status_ids(r"(?:^|; )OWNER")
