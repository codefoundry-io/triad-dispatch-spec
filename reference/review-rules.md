# Review rules — the one normative location

Both hosts implement these rules. Each carries an anchor; `process.md`, `cases/cases.json`, `units.json` and the host
skills reference the anchor. Owner rulings are quoted from `decisions/owner-register.md`.

## Agreement

<a id="R-AGREE"></a>
A round is agreed when NO unresolved BLOCKING finding remains from any participating leg (owner Q-H / Q-Q / Q-S). A
verified Critical or must-fix finding blocks whatever leg raised it and whatever label the leg carries. A MERGE WITH FIXES
whose findings are all non-blocking counts as agreement; the non-blocking findings are recorded and fixed without another
full round (owner Q-S: "Minor-only MERGE WITH FIXES counts (no extra round)"). A missing, failed, invalid or unresolved
non-affirmative result is not agreement. A block is released only by a probe that refutes the finding, a fix confirmed by
the re-review, or a recorded owner decision. The leader verifies findings with evidence; a vote decides nothing. The
leg-facing clause reserves MERGE WITH FIXES for a blocking finding (`prompts/common-clauses.md § verdict-selection-rule`);
a Minor-only MERGE WITH FIXES still counts as agreement per Q-S and is recorded as a verdict-selection deviation. A round
in which fewer than three families returned a verdict is released only by a recorded owner decision (shipped CFR rule 1;
owner Q-L). The wire representation of "agreed" (verdict tokens, finding fields) is `contracts/leg-verdict.schema.json`
after the D-3 round.

## Correction re-review

<a id="R-REREVIEW"></a>
Any correction to reviewed content or to the review conditions (prompts, criteria, roster, model, effort, route, policy)
creates a new bound basis, and EVERY participating leg reviews the complete agreed scope again. Previous findings and
their rebuttal evidence are delivered as input (the prior residual table, fenced as data); previous approval never carries
forward to changed bytes. The shipped "one focused re-confirm scoped to the wave's hunks" is withdrawn on both hosts.

<a id="R-RETRY"></a>
When a leg failed to RUN and nothing changed (source, prompts, criteria, roster, model, effort, route, policy), retry only
that leg on the same bound basis (owner Q-C). Before any dispatch exists, retry the corrected preparation step.

## Roster

