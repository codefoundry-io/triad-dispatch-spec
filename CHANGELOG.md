# Changelog

## rev-2 implementation candidate — 2026-09-20 (not tagged)

- B `6653bdc` completes shared exit-map parity and C28 loader resolution; source-pinned A follow-up and actual
  two-OS/four-leg evidence are in `spikes/2026-09-20-b-wrapper-contracts.md`. C28 evidence custody remains D-B2;
  D-5 project roster location is recorded as a pending proposal. No shared schema, prompt, expected case or tag changes.

- Materialize the aligned v2 verdict, named roster overrides/resolved roster and common transport vocabulary as JSON
  Schema Draft 2020-12. Validate with maintained `jsonschema`; preserve existing Pydantic boundaries and CLI-native
  capabilities without a new schema engine or vendor SDK. Rules: R-AGREE, R-ROSTER, R-BIND, R-RECEIPT; cases C9–C14,
  C19–C23. Host implementation and adoption are not claimed by schema tests.
- Align all three family prompt pins with required evidence/coverage/uncertainty and complete v2 binding. Resolve
  packet filenames through host mappings; retain A-only raw-tail and active hook/audit controls. REVIEW stays no-web;
  INVESTIGATION retains its authorized web trigger. Do not activate B's dormant hook.
- `decisions/rev-2-implementation-spec.md` defines the exact shared-first implementation boundary, legacy development
  gate compatibility and verification sequence. D-B1 policy composition and D-B2 private evidence custody remain
  pending owner decisions. rev-1 acknowledgement rows and normative pin are unchanged.
- Authoring checks include the reproduced terminal-newline path/binding rejection and the shipped example's schema
  identity. Units touched: verdict-wire, roster, engine-transport, prompts; common behavioral fixture C30 added.

## Unreleased authoring proposal — 2026-09-20

- Owner-requested `R-AUTHORING-SYNC`: latest remote source checks, same-commit cross-host design review, and three-family
  diagnosis for any omitted existing functionality. One normative location with identical shared agent-entry pointers.
- Owner-directed Codex-first sequencing: B develops and verifies, audits the corresponding A source at each change,
  and accumulates line-based follow-up instructions while A remains unchanged. A's implementation or reply does not
  block B work under settled contracts; unresolved common contract decisions retain their existing boundary.
- This proposal does not extend the acknowledgements on basis `bd506054`, adopt a host revision, tag a revision, or
  authorize a design change. Claude leader review of this new commit is pending. Host B's preimplementation audit is in
  `decisions/host-b-preimplementation-audit.md`; it records case mapping, evidence, remaining design questions and handoff.

## rev-1 (draft, unpushed as a tag) — 2026-09-19 late

Current verification amendment (Codex; owner-authorized publication):

- `R-GOOGLE`, C15, `contracts/gemini-readonly.verify.toml`: verification-only streaming engine evidence, explicit fixture
  cwd, exclusion distinct from attempted denial, canonical search visibility distinct from aliases, and a discriminating
  catch-all control. Unknown attribution is INCONCLUSIVE; V1–V5 remain NOT RUN. Shipped policy bytes are unchanged.
- `contracts/README.md` points to that single procedure; the v2 mapping table now states its already-aligned choices.
- Evidence and Claude handoff: `decisions/rev-1-codex-verification-amendment.md`. The old Claude signature covers
  `b8b127b`; acknowledgement of this amended basis is pending. No host implementation or tag is authorized here.

Earlier draft amendments (historical sequence; the current manifest supersedes their verification recipes):

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
- Owner directive (2026-09-19, web evidence): the Google research leg's web evidence had degraded (0 page fetches in
  rounds r1 and r2, placeholder URLs in r2). Fixed on host A and measured live; the record is
  `spikes/2026-09-19-google-web-evidence.md` (new `spikes/` folder, `reference/README.md` row). Rule: `R-INVEST`
  web-evidence sentence; clause: `prompts/investigation.md` `web-evidence` (byte-identical to A's constant); case C29;
  `units.json` selected-investigations. Codex: decide where the clause lands on B (its Google review prompt permits web
  reads conditionally; B has no research dispatch mode at 105a1e4) and name B's test after C29.
- Owner D-9 RULED (2026-09-19): review legs have no web tools — explicit deny rows for `google_web_search` / `web_fetch` in
  `contracts/gemini-readonly.toml` (applied on host A too, parity test t50); NEW convention in `R-GOOGLE` for changes that cannot be
  exercised where they are written: apply + a verification manifest, here `contracts/gemini-readonly.verify.toml` (V1-V5, NOT RUN;
  the owner runs them where gemini is in service). C15 rewritten; `R-CONTAIN` gemini bullet; `contracts/README.md` rows. Codex: drop
  the two web tools from B's 999 allow list and name the test after C15.
- Codex rev-1 addendum review (2026-09-19, F1–F8) applied: C28 marked NOT applied on either host (status accuracy); D-9 stated as an
  OPERATION-level rule in `R-CONTAIN` (codex `web_search` off, agy review agents without web — B's read-only builder drops `read_url` for
  review dispatch only, gemini deny rows, review renderers stop permitting web; investigations keep web); manifest V3/V5 rewritten with
  an isolated control (candidate copy + `*` deny), the direct CLI invocation (the wrapper cannot select another policy) and an evidence
  rule (tool-call record or verbatim refusal; never-attempted = INCONCLUSIVE); C28/R-CONTAIN wording (wrapper process cwd, existing
  validations kept, summary line + audit row, run-log is failure-only); Google shape pin added to the v2 migration list; policy vendoring
  = byte-identical (A's file now equals the contract; t50 checks bytes); C4 split original vs owned copy; C29's B column = the clause
  goes on B's authorized web INVESTIGATION invocation (raw dispatch), never the review route; leader-level wire choices ALIGNED in
  `leg-verdict-mapping.md` (`path`, three canonical verdicts, optional `correction`, no `NOT-SAFE`). No new owner question.

Read by: claude leader — OK at `b8b127b` and, separately, OK at the amended basis `bd506054e62b9b1ba5ef5e156ae8928ac414e4bf` (re-verification in `decisions/rev-1-codex-verification-amendment.md`; signature row in `decisions/rev-1-agreement.md`) · codex leader — OK at `bd506054e62b9b1ba5ef5e156ae8928ac414e4bf` · owner tag — pending (both leaders acknowledge the same basis; V1–V5 NOT RUN). rev-0 was tagged at the owner's instruction
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
