"""C15 payload invariants; these are not authenticated policy-engine results."""
import hashlib
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_c15_b_profile_preserves_read_plan_and_catchall_rules_without_web_allow():
    path = ROOT / "contracts/gemini-readonly-b.toml"
    assert path.is_file(), "the separate B contract is missing"
    data = tomllib.loads(path.read_text())
    allowed, denied = set(), set()
    for rule in data["rule"]:
        names = rule["toolName"]
        names = [names] if isinstance(names, str) else names
        if rule["decision"] == "allow":
            assert rule["priority"] == 999
            allowed.update(names)
        elif rule["decision"] == "deny" and rule["priority"] == 999:
            denied.update(names)
    assert allowed == {"read_file", "read_many_files", "list_directory", "glob",
                       "grep_search", "get_internal_docs"}
    assert denied == {"write_file", "replace", "run_shell_command", "enter_plan_mode",
                      "exit_plan_mode", "google_web_search", "web_fetch"}
    assert any(r["toolName"] == "*" and r["decision"] == "deny" and r["priority"] == 998
               for r in data["rule"])


def test_c15_a_payload_is_unchanged_by_b_profile_split():
    data = (ROOT / "contracts/gemini-readonly.toml").read_bytes()
    assert hashlib.sha256(data).hexdigest() == "13d25f61a430cbee082b756a04b6d872d225e1749eeaad55f95e22ad21fa6980"


def test_c15_b_manifest_binds_exact_profile_and_leaves_live_checks_unrun():
    path = ROOT / "contracts/gemini-readonly-b.verify.toml"
    assert path.is_file(), "B profile needs an independent unrun manifest"
    manifest = tomllib.loads(path.read_text())
    assert manifest["policy"] == "contracts/gemini-readonly-b.toml"
    assert manifest["policy_sha256"] == hashlib.sha256((ROOT / manifest["policy"]).read_bytes()).hexdigest()
    assert manifest["status"] == "NOT RUN"
    assert len(manifest["check"]) == 3
    assert all(row["status"] == "NOT RUN" and row["case"] == "C15" for row in manifest["check"])
    assert len({row["id"] for row in manifest["check"]}) == 3


WEB_TOOLS = {"google_web_search", "web_fetch"}


def _rule_rows(path):
    """(tool, decision, priority) per named tool; header comments are ignored."""
    rows = set()
    for rule in tomllib.loads(path.read_text())["rule"]:
        names = rule["toolName"]
        for name in [names] if isinstance(names, str) else names:
            rows.add((name, rule["decision"], rule["priority"]))
    return rows


def test_c32_a_web_profile_moves_only_the_two_web_tools_to_allow():
    no_web = _rule_rows(ROOT / "contracts/gemini-readonly.toml")
    web = _rule_rows(ROOT / "contracts/gemini-readonly-web.toml")
    assert {r for r in no_web if r[0] in WEB_TOOLS} == {(t, "deny", 200) for t in WEB_TOOLS}
    assert {r for r in web if r[0] in WEB_TOOLS} == {(t, "allow", 100) for t in WEB_TOOLS}
    assert {r for r in web if r[0] not in WEB_TOOLS} == {r for r in no_web if r[0] not in WEB_TOOLS}


def test_c32_review_web_manifest_names_both_host_web_profiles_unrun():
    manifest = tomllib.loads((ROOT / "contracts/review-web.verify.toml").read_text())
    profiles = {row["host"]: row.get("policy") for row in manifest["check"] if row.get("policy")}
    assert profiles == {"A": "contracts/gemini-readonly-web.toml", "B": "contracts/gemini-readonly-web-b.toml"}
    assert all(row["status"] == "NOT RUN" for row in manifest["check"])
    assert all((ROOT / p).is_file() for p in profiles.values())
