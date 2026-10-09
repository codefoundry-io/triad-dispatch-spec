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

## Design choice before dependent code

Two approaches can preserve the existing no-vendor-call contract:

1. Share pure classification/interpretation functions between runtime and replay,
   deriving the same inputs from the existing record and refusing unsupported
   historical records. This avoids a new log field but refactors route code.
2. Record the exact classification inputs and relevant phase in future run logs,
   then verify those inputs. This adds a log surface and requires explicit handling
   of old records and later wrapper overrides; field replay alone must not claim
   full terminal-admission verification.

The common result remains DL-104; native spawning, new error classes and provider
re-execution are excluded. The owner requested a stop for substantial design
changes. B recommends shared pure runtime/replay interpretation to preserve
existing log format and avoid a second approximation of vendor behavior; the
route-refactoring choice is pending before implementation. A may provide its
F3-c design or counterevidence; neither host silently standardizes new log fields.
