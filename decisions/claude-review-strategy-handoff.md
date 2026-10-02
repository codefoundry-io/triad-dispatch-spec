# Claude-host review-strategy implementation handoff

This guide for host A (Claude) follows the normative strategy introduced at shared-spec commit `04245c740afc9be36ad7702a134f71aec8ff0b7f`; it is not a second normative contract.
Use the [single-source map][sources] to resolve any disagreement; change a rule at its
normative location, not by editing this guide into a competing requirement.

Host A implementation and verification of this amendment: **NOT RUN**.
No current A implementation code was inspected for this handoff. Native topology and
historical A source pointers establish neither current behavior nor conformance.
At A implementation start, inspect its actual checkout and applicable instructions,
record its commit/dirty state, and preserve intentional local work.

## Authority and boundaries

The owner authorized Codex-host implementation, testing and code review first, then
necessary same-commit shared-spec review/CI and shared-spec main landing to guide A.
That sequence does not authorize product merge, installation or release on either host.
A adoption, implementation planning, verification and installation remain later steps.
Read [current-source coordination][sync] before adoption and record the shared main SHA;
shared-spec publication and a host's `SPEC_REVISION`/digest adoption are separate claims.

## Normative anchors to implement

| Surface | Normative source | A implementation responsibility |
|---|---|---|
| Phase and purpose | [R-PROMPT][purpose], [stage schema][kind], [shared clauses][clauses] | Select one shared purpose through existing renderer/input surfaces. |
| Configurable roster | [R-ROSTER][roster], [roster schema][roster-schema] | Keep owner selection and exact models in A's existing JSON configuration. |
| Collection | [R-AGREE][agree], [verdict wire][wire], [R-BIND][binding] | Require explicit approval from every selected entry on its exclusive bound attempt. |
| Environment and evidence | [R-CONTEXT][context] | Faithfully bind/transport leader prose through existing brief/evidence surfaces. |
| Changed basis | [R-REREVIEW][rereview], [R-RETRY][retry] | Full current-scope review after changes; unchanged failed-to-run retry stays separate. |
| Finding disposition | [R-VERIFY][verify], [R-SMELL][smell], [R-STOP][stop] | Preserve evidence, bounded correction and nonapproval when verification stalls. |
| Cleanup | [R-CLEANUP][cleanup], [PRD-RETENTION][retention] | Use A's existing ownership/export/terminal/retention lifecycle. |
| CLI compatibility | [R-CLI-VERSION][versions], [R-NOCOST][nocost], [R-AUTH][auth] | Preserve required controls, justified floors and browser-login boundaries. |

`formal-plan` selects `plan-purpose`; `pre-merge` and `implementation-review` select
`code-purpose`. Omission defaults at the invocation boundary to `pre-merge`; explicit
null and unknown values refuse before dispatch. The schema does not insert its default.
The plan clause replaces the code clause. The existing affirmative token approves a
plan as written for implementation, and does not approve future implementation bytes.

The default three-family roster is a convenience. Owner-selected one-leg or same-family
rosters are valid; every enabled entry, including `informational`, must explicitly approve.
A Minor-only negative remains valid wire data and nonapproval. Missing, skipped, failed,
invalid, blocking or unresolved-question results prevent agreement; family count adds no
veto. A leader refutation or owner exception cannot rewrite a negative result.

Mechanical checks establish binding, field/file validity and decoded-value transport.
They do not establish context truth/completeness, semantic deduplication or reviewer use.
The leader distinguishes supported target versions, declarations/lock resolutions and
observed validation versions, and supplies cited facts, assumptions and explicit unknowns.
Preserve A's existing checks; do not add an environment parser or borrow B's packet slots.

For a changed basis, supply one leader-authored current residual as fenced data, with the
needed prior findings, counterevidence and verification excerpts currently bound. Render
it once for every selected leg; do not append transcripts or old residuals automatically.
Historical paths are provenance, not current evidence or implicit access authorization.
Materialize needed evidence before eligible old-root cleanup; use A's existing surfaces.
Preserve A's committed-ledger export, ownership-proven close and host retention rules,
including protections for uncertain, foreign, provider-owned and in-progress resources.

Verify each finding against current bytes, requirements, trigger and impact. Apply the
smallest adequate in-scope correction; substantive contract/design changes go to the owner.
Stop repeating an item when no new evidence addresses it; independently progressing
items may continue. Stop automatic rounds when no remaining item has a concrete
verification path. R-STOP governs reopening and conflicts that survive verification. Preserve dissent/unknowns and the stop reason; quotas,
wording changes and repeated votes cannot create agreement. Structural/static checks of
skills or prompts do not prove model behavior. Do not arrange prompt-efficacy experiments
or treat a leader reenactment as independent evidence; preserve unverified hypotheses.

