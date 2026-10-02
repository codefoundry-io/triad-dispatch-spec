# Review strategy amendment — 2026-10-02

Status: shared candidate; host implementation, adoption and formal admission are pending.
Authoring basis: fetched `main` at `6f57ea499a28725da0dbc83bb673378e620c8bfa`.
Owner authority and verbatim decisions: [D-REVIEW-STRATEGY-20261002](owner-register.md#D-REVIEW-STRATEGY-20261002).
The owner received a Markdown change summary before this amendment was applied.

## Evidence and direction review

The owner compared several prompt variants on previously reviewed plans and commits, then asked for research and
independent direction assessment. The local observations are exploratory: single runs, model variation and different
plan/code tasks do not establish a universal ranking of prompt length or prove that detailed instructions suppress
defect discovery. The strategy is an operational choice to preserve broad discovery, adequate context and clear approval.

Research considered includes [VulContextBench](https://arxiv.org/html/2609.32601v1),
[ZeroPath's Opus 4.6 experiment](https://www.eu.zeropath.com/blog/benchmarking-opus-4-6-vuln-detection),
[SWR-Bench](https://arxiv.org/html/2509.01494v2) and
[PerspectiveGap](https://arxiv.org/html/2606.08878v2). Their tasks and models differ from this workflow. In particular,
viewing a ground-truth code block versus citing it in a final report is not a measure of recognizing a defect versus
deliberately withholding it. These sources do not establish an optimal roster, universal role-prompt harm or mandatory
repeat count. No claimed measured quality improvement is a release criterion for this amendment.

Direction reviewers were requested as Astra/xhigh and Opus 5.5/xhigh (`claude-opus-5-5`), with web authorized.
Requested settings are not certification of hidden runtime settings. R1 was independent; R2 was a scoped correction
check with prior findings disclosed, not a new blind experiment. These were selected investigations, not formal reviews.

| Direction review | Astra | Opus 5.5 |
|---|---|---|
| R1 | READY_WITH_NONBLOCKING_NOTES | MATERIAL_OBJECTION: two input/evidence contract gaps |
| R2 | READY | READY_WITH_NONBLOCKING_NOTES; both material objections closed |

The two corrections are concrete:

1. Environment and residual content remain leader-authored prose. Existing checks establish structural input validity,
   binding and faithful transport, not semantic completeness, state transitions or automatic issue deduplication.
   A typed environment/residual subsystem was explicitly rejected as unnecessary scope.
2. Required earlier excerpts, counterevidence and verification results are included in current bound packet surfaces.
   Historical paths alone cannot supply authority or survive temporary-root cleanup. No new packet slot or retention
   extension is needed.

Remaining R2 notes clarified nonempty field checks, existing transport slots, prose versus enum terminology and the
stage mapping. They introduced no new design choice. The direction reviewers did not inspect this later shared-spec
diff or certify host conformance. Same-commit shared-spec review and required host gates remain later steps.

## Current behavior and changed target

The authoritative rules are [review-rules.md](../reference/review-rules.md); this table identifies changes and seams.

| Current or historical surface | Candidate change | Owning unit / case |
|---|---|---|
| R-AGREE admits Minor-only negative; family coverage can require an owner release | Every selected enabled entry explicitly approves; no family minimum; exception remains non-agreement | review-lifecycle, verdict-wire, roster / C13, C33 |
| v2 prompt says pre-merge; legacy has stage vocabulary | One shared plan or code purpose, selected using the existing vocabulary and omission default | prompts, review-lifecycle / C60 |
| Existing TASK/brief and residual strings | Leader writes environment and current issues; host transports without new semantic machinery | prompts / C61, C62 |
| Prior findings can point to earlier records | Materialize evidence needed now in existing currently bound surfaces | cleanup, review-lifecycle / C20, C63 |
| Conflicts/repetition go to the owner | Continue verifiable progress; stop exhausted wording loops without approval | review-lifecycle / C64 |
| Model IDs and efforts are existing roster data | Reuse that single configuration seam and exact CLI IDs; no default/model policy change | roster / existing C12, C22 |
| Observed CLI versions and capability controls | Observed patch is evidence, not an equality pin; retain justified capability/version guards | engine-transport / C65 |

B source checked for the proposal was `8bc6b07684058eccc0ed6e7f632077ef4a207b8c`: stage selection and all-selected
approval require later changes to `bin/review_prompts_v2.py` / `bin/review_round_v2.py`; the existing roster, binding,
retry and cleanup paths are reused. This amendment changes no B product source. The owner explicitly excluded A host
implementation inspection. A entries in `units.json` are earlier source pointers; current A behavior is not asserted.

## Preservation, overlap and adoption

- Keep canonical verdict tokens and fields, duplicate rejection, identity/digest/attempt binding, full-scope re-review
  on changed conditions, failed-to-run-only same-basis retry, containment and directly requested web authorization.
- Keep native host topology, exact model IDs, JSON override precedence, explicit null semantics and existing defaults.
  Do not introduce new model configuration, fallback, catalogue probes or wholesale catalogue-policy changes.
- Preserve host-specific [retention and export](claude-host-v2-implementation-prd.md#PRD-RETENTION): generated brief,
  residual and evidence files follow their existing ownership/lifecycle. No common replacement age limit, scheduled
  cleaner, automatic deletion of durable exports/investigations or cleanup of provider-owned resources is introduced.
- Skill/prompt behavior experiments are outside TRIAD. Static schema, text transport and contradiction checks remain
  valid; a leader reenactment does not certify behavioral improvement.
- Open [PR #6](https://github.com/codefoundry-io/triad-dispatch-spec/pull/6), inspected at
  `29777171c1b7e5d0d0fe0daad969291b0cfed7bf`, changes R-ROSTER/model catalogue policy and quota wording. This draft is
  separate. Reconcile overlapping paragraphs explicitly when integrating; a quota/partial-result owner decision must
  not become all-leg agreement. Its proposed cleanup exception is not adopted here.
- Host adoption must align renderer, phase input and collection in one coherent release. Keep explicitly selected legacy
  entry points distinct; do not reinterpret historical results or claim installed behavior changed with this spec PR.
  The shared-spec commit may be reviewed before adoption without inspecting A implementation code.

## Verification and remaining limits

Shared authoring and schema validation ran on macOS with Python 3.12.13 and pytest 9.0.3 using the repository's existing tools. The phase schema validates a scalar;
its default is an annotation, so the host must implement omission defaulting. Tests do not execute a provider or prove
model review quality. C13/C20/C33 preserve historical results while revised behavior and C60–C65 are NOT RUN on both hosts.

| Check | Status |
|---|---|
| Shared authoring map / references | PASS: `python3 tools/check_authoring.py` — 1 valid map, 0 invalid |
| Canonical schemas, phase boundaries and repository test suite | PASS: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tests` — 114 passed |
| Whitespace / diff integrity | PASS: `git diff --check` |
| New host collection, rendering, retry and cleanup conformance | NOT RUN — implementation has not started |
| New authenticated CLI compatibility / runtime policy | NOT RUN |
| Independent model-quality/skill-behavior experiment | Not part of this amendment |
| Same-commit shared-spec review; revision tag and host adoption | Pending; no prior direction verdict is carried forward |

`contracts/review-strategy.verify.toml` records the deferred host checks using existing cases and operations.
It is a handoff checklist, not authorization to dispatch vendors or an implementation plan.
