# Changelog

## rev-1 (draft, unpushed as a tag) — 2026-09-19 late

Amendments from codex's R2 reconciliation (its consolidated document § "R2 reconciliation with the published
specification") and the owner's decisions in codex's session (Q1, Q2, Q3; Q4 pending):

- `R-AGREE`: Minor-only findings do not block the UNCHANGED reviewed bytes; fixing them is a new basis → full re-review
  (Q1). `R-STOP`: CONFLICTED defined as two verification-surviving, mutually incompatible findings. `R-CLEANUP`: delete
  only a provably allocated/claimed resource; empty or plausibly-marked dirs can still be foreign. `R-PREPARE`: separation
  is presentation; symlink rule marked OPEN (Q4). `R-NOCOST`: Pro family + verifiable HIGH on both Google CLIs (Q2; the
  agy slug is not a portable gemini CLI argument; B Auto-only and A unpinned = migration items). `R-ROSTER`: claude
  model/effort as data, `model: null` = host default, explicit Google `route`, adapter-validated timeouts, runnable
  three-leg default vs opt-in entries. `R-BIND`: seeds bind the older field set until D-3. New `R-INVEST` (selected
  investigations) with unit + case C25.
- `prompts/`: `adversarial-framing` replaced by the evidence-centred clause (Q3; D-10 CLOSED); `smell-criterion` wired
  into every leg's order; Google seed caveats (A packet names / hook / fields; web prohibition does not settle D-9).
- `contracts/`: roster example (claude block with model, codex null rule, google `route` + 600 s, second claude arm
  opt-in); exit tokens carry the B delta (`route-mismatch`, `permission-unavailable`, stdin mapping); gemini policy header
  drops the historical Vertex/API-key wording.
- `units.json`: A_source / A_shipped / B columns; `selected-investigations` unit. `cases/`: `input` per case; C21 wording;
  C25.
- `README`: vendoring keeps payload bytes unchanged (adjacent manifest), `reference/` vendored too for offline pinned
  rules, cross-host drift informational vs a host's own failed check = local defect, authoring vs publication.
- A-side SoT inconsistency recorded for A's migration: `leg-contracts.md` still embeds the agy slug and leaves gemini
  unpinned; the focused re-confirm at two SKILL sites; advisory non-gating semantics.

- Round r2 (three families on this draft, 2026-09-19 late): R-AGREE open-question axis; R-BIND split into shipped binding vs
  v2 additions; `contracts/leg-verdict-mapping.md` (D-3 converged); R-CONTAIN precision (process-group reaping, codex egress
  precondition in the SKILL, tool-name controls, no host-internal cites); R-PREPARE symlink = integrity + delivery clauses (Q4
  open, C26); R-VERIFY blocking vs non-blocking; R-SMELL tail; R-ROSTER wording; roster example = illustrative template (no
  `route: auto`, gemini placeholder honest, timeouts); exit-token pre-spawn exception; gemini policy header = enforcement
  PENDING + the inherited-search-allow finding (D-9 owner decision); units packet_files + exception corrections; cases C4
  split, C13 host-neutral, anchors re-pointed, C26/C27; prompts renumbered, D-10 closure wording, D-3 token marker;
  revision labels rev-1. Remaining for codex: split the Google read-grant into shared vs host notices; rename
  `adversarial-framing` → `evidence-framing` at adoption; B columns.

- Owner directive (2026-09-19): relative `--prompt-file`/`--cwd` are resolved against the caller's cwd and recorded, never refused for being relative (R-CONTAIN, C28) — the recurring dispatch failure both wrapper legs hit at round r2.
- Owner Q4 ruled (2026-09-19): review the link itself, never follow its target automatically → R-PREPARE symlink clause and C26.
  D-9 (web tools in review legs) still awaits the owner after a detailed briefing.

Read by: claude leader (author) · codex leader — pending · owner tag — pending. rev-0 was tagged at the owner's instruction
(2026-09-19) before these amendments; they land as rev-1 when the owner tags.


## rev-0 (tagged 2026-09-19 at the owner's instruction, commit dfbeb60) — 2026-09-19

First content from the claude leader after the second agreement round with codex (codex's amendments pending):

- `reference/` — the one-source-per-fact table; the spec-authoring method (owner Q-V: concept only, no UI, no LikeC4);
  review rules with anchors (agreement per owner Q-S, correction re-review, roster per Q-L/Q-M/Q-O, Google leg per Q-N,
  smell criterion, design-change stop, containment inventory with the two verified A-side defects, no-cost/CLI-only with
  the `--policy` and auth-vs-model source findings, platforms); the shared process diagram (codex's second-pass shape) and
  the four failure-diagnosis rules.
- `prompts/` — host A's shipped review text split into a shared clause library + leg-specific clauses with an order list
  (owner Q-U; no clause appears twice); host B's counterpart to be merged by codex from `render_review_prompt`.
- `contracts/` — A's `gemini-readonly.toml` with the header expanded by the version-pinned `--policy` source cite (A's
  substance was right); A's exit-token table as data with the B delta to confirm; a post-cut roster example.
- `cases/cases.json` — C1–C24 seed with rule anchors (C19–C24 added after the fresh-eye check); host test columns partly
  filled (A), B to fill.
- `units.json` — surface → common shipped name → contract → preserved host exceptions → host paths.
- `decisions/owner-register.md` — owner rulings and their effect, site-neutral (verbatim record stays in the host plan).

Amendment 2026-09-19 (owner Q-W): Google review leg default model = the Pro-high tier on either CLI; Flash retired as a
reviewer; the model option is kept only to evaluate future models (`R-NOCOST`, roster example, C18).

Read by: claude leader (author) · codex leader — pending · owner tag — DONE (rev-0 = dfbeb60).

Roster keys deliberately ABSENT in v2 (audit ranks 1-10, owner Q-M/Q-N/Q-O): `substitute_for`, `operation`, `posture`,
`trial`, `sites`; no `legs` subcommand; `vendor` is a family value (`claude` | `codex` | `google`) and the Google CLI is
named only by the `agy` / `gemini` block.