Keep model/effort changes in the existing JSON roster, with no independently editable
prompt/code copies. Preserve the existing exact CLI model IDs, explicit null overrides
and route-valid Google Pro/HIGH selection; read defaults from the current roster data.
Validate adapter capabilities before inference and expose the resolved roster.
Requested selection is not runtime identity; unexposed identity stays unknown/null.
Observed patch versions are evidence, not equality pins or upper bounds. A later version
alone does not refuse; missing required controls and justified defect floors still do.
The [official Opus 5.5 model documentation](https://code.claude.com/docs/en/model-config) (checked 2026-10-02) states `Claude Code >= 2.1.280`; that selection seam and an independent generic
`2.1.205` seam are B fixture evidence, not a universal A minimum or proof of native A behavior.

## Implementer acceptance cases

The [case registry][cases] defines expected behavior; [verification manifest][manifest]
provides deferred check briefs. Carry the case IDs into A tests and record actual results.

| Case | Required acceptance coverage |
|---|---|
| C13 | All-selected explicit approval; Minor-only negative remains nonapproval; invalid SAFE/blocker/question and missing/failed output cannot PASS. |
| C20 | Changed bytes/conditions create a new full-scope basis; current residual/excerpts survive without transcript auto-append or carried approval. |
| C33 | One/same-family/informational rosters; exclusive named-entry custody; sibling result/receipt swaps fail; retry and changed-phase paths stay distinct. |
| C60 | All three stages, omission, null and unknown; exactly the selected plan or code purpose. |
| C61 | Supported/locked/observed versions and unknowns remain distinct; escaped/non-ASCII context preserves decoded values without semantic-quality claims. |
| C62 | Current residual rendered once for every selected leg; no automatic earlier transcript/residual. |
| C63 | Needed prior excerpts readable in current bound inputs after eligible owned cleanup; foreign/in-progress controls preserved. |
| C64 | Stalled, incomplete, quota-stopped or exception-released round remains non-approved; stop/progress reasoning belongs to the leader. |
| C65 | Newer compatible CLI accepted; missing controls and justified defect versions refused; actual version recorded without runtime inference. |

## Dependency order for A

1. Reconcile the adopted shared basis and current A interfaces using the [implementation map][map]. Freeze the bounded change and applicable capability/containment assumptions.
2. Add provider-free failing fixtures for phase/default/refusal and entry-binding/collection; then implement stage transport and all-selected agreement through existing A machinery.
3. Extend existing shared-clause rendering and current brief/residual transport; prove decoded equality and once-only delivery before touching cleanup tests.
4. Exercise evidence materialization through A's existing export/close lifecycle with negative ownership/in-progress controls; preserve its native layout and numeric retention policy.
5. Verify CLI capability/version behavior and exact model/config resolution at A's actual adapter boundaries; native routes have no CLI version.
6. Align leader guidance with finding verification, scope stops and stalled nonapproval. Run affected A checks, independent review and any separately authorized service checks; record limits and unrun checks explicitly.

Do not replace A's native Claude path, active containment/read-audit or custody helpers
with B's subprocess/packet design merely for symmetry. Historical seams are discovery
leads to recheck locally; these stages prescribe dependencies and behavior, not B APIs.

## Codex-host evidence and publication boundary

- B product source: `f6651121bf775a40f8743c10cd6c3f3590fef88c`; [implementation and verification report](https://github.com/codefoundry-io/triad-codex-dispatch/blob/f6651121bf775a40f8743c10cd6c3f3590fef88c/docs/reviews/2026-10-02-review-strategy-implementation.md).
- B provider-free verification: macOS 26.6.2 arm64 / Python 3.12.13 / pytest 9.0.3: 1818 passed; Ubuntu 24.04.4 arm64 / Python 3.12.3 / pytest 9.0.3 as uid 1000: 1816 passed, 2 filesystem-specific skips. Structural source checks, validator and provider-free lifecycle passed.
- B code review `triad-strategy-impl-20261002-r1`: all four selected legs explicitly approved the bound current source; integrity passed. Requested Opus 5.5/xhigh, Google Pro/high, Flash/high and Astra/high; hidden runtime settings remain unexposed.
- The exact shared-spec review SHA, reviewer results, CI and merge evidence are recorded on [PR #8](https://github.com/codefoundry-io/triad-dispatch-spec/pull/8); this guide does not self-certify its own future commit or host adoption.
- A revised-strategy host tests/service checks: **NOT RUN**; no B result establishes A conformance.

[sources]: https://github.com/codefoundry-io/triad-dispatch-spec/blob/04245c740afc9be36ad7702a134f71aec8ff0b7f/reference/README.md
[sync]: https://github.com/codefoundry-io/triad-dispatch-spec/blob/04245c740afc9be36ad7702a134f71aec8ff0b7f/reference/spec-authoring.md#R-AUTHORING-SYNC
[purpose]: ../reference/review-rules.md#R-PROMPT
[kind]: ../contracts/review-kind.schema.json
[clauses]: ../prompts/common-clauses.md
[roster]: ../reference/review-rules.md#R-ROSTER
[roster-schema]: ../contracts/review-legs.schema.json
[agree]: ../reference/review-rules.md#R-AGREE
[wire]: ../contracts/leg-verdict.schema.json
[binding]: ../reference/review-rules.md#R-BIND
[context]: ../reference/review-rules.md#R-CONTEXT
[rereview]: ../reference/review-rules.md#R-REREVIEW
[retry]: ../reference/review-rules.md#R-RETRY
[verify]: ../reference/review-rules.md#R-VERIFY
[smell]: ../reference/review-rules.md#R-SMELL
[stop]: ../reference/review-rules.md#R-STOP
[cleanup]: ../reference/review-rules.md#R-CLEANUP
[retention]: claude-host-v2-implementation-prd.md#PRD-RETENTION
[versions]: ../reference/review-rules.md#R-CLI-VERSION
[nocost]: ../reference/review-rules.md#R-NOCOST
[auth]: ../reference/review-rules.md#R-AUTH
[cases]: ../cases/cases.json
[manifest]: ../contracts/review-strategy.verify.toml
[map]: ../authoring/maps/claude-host-v2.json
