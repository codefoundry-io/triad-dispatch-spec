# Shared implementation planning and new investigation evidence

Status: authoring follow-up, 2026-10-09. Facts and proposals below do not
claim merge, adoption, release, live service acceptance or a changed model-name
grammar. Current remote main `3afc4d7`, PR #12 `1a5ab9a`, PR #13 `cff8a20` were
rechecked. Both PRs remain open. Each host is implementing concurrently.

## Owner direction and cooperation

Owner, direct Codex session instruction, 2026-10-09:

> claude도 같은 스펙으로 구현을 진행중에 있다는 것을 참고로해 스펙만 존재하고 아직 반영 안된 부분이 있어

The owner requested specification review, a staged execution plan, and bounded
spikes or primary-source research for the five questions below. A pending host
implementation is not by itself a defect or evidence that the rule is wrong.
Check each current rule, code path and measured fact; amend a missing common
contract before dependent code. Claude code is evidence, not presumed authority.
Each host's native leg remains host-owned.

For prompt work the owner specified contextual defects and minimal instructions;
when repeated findings concern fine grammatical/wording nuance, observe choices
in fresh Luna/high scenario/control simulations. This is the Codex task's
development method, not a new shared reviewer-model requirement or an exemption
from either host's existing review gates.

## Evidence dispositions

| Question | Finding | Action and owner |
|---|---|---|
| AGY credits carrier | Vendor changelog 1.2.15 supplies the sentence, not channel/exit. General headless docs describe stdout responses, stderr diagnostics and structured errors; changelog 1.2.6/1.2.10 describes model/API failures with `AGY_ERROR`/3. The specific credits condition is not linked to that path. | Both hosts keep the phrase evidence and unmeasured carrier separate. Supply an existing sanitized capture or record a naturally occurring event; do not exhaust quota or infer the missing fields. |
| DL-103 AGY schema | Current dirty B `bin/verdict_v2.py:45-46` narrows the bound route to `['agy']`; the actual AGY v2 emission no longer has the old null enum. Other schema keywords remain. A's projection is not evidence that every omitted keyword is rejected by AGY. | Update DL-103's current observation when reconciling the rows. B retains a pending live acceptance check; do not reimplement the already-present narrowing. |
| DL-124..126 | Inspected A per-attempt hook attribution, stream simplification and single audit publication are present. Corresponding removed mechanisms are absent in B or already match the described parser behavior. | No new B port identified. A/spec maintainer reconciles historical pointers and cases without claiming total A/B stream-admission equivalence. |
| DL-110/121 | Four current spec descriptions still attribute a Claude CLI route/extractors/tests to A after that route's removal. PR #12 records but does not yet apply all corrections. | Keep `task-blocked` membership; identify B as Claude-wrapper producer; correct A extractor count and C35/37/43 references. A confirms surviving exact test axes/counts. No B Claude-wrapper removal. |
| Model strings shaped like options | Actual Gemini 0.63.0 parser, isolated from provider startup: separate `--model --help` activates help; `--model --yolo` fails parsing; equals-form values remain strings. AGY/Claude help-only observations do not expose resolved model values. | Proposed R-MODEL transport clarification below. No blanket syntax ban or product change in this follow-up. |

Current A source was inspected at `32124be528ab736cad6ac8d8f76990d99bdf3556`;
concurrent source may advance. The named hook/stream/audit files were clean at
inspection; another A test was dirty. B remains `632f426` plus preserved dirty
work. Provider-free B schema modules passed 95 tests with 4 skips, Python
3.12.13/pytest 9.0.3. Fixtures replace vendor execution; no live acceptance claim.

Primary references:

- [AGY changelog](https://github.com/google-antigravity/antigravity-cli/blob/main/CHANGELOG.md)
  (1.2.15 sentence; 1.2.6/1.2.10 general model/API failure behavior).
- [AGY headless errors](https://antigravity.google/docs/cli/headless/#handle-exit-codes-and-errors).
- [Gemini 0.63.0 parser source](https://github.com/google-gemini/gemini-cli/blob/v0.63.0/packages/cli/src/config/config.ts).
- [Official 0.63.0 npm artifact](https://registry.npmjs.org/@google/gemini-cli/-/gemini-cli-0.63.0.tgz),
  SHA-256 `97a6edfc10645463b517f0518d46a8c72efbdc12558a9a948607f726284a0420`.

## Proposed clarification: preserve an opaque model value

Existing requirement: R-MODEL passes the user's explicit pin as written, without
catalog membership gating. Current B uses separate model-option/value tokens
both at Python-wrapper boundaries and in vendor argv. Separate tokens avoid
shell expansion, but do not alone establish lossless option-parser transport.

Evidence: the spike preserved the actual bundled yargs and `parseArguments`
from Gemini 0.63.0, with external startup helpers inert. Separate `-m --help`
and `--model --help` exit 0 through help; separate `--yolo`/`--made-up-model`
values exit 1 for a missing model argument. `--model=...` preserves those values
and does not set yolo. Unknown names and spaces/newlines/tabs inside one token
are also preserved by the measured parser. No inference or permission escalation
was demonstrated. NUL and arbitrary other controls were not tested.

Proposed observable requirement: each host transports the pin as one opaque
model-option value across every wrapper/vendor parser boundary; a value that
resembles another option does not activate that option. A vendor may still
reject the model as unavailable, producing the existing one terminal outcome.
This adds no supported-model list or shared naming grammar. Equals encoding is
a candidate implementation, not a mandated universal spelling: verify each
actual parser before using it.

Features to preserve: unknown ordinary pins, requested/observed identity
separation, CLI floor and capability checks, authentication/containment, exact
receipt bindings, no silent model/route substitution and no repair retry merely
for an unavailable model. Test the Python-wrapper boundary as well as the vendor.

Request to the other maintainer: review this evidence against the same shared
revision, inspect A's model argv construction, and identify an existing common
case or add the boundary to C18/C34 after agreement. Report exact parser/version
evidence for AGY/Claude if available; a help-only exit cannot prove the model
value that inference would receive. Codex keeps dependent product changes out
until the shared disposition and applicable gates are satisfied.

## Documentation reconciliation requests

- PR #12's body/title only names early phases while its files now record
  DL-118..126. Distinguish completed source work from pending rule/case edits.
- PR #13's original body says no normative change and cites the first failed
  C43 round. Its later commits contain D-GEMINI-FLOOR-20261009 and successful
  bounded review evidence. Rewrite the description around the final scope when
  publishing this follow-up; do not erase historical failed evidence.
- DL-121: update the exit-token note, A's extractor description and C35/37/43
  test pointers. Confirm remaining test axes with A rather than guessing counts.
- DL-124..126: preserve earlier DL-6/10/11/12/13 as history and append the
  current limits/removals; align C1/C23/C36 and the `read-audit-file:` custody
  description with A's actual code.
- Current B findings and completed Google/quota work supersede stale OPEN-B
  observations only within their demonstrated scope. Neither PR is full host
  conformance, and a pending A implementation is not a reason for B to diverge.

The Codex execution plan is in its source repository at
`docs/superpowers/plans/2026-10-09-shared-spec-execution.md`; its live SoT remains
`docs/status/spec-to-code-sot.md`. Detailed local parser and schema evidence is
retained under `_runs/spec-plan-20261009/`. Those files are evidence, not an
additional shared runtime interface or installed instruction.
