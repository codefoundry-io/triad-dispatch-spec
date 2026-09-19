# prompts/ — the one editable copy of the review prompt text (owner Q-U)

`common-clauses.md` is the shared clause library; `leg-codex.md`, `leg-google.md`, `leg-claude.md` carry each leg's own
clauses and the ORDER in which a host renderer concatenates shared and leg clauses. Each clause is named after the rule
anchor it implements (`reference/review-rules.md`). A renderer fills the placeholders and never rewords a clause; the
vendoring rule is `README.md` § How a host uses a revision.

Seed state (rev-0 draft): host A's shipped text, dumped verbatim and split into clauses — no text appears twice. Host B's
counterpart (codex `render_review_prompt` / `render_worktree_review_prompt`, `references/review-prompt-contract.md`) is
merged by codex: same meaning in different words → one wording survives; different substance → a `decisions/` item.
D-10 CLOSED (owner Q3): evidence-centred clause; a no-defect conclusion is allowed. Proposed, not yet rendered by any host: `smell-criterion` (owner R2).

Token vocabulary inside `severity-instruction`, `verdict-selection-rule` and the claude shape/integrity clauses is host A's shipped set pending D-3 (`contracts/leg-verdict-mapping.md`); a host renders its own tokens until the v2 wire lands. Seed provenance = host A's shipped text at the rev-0 dump; the current draft is rev-1.
