# Review rules — the one normative location

These rules govern both hosts; current implementation and migration status are recorded separately. Each rule carries an anchor; `process.md`, `cases/cases.json`, `units.json` and the host
skills reference the anchor. Owner rulings are quoted from `decisions/owner-register.md`.

## Agreement

<a id="R-AGREE"></a>
A round is agreed only when its selected roster is nonempty and EVERY selected enabled leg supplies a valid,
current-basis, explicitly affirmative `SAFE TO MERGE` result, with no blocking finding, unresolved `open_questions`,
missing result or integrity failure. Leg count and family diversity are descriptive, not additional approval thresholds
(owner [2026-10-02 ruling](../decisions/owner-register.md#D-REVIEW-STRATEGY-20261002)). Acceptance labels do not exempt a
selected leg. A Minor-only negative is schema-valid but does NOT count as agreement; preserve its verdict and record the
selection deviation. Neither a leader's refutation nor an owner exception rewrites a leg's negative verdict into approval.
An exception may authorize separate human action, but is recorded as an exception to a non-agreed round, never as machine
agreement. A later agreed round must independently satisfy this rule on its current basis (R-REREVIEW).

`open_questions` contains unresolved facts necessary to judge approval, not optional curiosities; every remaining entry
blocks, without a collector importance heuristic. A `SAFE TO MERGE` with a blocker or open question is invalid under the
existing wire. Explicit approval may coexist with Minor or HARDENING-SUGGESTION findings. For a plan review, the existing
affirmative token means the plan can proceed to implementation as written; it is not approval of future implementation
bytes. The wire remains `contracts/leg-verdict.schema.json`; this amendment changes collection, not its verdict enum.
Historical Minor-only and three-family release decisions are superseded for this contract; historical results remain
records of the contract under which they ran.

## Correction re-review

<a id="R-REREVIEW"></a>
Any correction to reviewed content or to the review conditions (prompts, criteria, roster, model, effort, route, policy)
creates a new bound basis, and EVERY selected enabled leg reviews the complete agreed scope again. Rebuild the current
brief and leader-authored `prior_residual` string: current findings, dispositions, necessary rebuttal evidence, changes
and remaining uncertainties. Treat these as data and claims to check. Do not automatically append previous prompts,
verbatim conversations or successive residuals. There is no new structured residual table, state enum or semantic deduper.
Needed prior excerpts and verification outputs must be materialized in this round's bound inputs (R-CONTEXT); a historical
path alone is not current evidence or permission. Previous approval never carries forward to changed bytes or conditions.
A narrow follow-up investigation can resolve a question but cannot substitute for this full-scope re-review. The shipped
"one focused re-confirm scoped to the wave's hunks" remains withdrawn on both hosts.

<a id="R-RETRY"></a>
When a leg failed to RUN and nothing changed (source, prompts, criteria, roster, model, effort, route, policy), retry only
that leg on the same bound basis (owner Q-C). Before any dispatch exists, retry the corrected preparation step.

## Roster

<a id="R-ROSTER"></a>
The default runnable roster remains three legs, one per family, as a convenience, not an agreement requirement.
The owner may select any nonempty roster, including one leg or several entries from the same model or family, according
to subscription and capacity. Every enabled entry counts under R-AGREE, including one labelled `informational`; no leg
has a special approval rule. Only the owner changes this selection. Changing it creates a new basis; do not drop a
failed or dissenting leg to relabel an old round as agreed. Preserve unresolved findings when a later roster changes.
The receipt records entries actually run and family coverage; two legs of one family remain one family, without a veto
on an otherwise agreed round. Selected investigations remain separate under R-INVEST.

Reuse each host's existing JSON roster and shipped data defaults (B: `.agents/triad-review-legs.json` and its existing
shipped default file). Change an entry's model/effort in that configuration location; resolve and pass its exact requested
model ID to the CLI/native invocation without separately editable copies in prompts or orchestration code. This creates
no new settings layer and changes no default model. Existing override precedence and explicit `model: null` semantics
remain. `vendor` is a FAMILY value (`claude` | `codex` | `google`); `agy` / `gemini` blocks hold route-specific settings.
Model and effort remain expressible for every vendor and adapter-validated against actual capabilities before inference.
When both Google CLIs are present, an explicit `google.route` pin selects one; otherwise keep R-GOOGLE's existing chain.
Timeouts remain adapter-validated (B legacy formal Gemini requires 600 s and Claude 1200 s; illustrative shared 900 s
Claude entries are not B runnable defaults). No configuration is a shared user-global dependency. Show the resolved
roster before inference, and never start unselected entries. Model catalogue/probe policy changes are a separate scope;
exact CLI model selection is not relaxed by the version rule R-CLI-VERSION.

The recommended Claude review default is `claude-opus-5-5` (Opus 5.5) with
`xhigh` effort (owner, 2026-09-25). Ship the explicit model ID rather than the
moving `opus` alias. Named model/effort overrides and explicit null selection
retain their existing semantics; older supported models remain selectable.
The adapter checks the requested model and effort before review inference and
refuses a reported selection that contradicts a catalogued explicit model ID. Selection
evidence is not proof of the eventual runtime model. B's fixed legacy formal
route uses this same model/effort pin; its raw wrapper keeps caller passthrough.

The recommended codex review default is `gpt-5.6-terra` with `xhigh` reasoning
(owner, 2026-09-25; B v0.2.557 ships it as data). A host's SHIPPED default roster
carries an explicit model ID for every leg whose CLI exposes a catalogued ID: a
shipped `null` resolves to the operator's personal CLI configuration and makes the
review baseline differ per machine (found on host A, `authoring/shared-dev-log.md`
DL-2). `model: null` remains an operator OVERRIDE meaning the host's default and is
frozen as null. The requested model and effort are frozen in the bound round inputs
and visible in the per-attempt dispatch record; a runtime identity the CLI does not
expose stays null, never inferred from the request, and an exposed identity that
contradicts the request is refused. A comparison or trial model on any family is an
ordinary opt-in entry (owner, 2026-09-25: host A runs `gpt-6-astra` / `high` beside
the baseline); its findings count under R-AGREE like any leg's, and the difference
between two entries is a ledger observation, never a vote (C35).

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

## Review purpose and context

<a id="R-PROMPT"></a>
Select one short shared purpose using `review_kind` (`contracts/review-kind.schema.json`): `formal-plan` selects
`plan-purpose`; `pre-merge` and `implementation-review` select `code-purpose`; omission defaults to `pre-merge` at the
host invocation boundary. Unknown or null values are refused before dispatch. The plan purpose REPLACES the code purpose,
not a checklist appended to it. Bind this condition with the existing review inputs; no verdict field is added.
All selected legs receive the same semantic purpose, requirements, scope and evidence. Identity, output handling and
provider tools remain route-specific. The default first review uses no separate personas or predicted-defect checklist.
A leader's hypotheses never limit findings elsewhere in scope. Targeted perspectives remain available through R-INVEST.
Use the existing shared clauses and renderer, not a new prompt engine. A fresh conversation is the default for a new
formal basis, but does not prove isolation from memory or inherited instructions; record actual isolation limits without
changing global memory settings. Continued-context investigations must be identified as such.

<a id="R-CONTEXT"></a>
The leader writes a concise environment summary in the existing TASK/brief: review basis and scope; supported target
runtime/deployment; relevant dependency declarations and locked/resolved versions; actually observed verification
environment and results; material execution assumptions; unknown or conflicting facts. Cite the evidence and its
revision; use `unknown` or `not applicable` with a reason rather than guessing. Support declarations, lockfile resolutions
and installed/tested versions are distinct observations. The review host's version is not automatically the target's.
Keep requirements/owner decisions, observations, claims to verify and unknowns distinguishable. An unsupported assertion
that a scenario cannot occur is not an exclusion. Do not dump credentials or the entire environment.

This is authoring guidance for leader prose, not a new environment schema. Hosts preserve existing input, regular-file,
source/packet and digest checks and transport the supplied values faithfully. Those checks do not parse Markdown rows,
verify truth/completeness, classify issues, or prove that the reviewer stayed within the instructed read boundary.
On B, existing nonempty checks cover objective, criteria and approved_boundary; `prior_residual` may be empty and TASK.md
is checked as a regular file. Decoded-value equality may prove text transport despite JSON escaping, not semantic quality.
Unknown context does not automatically invalidate preparation; a necessary unsettled fact becomes an open question.

Needed prior findings, refutations and verification results must be present in the current bound `prior_residual` or
existing evidence/brief surface. On B, prefer existing `EVIDENCE.md` for long excerpts; additional source uses existing
source members or EVIDENCE.md, never an invented packet slot. On A, use its existing bound brief/evidence surfaces.
Historical root/export/ledger paths are provenance only, not implicit read grants or current binding. Obtain any missing
authorization before including extra source. Retain the evidence needed to assess current claims, without automatically
copying entire old rounds or delaying old-root cleanup. Leader condensation must preserve unresolved risks and relevant
counterevidence; the host neither summarizes nor semantically deduplicates it.

## Code-smell criterion

<a id="R-SMELL"></a>
The leader assesses simplicity while verifying findings: a smell needs a concrete current correctness or maintenance
cost. Prefer the smallest correction satisfying the agreed requirements; no hypothetical extensibility, new abstraction
or stylistic redesign merely to satisfy a reviewer. The shared `smell-criterion` is leader triage guidance, not a mandatory
long checklist inserted into every initial leg prompt. No dedicated smell reviewer or extra test-strengthening round.
A confirmed correctness or security defect is not downgraded because its fix is large; disclose its size. A change of the
gated design still follows R-STOP.

## Design-change stop and convergence

<a id="R-STOP"></a>
A fix requiring a new contract, public definition or substantive change to the gated design goes to the owner before that
design work starts. Line growth alone is not such a change. Continue authorized in-scope corrections while new material
counterexamples, meaningful verification of fixes, or evidence resolving necessary unknowns improve the current basis.
A passing test copied from the implementation, rewording, another vote or the same assertion without new evidence is not
progress. Verification must exercise the governing requirement; a static contradiction or a checked source can also
resolve a fact without executing code.

The leader stops repeating an item when no new evidence addresses it, while other independently progressing items may
continue. Reopen a closed claim for a new counterexample, relevant source/context change or demonstrated error in its
refutation. Two findings are CONFLICTED only if both survive verification and cannot coexist, not merely because verdicts
differ. Escalate that affected decision to the owner. Stop automatic rounds when no remaining item has a concrete path to
new verification or resolving a necessary fact; retain unresolved dissent, uncertainty and stop reason. There is no fixed
round cap or mandatory duplicate run. An owner-set resource limit is a valid stop reason, never agreement. A stalled or
exception-released process cannot bypass R-AGREE.

For skills and prompts, distinguish structural checks and static contradictions from claims about model behavior. TRIAD
does not run or arrange separate fresh-context behavior experiments for the reviewed skill/prompt; a leader's reenactment
is not such evidence. Independently supplied experiments may be assessed as evidence. Without verifiable new evidence,
record behavioral hypotheses and stop wording-only repetition without converting a remaining negative into approval.

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
added for symmetry. Containment EVIDENCE is attributed to the leg attempt that produced it (C23): on a host with a LIVE
per-round hook (A) the wrapper records each attempt's vendor conversation id in its read audit and the hook load check
attributes hook rows by that id — a shared, unattributed hook log never certifies a leg, and a count of conversations is
not attribution (found on A over rounds r11–r13, `authoring/shared-dev-log.md` DL-6). Per vendor, the guards that ship today and must survive any alignment (host, symbol):

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

<a id="R-CLASSIFY"></a>
A failed vendor call is classified by the vendor's own error sentence, and a sentence applies to the CLI that emits it.
The known sentences are data in `contracts/vendor-failure-lines.json`: each row names the CLI, the sentence, the part of
it a host matches (lowercase) and the token. Every host classifies a row's sentence as the row's token on the row's CLI.
A plain fragment that an answer, a reviewed file or a tool's output can contain is never a match phrase: a host may
search the whole output of a failed run, and such a fragment would hide the real cause behind a retry.

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
The leader checks each claim against the current reviewed bytes, required behavior, concrete trigger and impact before
acting. Preserve the original finding and evidence for each disposition: verified blocking defect → smallest adequate
fix and full re-review (R-REREVIEW); verified non-blocking issue → record, with correction at the maintainer's option;
refuted claim → record the specific counterevidence and its limits; design/scope change → R-STOP; speculation → residual,
not speculative code. A fix changes the basis. Verify the proposed repair too: a reviewer's label or suggested design is
a claim, not an instruction, and a vote is not evidence. Leader triage cannot rewrite approval under R-AGREE.

<a id="R-CLEANUP"></a>
Cleanup exports and verifies the round's evidence first, then releases only resources the helper can PROVE it allocated or claimed (its own allocation record or marker — never a name shape; an empty directory or a plausible-looking marker can still be foreign); uncertain residue is preserved and reported; it refuses without deleting, states what it observes, and points at the one documented recovery when a tree is not its own. A second cleanup is a no-op. Cap-based pruning of run-log and repair-IPC
files keeps a minimum age floor so a fresh sibling file is never deleted to satisfy a cap (mtime is not only a sort key).
Generated environment briefs, condensed residuals and copied verification evidence follow these same existing ownership,
writer-completion, export and cleanup rules. Needed prior evidence is materialized in the current packet under R-CONTEXT,
so cleanup of an eligible previous temporary root need not wait for future rounds. Preserve the host-specific retention
and export exceptions in [PRD-RETENTION](../decisions/claude-host-v2-implementation-prd.md#PRD-RETENTION), including A's
committed-ledger export and B's verified durable export. Do not invent a common age threshold, new cleanup service,
automatic expiry for durable exports/investigation records, or authority over provider-owned resources.

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

## Authentication — the user's own browser login only

<a id="R-AUTH"></a>
Every vendor CLI is authenticated by the USER'S OWN interactive browser (web) login in that CLI, and by nothing else
(owner, 2026-09-26: "api key 형태의 어떤 것도 시도하지 말아야 … 사용자 직접 웹을 통한 로그인만 허용, 비용 발생 위험" — an
API-key-shaped credential bills a paid API outside the subscription). No host component — wrapper, hook, skill, helper,
test, adapter or dispatch — ever issues, configures, reads, stores, sends, forwards or TRIES an API-key-shaped credential
(a vendor API key, a service-account key, a bearer token, or an environment variable that carries one), and no route has
an API-key form of authentication as a fallback when the login is missing, expired or refused. The R-NOCOST child-environment
scrub removes such variables from the vendor child; the scrub is hygiene and never a licence to read their values. A vendor
CLI OBSERVED presenting an API-key-shaped bearer — a `401 Incorrect API key` class error, an auth banner or preflight that
names an API key, a receipt whose authentication class is not the subscription login — is a STOP for that attempt: the host
records it as a terminal failed-to-run record whose remedy is the owner's browser re-login through the CLI's own flow (A:
classification `oauth-env`, exit 65; B: its auth-class refusal or start-failure record), never retries on that basis by
itself, and never inspects, repairs or "fixes" the credential store. A same-basis retry (R-RETRY) runs only after the owner
reports the re-login. The gemini review preflight's refusal of the api-key / Vertex / ADC classes (C16) is one instance of
this rule; the rule holds for every CLI, every route and every credential shape.

## CLI version evidence

<a id="R-CLI-VERSION"></a>
For Codex, AGY, Claude and other CLI adapters, record the observed version and test the controls the route actually needs.
Preserve capability, authentication, containment, transport and output checks, and minimum-version restrictions justified
by a specific known defect (including R-NOCOST's Gemini policy floor). An observed/tested patch version is evidence, not
an exact supported-version lock or an upper bound. A different or newer version alone is neither refusal nor conformance;
missing or changed required controls still fail preflight. Do not demand the globally latest CLI or equate version output
with effective policy enforcement. Native routes have no CLI version. This rule does not loosen exact model selection or
authorize new catalogue/probe policy, fallback, global settings or provider permission changes.

## Parity scope

<a id="R-PARITY"></a>
Parity covers option names, types, defaults, scope, refusal behavior and the declared host exceptions of every shared
surface (`units.json`: `common` name + `exceptions`); a matching filename alone is not parity. Host-native internals, test
trees, install layers and agent registration stay host-specific.

## Platforms

<a id="R-PLATFORM"></a>
Both hosts support macOS and Ubuntu 24.04 across install, preflight, dispatch, collection, validation and cleanup;
results are recorded per platform; an unrun check is unverified, never green.