<a id="R-ROSTER"></a>
The default round is a three-family review — claude, codex, google — with at least three legs (owner Q-L: "3자 리뷰가
기본이야 나머지는 대처제이고 3자리뷰 모델은 교체가능해야해"). Every leg is an entry in the roster file with a recommended
default model and effort, changeable at any time; the number of legs is variable (owner Q-M). No leg carries a special
rule. `acceptance` is an operator-set data field with a recommended default per leg; no rule is derived from it (owner
Q-O) — R-AGREE decides what blocks. Additional legs (a second claude arm, a trial model) are ordinary entries. When a leg is
switched off or breaks, another entry may be enabled in its place — a different model, or the same model with a different
perspective (owner D-4); the round receipt records which legs actually ran and their family coverage: two legs of one
family are one family (the release valve for a short round is R-AGREE). `vendor` is a FAMILY value — `claude` | `codex` |
`google`; the Google CLI is named only by the `agy` / `gemini` block (R-GOOGLE). Selected investigations (custom prompt, web, extra read roots) are not review rounds and return no verdict
(owner Q-D). Model and effort must be expressible for every vendor in the roster file; a host validates them against the
vendor's actual capabilities at dispatch. No configuration is a shared user-global dependency; the resolved roster is
shown before any paid dispatch, and unselected legs are never started.

## Google leg

<a id="R-GOOGLE"></a>
agy and gemini are different CLIs of one family. Each host keeps its SHIPPED resolution: A — explicit pin, else agy if
installed, else gemini, else skip and log; B — `select-google-route` with its authentication-class gate (owner Q-N: keep
the existing fallback logic). The resolved route, binary and observed CLI version are frozen for the attempt and recorded;
a started leg never switches route silently. The "neither installed" outcome differs by host (A skips and logs, B refuses)
and is recorded as host policy; neither outcome is agreement. Gemini is spec-maintained where only agy runs and tested
where gemini is in service; the owner tests it and briefs the leader, who records the briefing (owner Q-N).

## Code-smell criterion

<a id="R-SMELL"></a>
The common brief carries ONE code-smell criterion — the clause `smell-criterion` in `prompts/common-clauses.md` (owner R2).
No dedicated smell reviewer, no extra test-strengthening round. A confirmed correctness or security defect is not downgraded
because its fix needs a larger change — that is R-STOP.

## Design-change stop

<a id="R-STOP"></a>
A finding whose fix requires changing the gated plan or design — a new contract, a new public definition, a restructured
order of operations — goes to the owner before any design work starts. A CONFLICTED item between legs, or an OSCILLATING
round (the same item flipping without new evidence), is an owner call at first occurrence. A round whose remaining
findings are all speculative or repro-failed is TERMINAL: record the residuals; the owner decides any blocking row. Line
or size growth alone is never a stop or an owner question; it is disclosed with its measured figures and the work continues.

## Containment and validity — what exists today and must survive

<a id="R-CONTAIN"></a>
Review legs read; they do not mutate, execute the candidate, or spawn vendors. No alignment may introduce a dangerous /
yolo permission bypass on any leg (A's only existing bypass is the agy permissive-baseline headless flag, outside the review
path — `3rd-Agent/CLAUDE.md § Safety boundary`). A leg a host runs natively stays native; no leader-model CLI subprocess is
added for symmetry. Per vendor, the guards that ship today and must survive any alignment (host, symbol):

- codex leg (A `codex_wrapper.py`, command builder): selected read-only sandbox, `approval_policy=never`, `--ignore-rules`
  on every posture, `web_search="disabled"` unless search is selected; selected search keeps the packet-egress
  precondition. These are A's wrapper controls, not instructions for B's native session.
- gemini leg (A `gemini_wrapper.py`): approval modes pinned to `default` / `auto_edit` (plan and yolo removed), the
  read-only × auto_edit conflict refusal, the read-only policy-file precondition, the hardened-install read-only default,
  write posture requires `--cwd`; B: `--help` capability preflight, policy self-check, credential/endpoint/model-selector
  variables removed from the child on the formal route. Effective posture is computed BEFORE the conflict and policy checks
  (verified defect on A: the hardened default is assigned after the checks).
- agy leg (A): per-round PreToolUse allow-list hook + hook load check + read-audit gate; B: non-mutating project route;
  B's hook stays dormant until separately agreed.
- all wrappers: binary presence; stdin delivery confirmed or refused (fail closed); process group captured at spawn and
  reaped; reader and writer completion before success (verified gap on both: a decode error or a surviving descendant can
  leave a "successful" prefix — R-TERMINAL); schema validation with one clean repair retry where a leg relies on it; verdict
  binding to review id, family and content digest; round integrity capture/verify.
- cleanup: refuses without deleting when a tree is not provably its own; ownership is proven by an allocation record or
  marker, never by a name shape (verified defect on A: the `.pruning` reclaim branch deletes on name shape alone; B's stale
  sweep accepts same-uid/prefix/age without provenance).

<a id="R-TERMINAL"></a>
Transport success requires: process exit collected, all reader threads joined without error, the owned process group
reaped, stdin delivery confirmed. A settings-guard release failure after a completed transcript is still a failure; the
transcript is preserved. A display-mirror failure is distinct from a failure to capture the result.

<a id="R-TOKENS"></a>
Every classification token a host EMITS is a member of `contracts/exit-tokens.json` and maps to the same exit code there;
wrapper-only tokens and compatibility aliases are listed explicitly as exceptions. A membership test replaces the vacuous
`is not None` assert shipped on both hosts.

<a id="R-RECEIPT"></a>
The transport receipt and the audit / run-log records carry the agreed field vocabulary (`contracts/receipt-fields.json`,
NOT YET in rev-0): stdin delivery class, resolved route, binary, observed CLI version, attempt.

<a id="R-BIND"></a>
Every leg's result binds `review_id`, leg identity, attempt, family, resolved route and content digest; a mismatch is an
INVALID leg, never a pass.
Duplicate JSON members are rejected at the original-text boundary before extraction or normalization can discard evidence
(verified gap: A's wrapper schema path and file path accept duplicates; only the raw-reply admission rejects).

## Preparation, verification, cleanup (lifecycle obligations)

<a id="R-PREPARE"></a>
`prepare` pins the reviewed basis (commit + content digest), writes the brief, the CODE-only gated patch and the test
patch separately, the history, and the per-round containment artefacts the host uses (A: the agy PreToolUse hook); resolves
the roster from the registry with the recommended defaults; prints one COMPLETE dispatch line per enabled leg; captures the
round snapshot. It refuses on a malformed registry entry and never launches a provider itself. A change to a rule,
schema, prompt clause or policy file is behavioral review scope even when the file contains only text; the docs-never-gate
rule covers narrative documentation only.

<a id="R-VERIFY"></a>
The leader verifies every finding against the reviewed bytes before acting: REAL (reproduced) → minimal fix and full
re-review (R-REREVIEW); refuted by a probe → recorded refutation, source unchanged; design or scope change → R-STOP;
speculative → recorded residual, no code. Reviewer labels are claims, never repair instructions; a vote decides nothing.

<a id="R-CLEANUP"></a>
Cleanup exports and verifies the round's evidence first, then releases only resources the helper can prove it allocated
(marker or allocation record — never a name shape); it refuses without deleting, states what it observes, and points at the
one documented recovery when a tree is not its own. A second cleanup is a no-op. Cap-based pruning of run-log and repair-IPC
files keeps a minimum age floor so a fresh sibling file is never deleted to satisfy a cap (mtime is not only a sort key).

## No cost, CLI only

<a id="R-NOCOST"></a>
Both hosts call vendor CLIs only — no vendor HTTP API, SDK or API key. Login is the user's own OAuth login in each CLI;
wrappers check the binary and never enter or store credentials. Billing follows the AUTHENTICATION type, not the model
flag (Gemini CLI v0.60.0 `contentGenerator.ts`: auth is selected before the model is resolved); environment scrubbing and
the absence of `-m` are hygiene, not proof of the billing route. Default model for the
Google review leg (agy or gemini): the Pro-high tier — Flash was retired as a reviewer (0 unique blocking defects over ten
rounds, owner 2026-09-14) and lower tiers are not review-capable (owner 2026-09-19). The slug is a dispatch-time value in
the roster's `agy` / `gemini` block, never a constant in code; the model option stays selectable only so a future model can
be evaluated, and a host validates the chosen value against the catalog its route exposes. Deterministic
provider-free checks (help, version, policy, argv, env, preflight) stay in each host's automated suite; only authenticated
service checks go through the owner-briefing route (R-GOOGLE); an unrun authenticated check is unverified, never green. Gemini formal review requires CLI
`>= 0.34.0` (PR #20639 lands the headless policy-allow fix) and tests the declared supported range. Gemini `--policy`
REPLACES the user-tier policy directory only; system/admin, workspace and built-in defaults still load (v0.46.0 and
v0.60.0 `packages/core/src/policy/config.ts`), so an admin policy can outrank the wrapper's denies; the CLI help string
"Additional policy files" is misleading and the wrapper's TOML header is right.

## Parity scope

<a id="R-PARITY"></a>
Parity covers option names, types, defaults, scope, refusal behavior and the declared host exceptions of every shared
surface (`units.json`: `common` name + `exceptions`); a matching filename alone is not parity. Host-native internals, test
trees, install layers and agent registration stay host-specific.

## Platforms

<a id="R-PLATFORM"></a>
Both hosts support macOS and Ubuntu 24.04 across install, preflight, dispatch, collection, validation and cleanup;
results are recorded per platform; an unrun check is unverified, never green.
