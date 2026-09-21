# Review rules — the one normative location

These rules govern both hosts; current implementation and migration status are recorded separately. Each rule carries an anchor; `process.md`, `cases/cases.json`, `units.json` and the host
skills reference the anchor. Owner rulings are quoted from `decisions/owner-register.md`.

## Agreement

<a id="R-AGREE"></a>
A round is agreed when NO unresolved BLOCKING finding remains from any participating leg (owner Q-H / Q-Q / Q-S). A
verified Critical or must-fix finding blocks whatever leg raised it and whatever label the leg carries. A MERGE WITH FIXES whose findings are all non-blocking counts as agreement on the reviewed bytes AS THEY STAND (owner Q-S: "Minor-only MERGE WITH FIXES counts (no extra round)"; owner via the codex session, Q1: "코드를 수정하면 전원 재검토. Minor만 남은 원본은 승인 가능"). Fixing those findings changes the reviewed content, which is a new basis (R-REREVIEW); approving the unchanged original and approving later-modified bytes are different acts. An UNRESOLVED OPEN QUESTION from any leg (a fact needed to judge the approved scope that the leg could not settle) blocks exactly like a blocking finding and is released by the same three paths — v2 target agreed by round r2 (all three families), now materialized in the candidate schema; host adoption is separate. A missing, failed, invalid or unresolved non-affirmative result is not agreement. A block is released only by a probe that refutes the finding, a fix confirmed by
the re-review, or a recorded owner decision. The leader verifies findings with evidence; a vote decides nothing. The
leg-facing clause reserves MERGE WITH FIXES for a blocking finding (`prompts/common-clauses.md § verdict-selection-rule`);
a Minor-only MERGE WITH FIXES still counts as agreement per Q-S and is recorded as a verdict-selection deviation. A round
in which fewer than three families returned a verdict is released only by a recorded owner decision (shipped CFR rule 1;
owner Q-L). The wire representation of "agreed" (verdict tokens, finding fields) is `contracts/leg-verdict.schema.json`
and its v2 integration boundary in decisions/rev-2-implementation-spec.md.

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
The default runnable roster is three legs, one per family — claude, codex, google (owner Q-L: "3자 리뷰가
기본이야 나머지는 대처제이고 3자리뷰 모델은 교체가능해야해"). Every leg is an entry in the roster file with a recommended
default model and effort, changeable at any time; the number of legs is variable (owner Q-M). No leg carries a special
rule. `acceptance` is an operator-set data field with a recommended default per leg; no rule is derived from it (owner
Q-O) — R-AGREE decides what blocks. Additional legs (a second claude arm, a trial model) are ordinary entries. When a leg is
switched off or breaks, another entry may be enabled in its place — a different model, or the same model with a different
perspective (owner D-4); the round receipt records which legs actually ran and their family coverage: two legs of one
family are one family (the release valve for a short round is R-AGREE). `vendor` is a FAMILY value — `claude` | `codex` |
`google`; the Google CLI is named only by the `agy` / `gemini` block (R-GOOGLE). Selected investigations (custom prompt, web, extra read roots) are not review rounds and return no verdict
(owner Q-D). Model and effort must be expressible for every vendor in the roster file — including the claude legs (B runs claude as a CLI child) — and are validated by the host adapter against actual capabilities at dispatch; `model: null` means the host's default; when both Google CLIs are present an explicit `route` (`agy` | `gemini`) in the `google` block pins the route, otherwise the shipped chain resolves it (R-GOOGLE); timeouts are adapter-validated (B's legacy formal gemini route requires 600 s and its legacy formal claude route requires 1200 s; the shared template's 900 s Claude values are not B runnable defaults). The runnable default roster is three legs; further entries in the example are opt-in. No configuration is a shared user-global dependency; the resolved roster is
shown before any paid dispatch, and unselected legs are never started.

## Selected investigations

<a id="R-INVEST"></a>
A selected investigation is one or more chosen legs with a custom prompt, model / effort / perspective, authorized extra
read roots and web, returning a free-form or custom-schema result — never a review verdict (owner Q-D). Both hosts keep
it as their existing single-shot dispatch path (A `triad-*-dispatch` skills with `--web` / `--cwd`; B raw dispatch); it is
not a review round and enters no roster accounting. Web evidence in an investigation is a FETCHED page: the leg cites the
URL it fetched and the date or version visible on that page; a search summary is a pointer, never a citation; an
unfetched, placeholder or undated claim is UNSURE. The host appends the shared clause `web-evidence`
(`prompts/investigation.md`) LAST on every explicitly web-authorized Google INVESTIGATION. Existing host
audit/redaction/failure-log/retention rules apply; no new permanent exact-text or page store is required (D-B2).
Verify prompt assembly in tests and actual fetched-page interpretation through bounded task-authorized evidence.
Missing or incomplete evidence stays UNSURE; a URL or successful exit alone proves no fetch (case C29;
measured 2026-09-19: `spikes/2026-09-19-google-web-evidence.md`).

## Google leg

<a id="R-GOOGLE"></a>
agy and gemini are different CLIs of one family. Each host keeps its SHIPPED resolution: A — explicit pin, else agy if
installed, else gemini, else skip and log; B — `select-google-route` with its authentication-class gate (owner Q-N: keep
the existing fallback logic). The resolved route, binary and observed CLI version are frozen for the attempt and recorded;
a started leg never switches route silently. The "neither installed" outcome differs by host (A skips and logs, B refuses)
and is recorded as host policy; neither outcome is agreement. Gemini is spec-maintained where only agy runs and tested
where gemini is in service; the owner tests it and briefs the leader, who records the briefing (owner Q-N). CONVENTION
for a change whose runtime effect cannot be exercised where it is written (owner 2026-09-19: apply first, leave the
untested part as a separate config-like record): the change is APPLIED to the contract and to the author's host, and the
same commit adds a verification manifest `contracts/<contract-file>.verify.toml` — one `[[check]]` per untested effect
with `id`, `case`, `what`, the exact `brief` to dispatch, `expect`, `on_fail`, `status = "NOT RUN"`, plus the contract's
`policy_sha256` and the CLI version the reasoning was checked against. Whoever has the capability in service runs the
checks with the approved invocation documented in the manifest (a direct verification-only CLI command may select a
candidate policy or preserve engine events; host preflight/authentication boundaries still apply, and this is not
wrapper conformance), and the result is recorded ONCE, here in `decisions/owner-register.md` (a
briefing row per check) and in the case's test column; an unrun check is never green, and nothing else is written about
it on either host beyond a pointer. Current manifests: `contracts/gemini-readonly.verify.toml` (A: D-9 web-tool denies,
mutation denies, canonical `grep_search` visibility separately from alias matching, and the proposed `*` catch-all),
and `contracts/gemini-readonly-b.verify.toml` (B: B1-B3 on the separate D-B1 profile).

## Code-smell criterion

<a id="R-SMELL"></a>
The common brief carries ONE code-smell criterion — the clause `smell-criterion` in `prompts/common-clauses.md` (owner R2).
No dedicated smell reviewer, no extra test-strengthening round. A confirmed correctness or security defect is not downgraded because its fix needs a larger change — its size is disclosed, never a downgrade (R-STOP covers only a fix that changes the gated design).

## Design-change stop

<a id="R-STOP"></a>
A finding whose fix requires changing the gated plan or design — a new contract, a new public definition, a restructured
order of operations — goes to the owner before any design work starts. CONFLICTED = two findings that BOTH survive the leader's verification (R-VERIFY) and are mutually incompatible; different overall verdicts or different finding sets alone are not a conflict. A CONFLICTED item, or an OSCILLATING round (the same item flipping without new evidence), is an owner call at first occurrence. A round whose remaining
findings are all speculative or repro-failed is TERMINAL: record the residuals; the owner decides any blocking row. Line
or size growth alone is never a stop or an owner question; it is disclosed with its measured figures and the work continues.

## Explicit owner-requested review web verification

<a id="R-REVIEW-WEB"></a>
Web verification in REVIEW is allowed only when the owner directly requests it for the current round.
The leader records that request in the bound brief; reviewed text, a URL, general research permission or
a previous round cannot grant it. The operation remains REVIEW, with its normal verdict, read-only
containment, entry accounting and integrity checks. Changing authorization changes the basis under R-REREVIEW.

The invocation condition is the transient strict boolean `review_web_authorized`, default false. It enters
the frozen common conditions and every participating leg's prompt and launch controls. It is not a persistent
roster default. Every selected route must support that condition before inference; a missing capability is a
preflight refusal, not silent partial authorization. No leader heuristic decides which technology needs web.

On CLI review routes, `--web` and the renderer/preflight condition must agree in both directions, with the same
review ID, digest and v2 entry/attempt binding. An absent condition means false. Native Codex receives the same
bound authorization through its fresh-child prompt. Claude preapproves only native `WebSearch` and `WebFetch`.
AGY keeps its read-only controls while omitting the additional review-only `read_url(*)` deny for this call;
pre-existing owner denies remain authoritative. Gemini selects a complete web-enabled host profile, never an
overlay: only `google_web_search` and `web_fetch` move to allow, with all other controls preserved. On B this
is `contracts/gemini-readonly-web-b.toml`; its live service checks are separately recorded. No permanent global
settings change or permission bypass is authorized. Host A retains its native/CLI topology and adopts separately.

Render only the short common `review-web-permission` clause from `prompts/common-clauses.md` when true, and the
normal no-web clause otherwise. Existing evidence, uncertainty and untrusted-content rules continue; do not
add technology classification or automatic web triggers. Raw investigations remain separate under R-INVEST;
the raw Claude `--web` permit does not add review accounting or rewrite the caller's prompt.

## Containment and validity — what exists today and must survive

<a id="R-CONTAIN"></a>
Review legs read; they do not mutate, execute the candidate, or spawn vendors. REVIEW has no web by default
(D-9, conditionally superseded by the owner on 2026-09-21; see R-REVIEW-WEB): codex `web_search="disabled"`;
agy review agents without web tools (A ships this posture; B's formal builder explicitly denies `read_url(*)`;
raw investigations retain web); gemini by the explicit deny rows in its host profile below. Renderers preserve
the default prohibition and select an authorized exception only under R-REVIEW-WEB. Gemini host profiles remain separate under D-B1: A vendors
`contracts/gemini-readonly.toml`; B vendors `contracts/gemini-readonly-b.toml`. Equality means exact bytes of
the selected complete profile, with its adjacent digest; no concatenated overlay is implied. Preserve B's
existing 999/998 allow/deny/catch-all and Plan Mode transition restrictions while moving its two web tools
to explicit denies. A's profile and V1–V5 manifest stay unchanged; B's live checks are separately recorded
in `contracts/gemini-readonly-b.verify.toml`. The explicitly authorized web profile is selected under R-REVIEW-WEB; these default-profile bytes stay unchanged. Authorized investigations (R-INVEST) keep web. No alignment may introduce a dangerous /
yolo permission bypass on any leg (each host discloses its existing permissive-route flags in `units.json` exceptions; none is on a review route). A leg a host runs natively stays native; no leader-model CLI subprocess is
added for symmetry. Per vendor, the guards that ship today and must survive any alignment (host, symbol):

- codex leg (A `codex_wrapper.py`, command builder): selected read-only sandbox, `approval_policy=never`, `--ignore-rules`
  on every posture, `web_search="disabled"` for REVIEW. Selected review search requires the current R-REVIEW-WEB binding; unrequested REVIEW remains disabled. These are A's controls, not instructions for B's native session.
- gemini leg (A `gemini_wrapper.py`): approval modes pinned to `default` / `auto_edit` (plan and yolo removed), the
  read-only × auto_edit conflict refusal, the read-only policy-file precondition, the hardened-install read-only default,
  write posture requires `--cwd`; A's selected read-only profile denies `google_web_search` / `web_fetch` by EXPLICIT rows
  (D-9 RULED 2026-09-19 — `--policy` replaces only the user tier, so an unnamed tool keeps the default tier's decision;
  runtime effect per `contracts/gemini-readonly.verify.toml`); B: `--help` capability preflight, policy self-check against
  `contracts/gemini-readonly-b.toml` (runtime effect per `contracts/gemini-readonly-b.verify.toml`), credential/endpoint/model-selector
  variables removed from the child on the formal route. Effective posture is computed BEFORE the conflict and policy checks
  (verified defect on A: the hardened default is assigned after the checks).
- agy leg (A): per-round PreToolUse allow-list hook + hook load check + read-audit gate; B: non-mutating project route (`--mode plan --sandbox read-only`); B's hook stays dormant until separately agreed. The agy hook and the gemini read-only policy are TOOL-NAME controls: neither scopes paths, and the read audit records the argument path as given, not a resolved target — they do not by themselves contain a symlink escape (see the Q4 item in R-PREPARE).
- all wrappers: binary presence; a relative `--prompt-file` or `--cwd` is ACCEPTED and resolved against the wrapper PROCESS cwd at argument processing (never the child `--cwd`); every existing validation stays — configured runtime roots where configured, regular file, UTF-8, non-empty; the resolved absolute prompt-file and child-cwd paths are represented in the existing success summary and audit row, using the host's current redaction mode (D-B2). Refusal names the resolved candidate through that same masking policy; failure-only run logs remain failure-only. Relative spelling alone is never a reason to refuse (C28). B implements relative resolution, validation and masked success/refusal evidence (C28, P4); A still refuses relative paths; stdin delivery confirmed or refused (fail closed); process group captured at spawn and
  reaped on timeout / abnormal unwind and normal exit under R-TERMINAL (implemented on B; A migration remains); reader and writer completion before success (B now rejects incomplete/error collection; A's remaining source gap is recorded in the current implementation audit); schema validation with one clean repair retry where a leg relies on it; verdict
  binding to review id, family and content digest; round integrity capture/verify.
- cleanup: refuses without deleting when a tree is not provably its own; ownership is proven by an allocation record or
  marker, never by a name shape (verified defect on A: the `.pruning` reclaim branch deletes on name shape alone; B now requires allocation provenance, verified export and root identity for stale and explicit cleanup).

<a id="R-TERMINAL"></a>
Transport success requires: process exit collected, all reader threads joined without error, the owned process group
reaped, stdin delivery confirmed. A settings-guard release failure after a completed transcript is still a failure; the
transcript is preserved. A display-mirror failure is distinct from a failure to capture the result.

<a id="R-TOKENS"></a>
Every classification token a host EMITS is a member of `contracts/exit-tokens.json` and maps to the same exit code there;
wrapper-only tokens and compatibility aliases are listed explicitly as exceptions. A membership test replaces the vacuous
`is not None` assert shipped on both hosts.

<a id="R-RECEIPT"></a>
The transport receipt and audit / run-log records carry the common transport object defined by
`contracts/receipt-fields.json`: stdin delivery class, execution route, binary, observed CLI version and attempt.
Existing host envelopes remain. Schema validation alone does not prove host implementation or observed runtime identity.

<a id="R-BIND"></a>
Every leg's result binds `review_id`, `family` and `content_digest` today on both hosts; a mismatch is an INVALID leg, never
a pass. v2 ADDS (round r2, all three families; lands with the D-3 wire — `contracts/leg-verdict-mapping.md`): `leg_name` (the
roster entry), `attempt` (integer ≥ 1, per leg), `route` (the resolved Google route `agy` | `gemini`; null for a family with
one route). The common v2 prompt pins use these fields. Each host adopts its validator, all shaped clauses and collectors together;
explicit legacy entry points retain their old contract and cannot admit v2 results.
Duplicate JSON members are rejected at the original-text boundary before extraction or normalization can discard evidence
(A's wrapper schema path and bare `json.loads` file path retain the previously recorded gap; A's raw-reply admission rejects duplicates. B rejects duplicates at the original-text boundary in its review wrapper/result paths, including explicit v2; see C14/C30).

## Preparation, verification, cleanup (lifecycle obligations)

<a id="R-PREPARE"></a>
`prepare` pins the reviewed basis (commit + content digest), writes the brief, the gated patch and the test patch as separate files (separation is PRESENTATION: relevant tests, policy and prompt text inside the agreed scope stay visible, bound and reviewed; host packet file names are mapped in `units.json`), the history, and the per-round containment artefacts the host uses (A: the agy PreToolUse hook); resolves
the roster from the registry with the recommended defaults; prints one COMPLETE dispatch line per enabled leg; captures the
round snapshot. It refuses on a malformed registry entry and never launches a provider itself. A change to a rule,
schema, prompt clause or policy file is behavioral review scope even when the file contains only text; the docs-never-gate
rule covers narrative documentation only. Symlinks (owner Q4, RULED 2026-09-19: "링크 자체는 검토하되, 대상을 자동으로 따라가지 않는 방식"): the LINK ITSELF is review material — its path, kind and exact link text are fingerprinted and available to reviewers; its TARGET is never followed automatically. Target content enters a review only as an independently authorized, bound input; a link the review cannot follow is disclosed as a coverage gap, never claimed inspected; cleanup never follows a link to delete its target. Each host implements "never followed" its own way and records the evidence (B: link-text fingerprint + symlink refusal in the prepared copy; A: replace its untracked-link refusal with link-text admission and either materialize the text in the round copy or prove no-follow through its read audit) — mechanism = host migration item, principle = shared rule.

<a id="R-VERIFY"></a>
The leader verifies every finding against the reviewed bytes before acting: REAL (reproduced) blocking → minimal fix and full re-review (R-REREVIEW); REAL non-blocking → recorded, fixed at the maintainer's option (any fix is a new basis, R-REREVIEW); refuted by a probe → recorded refutation, source unchanged; design or scope change → R-STOP;
speculative → recorded residual, no code. Reviewer labels are claims, never repair instructions; a vote decides nothing.

<a id="R-CLEANUP"></a>
Cleanup exports and verifies the round's evidence first, then releases only resources the helper can PROVE it allocated or claimed (its own allocation record or marker — never a name shape; an empty directory or a plausible-looking marker can still be foreign); uncertain residue is preserved and reported; it refuses without deleting, states what it observes, and points at the one documented recovery when a tree is not its own. A second cleanup is a no-op. Cap-based pruning of run-log and repair-IPC
files keeps a minimum age floor so a fresh sibling file is never deleted to satisfy a cap (mtime is not only a sort key).

## No cost, CLI only

<a id="R-NOCOST"></a>
Both hosts call vendor CLIs only — no vendor HTTP API, SDK or API key. Login is the user's own OAuth login in each CLI;
wrappers check the binary and never enter or store credentials. Billing follows the AUTHENTICATION type, not the model
flag (Gemini CLI v0.60.0 `contentGenerator.ts`: auth is selected before the model is resolved); environment scrubbing and
the absence of `-m` are hygiene, not proof of the billing route. Default model for the Google review leg on BOTH CLIs: the Pro family with a verifiable HIGH thinking configuration (owner Q-W; owner via the codex session, Q2: "두 CLI 모두 Pro 계열 + 확인 가능한 high로 맞춤; 인증 경계 유지"). agy: today's Pro-high catalog slug, recorded in the roster; gemini CLI: a route-valid Pro model whose default thinking level is HIGH (v0.60.0 `defaultModelConfigs.ts` gives Gemini 3 Pro `ThinkingLevel.HIGH`; the agy slug is NOT a portable gemini CLI argument). Flash was retired as a reviewer (0 unique blocking defects over ten rounds, owner 2026-09-14). Slugs are dispatch-time values in the roster's `agy` / `gemini` block, never constants in code; the configured default is recorded separately from the exposed runtime identity; the model option stays selectable only so a future model can be evaluated. B's explicit legacy development path remains Auto-only. B's opt-in v2 adapter selects route-valid Pro defaults and checks supported controls before inference; preflight settings do not prove runtime identity. A's unpinned gemini invocation remains a migration item. Deterministic
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
