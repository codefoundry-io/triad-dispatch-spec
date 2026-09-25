# Shared development log — defects and drift found while implementing the common items

<a id="R-DEV-LOG"></a>
One log for both hosts and for this specification. While a host implements the
common items (`authoring/maps/claude-host-v2.json`), its leader reads the other
host's released source as it goes (`reference/spec-authoring.md#R-AUTHORING-SYNC`).
Whatever that reading finds — a defect in A, a defect in B, or a rule that both
hosts read differently — is written here as a row, so the host that must act can
find it without a session transcript. Owner instruction, 2026-09-25: the PRD and
the spec move together, B's code is inspected as A implements, and what B must
fix is written into a shared development log rather than a session note.

## How a row is written

1. **Case id first.** A row that describes a behaviour takes a case in
   `cases/cases.json` before anything is fixed (`reference/spec-authoring.md` § 4);
   an existing case is reused when it already states the expected result. A row
   that describes only a record-keeping error (a stale path, a missing pointer)
   reuses the case of the surface it belongs to and mints nothing.
2. **Observation is `file:line` at a named commit.** A repository, a commit and a
   line; never "the code". Host A = `codefoundry-io/triad` (authoring branch named
   in the row); host B = the released `triad-codex-dispatch` tag; spec = this
   repository's `main`.
3. **Host column names who acts.** `A`, `B` or `spec`. A row never edits the other
   host: the owning leader verifies and changes only its own host.
4. **Status vocabulary.** `OPEN` (nobody has acted) · `FIXED-A` / `FIXED-B` /
   `FIXED-SPEC` (with the commit or PR that closed it) · `REFUTED` (the observation
   was wrong; the refutation stays as a row) · `OWNER` (needs an owner decision,
   named in `decisions/owner-register.md` when ruled). A row is never deleted.
5. **Cross-check before a row is written.** When one host is wrong and the other
   right, the row asks the wrong host to port the PROPERTY, not the mechanism.
   When BOTH hosts are wrong or neither implements the behaviour, the defect is
   in this specification: the rule, contract or case is corrected in the same PR
   and the row says so.

## Rows

| id | case | REQ | host | observation (file:line @ commit) | what to do | status |
|---|---|---|---|---|---|---|
| DL-1 | C12 | REQ-ROSTER | spec | `units.json` `roster.A_source` @ `41878ba` still named `review_scratch.py (x-leg config loader, prepare)`; host A's v2 named roster is `.claude/skills/triad-cross-family-review/lib/roster_v2.py` (shipped data `spec/review-legs.default.json` + project override `.claude/triad-review-legs.json`, merged by name, drift warnings, per-entry Google chain), frozen per round in `<packet-dir>/.roster-r<N>.json`. `google-resolution.A_source` named a bash snippet in `leg-contracts.md`; A's v2 chain is per entry in `roster_v2.py` (`tests/unit/skills/t12-roster-v2.sh` axes 9, 16). `verdict-wire`, `review-lifecycle` and `agy-containment` did not name `lib/verdict_v2.py`, `lib/collect_v2.py`, `lib/prompts_v2.py`. (triad `parity/host-a-v2` @ `ce6088d`) | Update the A columns of `units.json`; the B columns are untouched | FIXED-SPEC (this PR) |
| DL-2 | C35 | REQ-ROSTER | spec | `reference/review-rules.md#R-ROSTER` @ `41878ba` recommends an explicit model ID for the Claude leg only; `contracts/review-legs.example.json:23` ships codex `"model": null` ("the host's default codex model"). B ships `gpt-5.6-terra` / `xhigh` as data (`triad-codex-dispatch` v0.2.557 `contracts/review-legs.default.json:12`; `bin/review_adapters_v2.py:67` resolves a null request to the host-exposed default and records it). A ships `null` (`.claude/skills/triad-cross-family-review/spec/review-legs.default.json`), which `3rd-Agent/wrappers/codex_wrapper.py:458-459` turns into NO `-c model=` — the operator's `~/.codex/config.toml` decides the reviewing model (on the authoring machine `gpt-6-astra` with reasoning `ultra`, a tier the wrapper itself refuses to request). Two conformant hosts, two different baselines: a SPEC gap. Owner, 2026-09-25: baseline `gpt-5.6-terra` / `xhigh`; comparison entry `gpt-6-astra` / `high` on host A. | R-ROSTER gains the codex default sentence and the shipped-explicit rule; the example roster carries the ID; C35 added (this PR). A: default roster data `codex.model: "gpt-5.6-terra"` + opt-in `codex-astra` entry in its four-leg example. B: already conformant. | FIXED-SPEC (this PR); FIXED-A (triad `c056a2a`: `spec/review-legs.default.json`, `references/review-legs.four-leg.example.json`, t12 axes 36-37); B conformant |
| DL-3 | C35 | REQ-ROSTER, REQ-CUSTODY | A | With `codex.model: null` the per-attempt record shows no model anywhere: `results-r11/codex/attempt-1/dispatch.json` argv has no `--model`; the audit row's `cmd` has no `-c model=`; the `[wrapper] codex …` summary tail (`3rd-Agent/wrappers/_common.py:1821-1832`) carries `attempt=` and `prompt_file=` only; the transport receipt has no model slot by contract (`contracts/receipt-fields.json`, `additionalProperties: false` — deliberately transport-only). The REQUESTED model is frozen only as `null` in `.roster-r11.json`. B freezes `model`/`effort` in the adapter record and observes `runtime_model` separately (`bin/review_round_v2.py:454-477`, `runtime_identity: unexposed` when the host exposes none). Codex `exec --json` exposes no runtime model (observed stream: `thread.started`, `turn.started`, `item.*`, `turn.completed`). (triad `parity/host-a-v2` @ `ce6088d`) | A: emit `model=<requested>` on the summary tail when a model was requested (absent = the CLI default was used, already frozen as `null` in the round record); runtime identity stays unexposed and is never inferred from the request (C35 expected). No contract change: the model is a REQUEST, not transport. | FIXED-A (triad `c056a2a`: `_common.RunResult.requested_model`, `_summary_tail`, `audit()`, `emit_run_log`, `codex_wrapper.py`; t60) |
| DL-4 | C34 | REQ-ROSTER | A | `.claude/agents/cross-family-review-reviewer.md:5` (and the `-max` / `-high` siblings) pin `model: opus`, the moving alias; R-ROSTER @ `41878ba` recommends the explicit `claude-opus-5-5`. A refuses `claude.model` in the roster by design (the tier rides in the agent id), so the preset frontmatter is A's only pin point; Claude Code sub-agent docs (Tier 1, 2026-09-25) accept a full model ID there. | A: `model: claude-opus-5-5` in all three sibling presets, `effort` unchanged (`xhigh` / `max` / `high`), the t7 mirror test pins the trio; then fill C34 `tests.A`. | FIXED-A (triad `c056a2a`; t7 38/38; C34 `tests.A` filled in this PR) |

No B row is open at v0.2.557 for the surfaces read so far (roster, adapters,
v2 round record, claude wrapper pin). Rows are added as the reading continues.
