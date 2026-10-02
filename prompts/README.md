# prompts/ — the one editable copy of the review prompt text (owner Q-U)

`common-clauses.md` is the shared clause library; `leg-codex.md`, `leg-google.md`, `leg-claude.md` carry each leg's own
clauses and the ORDER in which a host renderer concatenates shared and leg clauses. Each clause is named after the rule
anchor it implements (`reference/review-rules.md`). A renderer fills the placeholders and never rewords a clause; the
vendoring rule is `README.md` § How a host uses a revision. `investigation.md` holds the clauses of a RESEARCH
dispatch (`R-INVEST`, not a review): today one clause, `web-evidence`, appended LAST by the host on every web-enabled
Google research prompt (case C29).

Seed state (rev-0 draft): host A's shipped text, dumped verbatim and split into clauses — no text appears twice. Host B's
counterpart (codex `render_review_prompt` / `render_worktree_review_prompt`, `references/review-prompt-contract.md`) is
merged by codex: same meaning in different words → one wording survives; different substance → a `decisions/` item.
D-10 CLOSED (owner Q3): evidence-centred clause; a no-defect conclusion is allowed. The 2026-10-02 amendment moves `smell-criterion` to leader triage under R-SMELL; it is no longer mandatory text in the default leg order.

Token vocabulary inside `severity-instruction`, `verdict-selection-rule` and the claude shape/integrity clauses is host A's shipped set pending D-3 (`contracts/leg-verdict-mapping.md`); a host renders its own tokens until the v2 wire lands. Seed provenance = host A's shipped text at the rev-0 dump; the current draft is rev-1.

## Review purpose and current context (candidate, 2026-10-02)

`review_kind` uses [the existing stage vocabulary](../contracts/review-kind.schema.json).
At invocation, omitted means `pre-merge`; schema defaults are annotations and do not populate it.
`formal-plan` selects `plan-purpose`; `pre-merge` and `implementation-review` select `code-purpose`.
Fill `<review-kind>` with the resolved value and `<review-purpose>` with exactly one selected clause.
The plan clause replaces the code clause. Bind the resolved kind and rendered text to the existing round basis;
unknown or null input refuses preparation. This is a small extension of the existing renderer/request, not a new engine.

Every leg receives the same semantic goal, common criteria and current evidence; identity, native tools and shape notices
remain host-specific. First-review defaults contain no per-leg persona or long smell checklist. Selected investigations
retain custom framing. Use `current-basis` with the existing leader-authored `prior_residual` string; do not append old
rounds automatically. Data fencing remains in force. There is no new table parser or state machine.

[R-CONTEXT](../reference/review-rules.md#R-CONTEXT) owns the leader's environment authoring guidance. The host transports
that TASK/brief text and existing evidence faithfully; it does not supply missing facts or validate semantic completeness.
Necessary earlier evidence is materialized in currently bound existing packet surfaces before old temporary roots expire.
Decoded-value comparison checks transport across JSON escaping; it does not prove content accuracy or review quality.

These clauses are a shared candidate. Adoption must update the consuming renderer, phase input and collector coherently;
historical host tests do not certify this amendment. Explicit legacy entry points keep their declared old contract and
must not advertise the new approval behavior until adopted. No model ID/default is changed by prompt selection.
