# Codex conformance audit and Claude follow-up — 2026-10-08

Status: implementation in progress; no adoption, release or full conformance claim.
Authoring basis: fetched main `3afc4d7` on 2026-10-08.
Rules remain at their existing anchors; this document records evidence and work.

## Owner scope

The owner asked Codex to review the specification and begin implementation,
checking uncertain items against Claude source and writing shared gaps and
Claude follow-up requests into this repository. The owner clarified:

> 각자 host leg는 참견하지 말도록해 네이트비는 알아서 잘하니까ㅣ

Each host owns its native leg. This audit excludes native spawning, presets,
model/effort configuration and native implementation choices. Shared inputs and
result contracts remain the interface. Common non-native behavior should follow
the same specification; an existing implementation difference alone is not a
reason for another host exception. Neither host's code is presumed correct.

## Current evidence

B source baseline is `632f42633d3a92d6cb27168cd15c4d4debd8558c`, the candidate
tree subsequently merged by PR #39. Existing local changes to `verdict_v2.py`
and two v2 test files are separate and preserved. The old October 2 pre-implementation
checkpoint is historical: the review-strategy implementation already shipped.

A source was inspected at `de9bb3940cef48c7d6fa406a261ab899ee2569f2`
on `impl/claude-host-2026-10`; its export was inspected at `a54299d`
(export source `6b78c1de`). A is being edited concurrently in another folder;
these observations apply to the named commits, not to later unexamined work.

| Shared item | B observation | A observation / follow-up |
|---|---|---|
| C43 / DL-117 quota sentences | Both specified sentences returned `unknown`; a bounded correction adds CLI-specific built-ins. RED: 2 failed, 13 passed before removing two redundant positive parameter combinations; focused GREEN: 40 passed including the exit-token contract. | A recognizes the codex usage sentence but its AGY CLI pattern table has no credits sentence. Add the AGY sentence to its own CLI only; do not broaden a global list. |
| C18 / DL-116 model catalogue gates | AGY `models`, Gemini packaged-list and Claude packaged capability gates remain. | AGY/Gemini gates also remain in the inspected A source and export; P3-3/A2 in A's implementation plan is pending. A code is not evidence that these gates conform. Both hosts implement R-MODEL. |
| C34 / DL-114 aliases | B's `_claude` comparison depends on `explicit_support` from its packaged catalogue. An alias request can bypass the full-ID mismatch check. Preserve the C34 selection check independently before changing defaults. | A native Claude leg is excluded. No native preset change is requested. The shared rule already requires a reported alias selection to remain in its named family/tier. |
| R-AGREE / DL-115 layout | B checks all selected approvals and uses a fresh review root. | A still re-pins in the inspected export; DL-115 assigns the fresh-root migration to A. No B rewrite is needed for this item. |
| R-CLEANUP / DL-77 | B lacks the declared cleanup-root configuration; existing hardcoded roots/floors need a separate coherent migration preserving custody/export proofs. | A's export supplies `cleanup.py` and `cleanup-roots.default.json`; inspect its relevant implementation against the shared cases before porting behavior. |
| DL-107 / DL-109 machine state | B still has a global AGY settings transaction and a config publication gap during bootstrap. | Concurrency impact has not been measured. Follow the existing shared requests; native-leg ownership does not exempt machine-wide shared state. |

## First bounded correction: C43 quota sentences

The governing expected results already exist in `contracts/vendor-failure-lines.json`
and DL-117. No new normative behavior or case is introduced. B changes only
`bin/_common.py` and `tests/test_vendor_quota_contract.py`: the two missing
sentences become `cli-subscription-cap` / 65 on their own CLI. Cross-CLI
negative controls, successful answers, wrapper timeouts and existing scoped
extensions are checked. The codex entry belongs to the shared classifier data;
it does not inspect or change the native Codex leg.

This is a partial C43 implementation. Authentication carrier precedence, AGY
`result.error`, other vendor sentences and full C43 conformance remain open.
The focused test result is not authenticated service evidence or formal review.
Full B regression: 1,846 passed, 4 skipped in 397.24 seconds, on macOS with
Python 3.12.13 / pytest 9.0.3. Independent read-only Sol/medium review found no
defect in the bounded change; the AGY sentence's actual carrier remains
unmeasured. Formal implementation review is NOT_APPROVED. Shared authoring checks:
one map valid; 182 tests passed. These results do not close the remaining rows.

## Request to the Claude maintainer

Review this evidence on the same specification commit. For DL-117, add the
measured AGY credits sentence with a positive classification test and a
cross-CLI negative control, or identify the exact newer source/test that
already implements it. Also supply the AGY quota event's sanitized **CLI version,
exit code, output channel, terminal event fields and exact source or capture
evidence**. The sentence alone is insufficient to choose its carrier. Do not
consume quota just to manufacture this event or treat a synthetic stream
position as an observed vendor fact. For DL-116, report the gate-removal implementation
and verification; the inspected code still contradicts R-MODEL. Correct this
record if newer evidence closes either item. No native-leg work is requested.

Keep necessary uncertainty explicit: a model label not yet measured must not
be invented to claim identity; a mock model-selection test does not prove what
the live CLI emits. Shared contract gaps discovered during these changes go
through R-DECISION-ORDER and R-AUTHORING-SYNC before either host diverges.

## Implementation review and unresolved shared evidence

Round `triad-c43-quota-20261008-r1`: Claude, Google Flash and fresh Astra SAFE;
Google Pro NOT-SAFE with an AGY carrier question. All results validated against
one digest and before/after worktree fingerprints matched:
`ROUND_INTEGRITY_OK`, **NOT_APPROVED**. Prior approvals do not resolve the
remaining negative result. No subsequent implementation unit has started.

Verified against B: `bin/antigravity_wrapper.py:286-303` sends stderr and status
to `classify`, excluding `result.error`; `:321-327` handles zero-exit ERROR
without classification. The new data recognizes the sentence when it reaches
the classifier, but does not prove that the real AGY quota event reaches it.
The existing shared row honestly marks the stream position uncaptured.

The [vendor changelog, 1.2.15](https://github.com/google-antigravity/antigravity-cli/blob/main/CHANGELOG.md#1215),
checked 2026-10-08, confirms the quota sentence but gives neither output
channel nor exit status. Installed AGY 1.3.1 is a Mach-O executable; the
[public vendor repository](https://github.com/google-antigravity/antigravity-cli)
lists documentation/examples rather than the implementation that would settle
this path. These checks do not establish a carrier. Record the missing fact
under R-DECISION-ORDER / D-MEASURED-SHAPES; do not invent wrapper behavior.

Claude also suggested a nonblocking codex JSONL carrier regression. The existing
shared helper path was checked: failed JSONL enters `classify`, and extraction
failure promotion maps matched quota to 65. This concerns the shared helper,
not the native Codex leg. Additional fixture coverage remains follow-up work;
it does not resolve the AGY evidence gap.
