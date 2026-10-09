# U4b2: preserve the original classification path during stored-record verification

## Maintainer reply and current evidence

A's [PR13 reply6083248450](https://github.com/codefoundry-io/triad-dispatch-spec/pull/13#issuecomment-6083248450)
agrees with U4b/DL-104, selector withdrawal/C75 and C76. It schedules E-ENV and
E-AUTH74 in Phase6 and F3-a..d in Phase7; these are planned implementations,
not completion evidence. C74's AGY reflection risk is confirmed by A; the Claude
permission-denials half is not applicable to A's removed external Claude route.
C72 toolkit binding is reported implemented, while executed-search proof remains
Phase12 T4. Do not infer native implementation work for B.

Read-only A source92b7fee is clean at this check: both applier caps remain,
three model-selector names remain in the environment exclusions, and source
repair agents still specify Read/Grep/Glob with network off. These snapshots
agree with pending work; no A execution or edits were performed. Shared main
was freshly fetched at3afc4d7; PR13 head142904d at the reply check.

## Provider-free characterization

B632f426 plus the current candidate has a route distinction relevant to DL-104:
`antigravity_wrapper._interpret_run` on nonzero vendor exit calls `classify`
with stderr plus result status and empty stdout. Its stored `extraction_error`
is a diagnostic containing additional terminal-error text, not that input.
`emit_run_log` stores original stdout/stderr and that diagnostic, not the exact
classifier call as a distinct record.

A local synthetic fixture used vendor exit7 and a result ERROR containing a
unique marker only in terminal error text. No CLI or provider was called.
After applying a fixture-only capacity pattern to an isolated extension file:

| Verification path | Result |
|---|---|
| Current actual AGY interpreter, before extension | unknown |
| Same actual interpreter, after extension | unknown |
| Naive classify of saved original stdout/stderr | server-capacity |
| Actual interpreter with the marker in stderr (control) | server-capacity |

The temporary directory was removed and the runner's extension override restored.
This disproves the proposed naive replay approach. It is not a new vendor
incident, production classifier defect, or authorization for adding a phrase.
Neither original streams nor the diagnostic may automatically be treated as the
original classifier inputs. Verification must respect the route's actual path.

## Historical alternatives, superseded by owner simplification

Two approaches can preserve the existing no-vendor-call contract:

1. Share pure classification/interpretation functions between runtime and replay,
   deriving the same inputs from the existing record and refusing unsupported
   historical records. This avoids a new log field but refactors route code.
2. Record the exact classification inputs and relevant phase in future run logs,
   then verify those inputs. This adds a log surface and requires explicit handling
   of old records and later wrapper overrides; field replay alone must not claim
   full terminal-admission verification.

The common result remains DL-104; native spawning, new error classes and provider
re-execution are excluded. These alternatives are historical investigation,
not two active implementation projects or an unanswered owner gate.

## Owner follow-up: minimal implementation

Owner direction, paraphrased: the skill's core is simple; security and separate
execution cwd machinery have increased code. Preserve review points and diff
review, and handle the remaining work simply.

B's planning interpretation: keep review points, diff/worktree and independent
related-code discovery. For U4b2, reuse the existing failed record and actual
classification path; extract only a small reusable function if necessary.
Do not introduce a general replay engine, new log schema, broad wrapper refactor,
additional cwd layers or routine security/read-log audits for this task. Existing
controls are not blindly deleted: any simplification must preserve the applicable
common result contract. An unsupported record is a disclosed verification limit,
not justification to guess a pass or manufacture another subsystem.

The previous architecture-choice question is superseded; B proceeds under this
bounded direction. A's F3-c evidence is still useful but is not a waiting gate.
Neither host's native leg changes. Shared main rechecked at3afc4d7.

## A follow-up and B implementation boundary

A's [reply6083800391](https://github.com/codefoundry-io/triad-dispatch-spec/pull/13#issuecomment-6083800391)
agrees with route-specific interpretation and refusing unsupported records without
a new log field. A reports a feasibility spike over234 stored records and generated
AGY streams; B has not rerun it. A's ordinary failure, extraction demotion and AGY
typed-signal paths describe A's runtime; they are not an instruction to copy those
branches into B. Both implementations must reuse their actual route semantics.

A's live source was then checked read-only atcc6fc3a with concurrent dirty changes
in `3rd-Agent/wrappers/_common.py`, its classifier-extension test and a history
document. `apply_patch.py` still has no `--verify-run-log`; `_common.py` still has
the500-entry/reason caps, and the AGY repair agent still prohibits network. These
are scheduled Phase7/capability work, not claims that A completed them or evidence
of a failed conformance run. No A tests or edits were performed.

B's bounded candidate adds `--verify-run-log PATH` to its existing applier. It
reads the explicitly selected classifier and saved failure without applying a
proposal, executing saved commands or calling a vendor. Matching classification
returns0; mismatch or unsupported evidence returns3. It checks eligible original
failure records, reuses AGY's interpreter and the existing Claude/Gemini
classification/extraction functions, and conservatively refuses unsupported
extraction outcomes. This is classification verification, not full replay of
review admission. The three external dispatch skills link to repair; timeout
and authentication are excluded. Native analyzer spawning remains unchanged.
Verification and review evidence are recorded separately below when complete.

## Review corrections within the existing verification outcome

B's first U4b2 round, triad-repair-replay-20261010-r1, is NOT_APPROVED with
matching source integrity. Both Google legs are SAFE. Claude and fresh Codex
identify a lost output-transport-failure decision: the runtime's private flag
is absent from the stored record, but the existing host-generated diagnostic
identifies the failure. Claude also identifies a same-class false pass and an
empty --verify-run-log value falling through to apply. Its test note identifies
the wrong lock sibling in the new test assertion. These are bounded defects in
the new B verifier, not evidence of new vendor failures or A defects.

R-CLASSIFY/C76 now makes the existing learned-repair claim explicit: require a
usable record and demonstrated classification change; unchanged classification
does not prove the proposal worked. Reject host transport/collection failures
and missing/empty verification input without mutation. B will use the existing
diagnostic fields as eligibility checks only, never as vendor classifier input.
No new log field, causal replay engine, provider call or native mechanism is
needed. A should check the same controls in its planned F3-c implementation;
no A runtime result is claimed. Original review and exact cleanup evidence stay
retained. Corrections require fresh RED/GREEN and a complete fresh review.
