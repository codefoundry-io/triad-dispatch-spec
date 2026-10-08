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


def _vendor_lines():
    return json.loads((ROOT / "contracts/vendor-failure-lines.json").read_text())["lines"]


def test_vendor_failure_rows_match_their_own_sentence_with_a_known_token():
    # R-CLASSIFY: each row's lowercase match part is part of its sentence, and its token is a contract token.
    tokens = {t["token"] for t in json.loads((ROOT / "contracts/exit-tokens.json").read_text())["tokens"]}
    for row in _vendor_lines():
        assert set(row) >= {"cli", "line", "match", "carrier", "token", "observed"}, row
        assert row["match"] == row["match"].lower() and row["match"] in row["line"].lower(), row
        assert row["token"] in tokens, row


def test_agy_print_timeout_row_is_a_timeout_on_agy():
    # Observed 2026-10-03 on host A: agy returned a partial answer at vendor exit 0 (authoring/shared-dev-log.md DL-62).
    rows = [r for r in _vendor_lines() if "print timeout" in r["line"]]
    assert [(r["cli"], r["token"]) for r in rows] == [("agy", "timeout")]
    assert "[agy] " in rows[0]["carrier"] and "any vendor exit" in rows[0]["carrier"]


def test_codex_incorrect_api_key_row_is_oauth_env():
    # R-AUTH / C37: the measured codex 401 line (host A gate-1 r18, 2026-09-25); no credential text in the row.
    rows = [r for r in _vendor_lines() if "incorrect api key" in r["match"]]
    assert [(r["cli"], r["token"]) for r in rows] == [("codex", "oauth-env")]
    assert "sk-" not in rows[0]["line"]
    # R-CLASSIFY: the measured vendor wording, never the bare phrase the spec and instructions quote.
    assert rows[0]["match"] == "unexpected status 401 unauthorized: incorrect api key"


def test_agy_ai_credits_row_is_a_subscription_cap_from_the_vendor_source():
    # R-CLASSIFY: agy changelog 1.2.15 quotes the sentence for an exhausted plan quota with no AI credits.
    rows = [r for r in _vendor_lines() if r["match"] == "your ai credits balance is too low to continue"]
    assert [(r["cli"], r["token"], r["line"]) for r in rows] == [
        ("agy", "cli-subscription-cap", "Your AI credits balance is too low to continue.")]
    assert "changelog 1.2.15" in rows[0]["observed"] and "not captured" in rows[0]["carrier"]


def test_c31_names_no_claude_cli_route_on_host_a():
    # owner 2026-10-08 (D-OWNER-ANSWERS-20261008 item 2): the claude family runs natively on host A
    assert cases()["C31"]["tests"]["A"].startswith(
        "n/a — host A runs the claude family natively and has no claude CLI route (D-OWNER-ANSWERS-20261008)")


def _rule(anchor):
    text = (ROOT / "reference/review-rules.md").read_text()
    start = text.index(f'<a id="{anchor}"></a>')
    end = text.find('<a id="R-', start + 1)
    return text[start:end]


def test_r_threat_splits_per_folder_from_machine_level_concurrency():
    # owner fact 2026-10-08 (D-CONCURRENCY-FACT-20261008): one folder runs one operation at a time; folders and hosts do not
    rule = _rule("R-THREAT")
    assert "D-CONCURRENCY-FACT-20261008" in rule
    assert "There is no concurrent operation" not in rule
    assert "machine-level" in rule
    assert "D-CONCURRENCY-FACT-20261008" in cases()["C68"]["expected"]


def test_agy_finish_resubmission_is_a_shared_admission_rule():
    # owner 2026-10-08 (D-OWNER-ANSWERS-20261008B item 7): kept on both hosts, written beside the agy admission
    rule = _rule("R-CONTAIN")
    assert "D-OWNER-ANSWERS-20261008B" in rule and "a LATER `finish`" in rule
