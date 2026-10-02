# Owner decisions — rulings and their effect (public, site-neutral)


<a id="D-REVIEW-STRATEGY-20261002"></a>
## Review strategy — owner direction, 2026-10-02

Verbatim excerpts from the current Codex conversation (the original Korean is preserved):

> 내 의견을 주자면 leg의 만장일치가 통과 기준이지 leg가 몇개인지 같은 모델 계열인지는 안 중요한 것 같아. 구독 요금이나 한도에 따라서 매번 조절 가능한게 맞는 것 같아.

> 프롬프트에 대한 지침은 니가 테스트할수 없어. 너는 이 직전의  결정과 지침 컨텍스트에 영향을 받고 니가 스킬이나 프롬프트를 재현하려면 ㄹresy eye에서 스킬을 테스트하거나 해야하는데 그건 triad 스킬의 범위를 벗어난 거야.

> 기존 리뷰 프롬프트에서 환경이나 라이브러리버전 이런 부분이 제대로 전달되지 않아서 리뷰어가 잘못판단하지 않을까 하는 우려가 있는데
> 기계적으로 복사하듯이 넣어야 하는 부분과 메인에이전트가 그때그때 판단에 따라 넣어줘야하는 부분들이 이전처럼 잘 나뉘어져 있으면 좋겠어.

> 이제 스펙을  PR을 업데이트하고 구현에 들어갈 검토를 시작하자 제시안 부터 줘 md로 줘 굳이 html로 만들지 말고

> 이후에 큰 이견 없으면 스펙 업데이트하고 업데이트 전에 정리사항 다시 md로 공유해줘

> 그리고 모델의 업데이트가 잦으니 모델명 설정을 쉽게하고 codex, agy, claude 버전을 너무 엄격하게 보지마
> 생성 파일에 대한 클린업을 다른 스펙 참고해서 제대로 관리하도록 우지 할 것

> claude 쪽 코드는 보지마 아직 스펙적용안했어

> Cli 로출하려먄 어쩔수 없이 모델을 정확히 적어야해. 그부분은 냅두고..json에 한군데맘 수정하게 설정으로 뽑으라고 이미되어있을건데

Effects: [R-AGREE](../reference/review-rules.md#R-AGREE), R-ROSTER, R-PROMPT, R-CONTEXT, R-REREVIEW,
R-VERIFY, R-SMELL, R-STOP, R-CLI-VERSION and R-CLEANUP. Historical Q-S/Q1 Minor-only negative release and
D-4/Q-L minimum-family/count release requirements are superseded; Q-B/Q-H/Q-Q's no-blocker test remains necessary
but is not sufficient without each selected leg's explicit approval. Historical outcomes are not rewritten.
The 2026-09-20 per-change A-source inspection directive is suspended for this amendment: use shared specs and
research documents, do not inspect A implementation code, and do not claim current A conformance.
Same-commit shared-spec review remains possible and is separate from A code inspection.

Leader implementation choices, not verbatim owner rulings: reuse existing prose TASK/brief and `prior_residual`, reuse
legacy stage names, materialize needed prior evidence in existing current packet slots, retain wire tokens, and prepare
a separate review-strategy draft PR with explicit overlap against model-policy PR #6. No new model settings framework,
model default change or model-catalogue policy is authorized by this amendment. Exact IDs remain JSON data consumed by
CLI/native dispatch. The MD change summary was shared before spec mutation after Astra/xhigh and Opus 5.5/xhigh
scoped direction review closed two material objections. See [the evidence and adoption record](2026-10-02-review-strategy.md).
This task authorizes the requested spec/PR work, not host implementation, merge, tags, installation or global settings.

## Historical owner decisions

2026-09-21 follow-up: owner requested “Claude 웹 수정하고 원격 spec에도 기입해” and clarified
“리뷰시도 웹감증 허용했는데 직접적으료 요청할때만”. The owner then clarified “다른 leg 마찬가지야. 리뷰시 신규기슐은 web검색없으면 없는 Api기능이라고 리뷰한다” and
“그렇게까지 프롬프트를 늘리지마 내가 직접 요청할께 신기술 판단은 리더도못해”. Apply the direct-request condition
to all legs with short permission wording, without technology-detection rules. This conditionally supersedes D-9's absolute
REVIEW prohibition: direct owner request for the current round only. The normative rule is
[R-REVIEW-WEB](../reference/review-rules.md#R-REVIEW-WEB); implementation and host boundaries are in
[the amendment and handoff](2026-09-21-owner-requested-claude-web.md). This authorizes the requested
branch amendment, not a revision tag, final merge, global permission change or host A implementation.

This repository is public. Each row records WHAT the owner decided and WHERE it lands here; the owner's exact words
(Korean, verbatim) are kept in the claude host's working record (`triad` plan `2026-09-19-triad-host-parity-plan.md § 8b`)
and in codex's consolidated document for the directions given in codex's session. Where the owner selected an option the
leader had written, the row says "selected option"; the choice is the owner's, the label the leader's. Nothing here is a
new rule; every row points at the normative location.

| ID | Decision | Effect here |
|---|---|---|
| Directive (2026-09-19, current-source and cross-host coordination) | Both leaders read latest remote main; share every common design/contract/prompt/behavior change before implementation; diagnose any omitted existing functionality with three families, however small. Codex drafts the shared protocol; Claude reviews the same commit. Each leader owns only its host | `reference/spec-authoring.md#R-AUTHORING-SYNC`; this new authoring draft awaits Claude review, without carrying forward the old basis acknowledgement |
| Directive (2026-09-20, Codex first) | "니가 먼저 진행하고 같은 문제가 있는지 항상 claude host 쪽 코드를 보고 지적 업데이트해 라인으로 지적하고 codex업데이트가 끝날때 까지 claude 쪽은 업데이트 안할거야" | Lead-host sequencing in `reference/spec-authoring.md#R-AUTHORING-SYNC`; B leads implementation and verification, inspects A at each change, and accumulates commit/file/line evidence and final A instructions. No A edits by Codex |
| D-3 | Verdict wire contract: adjudicate via ONE three-family round, each host keeps its own schema until then | `contracts/leg-verdict.schema.json` NOT YET; `R-AGREE` last sentence |
| D-4 / Q-L | Three-family review is the default; substitutes are contingency; the model behind each slot is replaceable; at least three legs run | `R-ROSTER` |
| D-9 | Network tools in the gemini review policy: same three-family round, date-anchored web evidence only | `contracts/README.md` (policy row) |
| D-10 | Reviewer framing: CLOSED by owner Q3 (codex session) — evidence-centred, a no-defect conclusion allowed | `prompts/common-clauses.md § adversarial-framing` |
| D-13 | Host A `fixture.sh` contract: header wins (leak prune + 14-day retention), A-side only | none here |
| D-14 / Q4 | RULED 2026-09-19: "링크 자체는 검토하되, 대상을 자동으로 따라가지 않는 방식" — the link itself is reviewed (text fingerprinted, visible); the target is never followed automatically; mechanism per host | `R-PREPARE`, C26 |
| Q-A | The host where gemini is in service can download from GitHub but not upload | `README.md § How a host uses a revision` (owner pushes; results come back by briefing) |
| Q-B / Q-H / Q-Q | Agreement = no unresolved BLOCKING finding from any leg; tiers are data | `R-AGREE`, `R-ROSTER` |
| Q-C | A leg that failed to RUN with nothing changed is retried alone | `R-RETRY` |
| Q-D | A selected investigation returns a free-form report, never a review verdict | `R-ROSTER` last sentences |
| Q-E / Q-M | No "degraded" label ceremony; no per-leg special rules; a leg has a recommended default model, changeable anytime; the count is variable | `R-ROSTER` |
| Q-F / Q-K | No development before the design spec is agreed; approved defect fixes on host A continue | `README.md` (rev-0 is a draft, not implementation authorization) |
| Q-G / Q-J / Q-N | agy and gemini are distinct CLIs of one family with opposite availability at the two sites; keep each host's SHIPPED fallback logic; the owner tests gemini where it is in service and briefs the leader | `R-GOOGLE` |
| Q-O | `acceptance` is a data field only; every rule derived from it is cut | `R-ROSTER`, `contracts/review-legs.example.json` |
| Q-P | The shared package lives in this SEPARATE repository; enforcement mode is the leaders' call (recommendation: informational drift report first) | `README.md § How a host uses a revision` step 3 |
| Q-S | selected option: a MERGE WITH FIXES with only Minor findings counts as agreement, no extra round | `R-AGREE` |
| Q-T | selected option: leaders hand files, the owner pushes | `README.md` step 1 and 4, `AGENTS.md`/`CLAUDE.md` |
| Q-U | selected option: prompts live here as the one editable copy; hosts vendor at the adopted revision | `prompts/`, `README.md` step 2 |
| Q-V | Concept only, no UI, no LikeC4; this repository is a lightweight experiment lab | `README.md` purpose, `reference/spec-authoring.md § 7` |
| Q1 (codex session) | selected option: "코드를 수정하면 전원 재검토. Minor만 남은 원본은 승인 가능" — Minor-only findings do not block the unchanged reviewed bytes; any change to reviewed content = full participating-roster re-review | `R-AGREE`, `R-REREVIEW` |
| Q2 (codex session) | selected option: "두 CLI 모두 Pro 계열 + 확인 가능한 high로 맞춤; 인증 경계 유지" — Pro family + verifiable HIGH on both Google CLIs; B's Auto-only path and A's unpinned gemini call = migration items | `R-NOCOST`, roster example, C18 |
| Q3 (codex session) | selected option: "증거 중심으로 통일하고 무결함 결론도 허용" — shared review prompt is evidence-centred and allows a no-defect conclusion; D-10 closed | `prompts/common-clauses.md § adversarial-framing` |
| Q-W | Google review leg default model = the 3.1 Pro-high tier; Flash retired as a reviewer; the model option stays only so a future model can be evaluated (corrects the leader's "provider default / auto" reading) | `R-NOCOST`, `contracts/review-legs.example.json`, C18 |

| D-3 (round r2) | Three families converged on a superset v2 wire (`contracts/leg-verdict-mapping.md`); residual choices are leader-level | `R-AGREE` open-question axis, `R-BIND` v2 additions |
| D-9 (round r2) | CONFLICTED: codex and google recommend ALLOW web tools in review legs with a date + version anchor; claude recommends DENY by explicit rows (and found A's policy INHERITS a search allow today). Owner decision requested | `contracts/gemini-readonly.toml` header, `contracts/README.md` |
| Q4 (round r2) | Split 2:1 (materialize in the round copy vs fingerprint + no-follow clause) → owner ruled the PRINCIPLE (review the link itself, never follow the target automatically); the mechanism is each host's migration item | `R-PREPARE`, C26 |

| Directive (2026-09-19) | The recurring relative `--prompt-file` dispatch failure must be solved mechanically, not by instructions: resolve against the caller's cwd or align the path with cwd; record the problem in the plan and specify the fix | `R-CONTAIN` (all wrappers), C28; host plan P4-22 |
| Directive (2026-09-19, web evidence) | The agy web search that had been working degraded in round r2: fix it and test it; deliver the spike record — lines and cause — to the other leader too, so both hosts fix the same seam | `R-INVEST` web-evidence sentence; `prompts/investigation.md` (`web-evidence`); C29; `spikes/2026-09-19-google-web-evidence.md`; host plan P4-23 |
| D-9 RULED (2026-09-19) | Review legs have no web tools: DENY `google_web_search` / `web_fetch` by explicit rows in the shared gemini read-only policy; investigations (R-INVEST) keep web with the `web-evidence` clause. The rule is per OPERATION, not per CLI: codex `web_search` disabled, agy review agents without web tools (B's read-only builder drops `read_url` for review dispatch only), gemini deny rows, every review prompt renderer stops permitting web (codex F2). Applied first; the runtime effect is verified where gemini is in service (owner: apply now, leave the untested part as a separate config-like record) | `contracts/gemini-readonly.toml` (rows at 200), `contracts/gemini-readonly.verify.toml` (V1-V5, NOT RUN), C15, `R-GOOGLE` convention sentence, `R-CONTAIN` gemini bullet; host A applied (t50); B: codex removes the two tools from its 999 allow list |
| Codex rev-1 addendum review (2026-09-19) | Findings F1–F8 accepted and applied by the claude leader — status accuracy (C28 NOT applied on either host), D-9 as an operation-level rule, executable V3/V5 with an isolated control and an evidence rule, C28 wording, Google shape pin in the v2 migration list, byte-identical vendoring of the policy (one definition), C4 original-vs-owned-copy split; leader-level wire choices aligned (`path`, three canonical verdicts, optional `correction`, uncertainty-only negative = DO NOT MERGE + `open_questions`, `SAFE`/`Major` import aliases only) | `R-CONTAIN`, `contracts/gemini-readonly{,.verify}.toml`, C4/C15/C28/C29, `contracts/leg-verdict-mapping.md`, `prompts/leg-google.md`, `units.json`, `spikes/2026-09-19-google-web-evidence.md` |
| Directive (2026-09-19, one place) | A large host restructuring is coming: rulings and conventions are written ONCE, in this shared repository; host documents carry pointers, never a second narration ("do not make the work happen three times") | `reference/spec-authoring.md § 3/§ 4`, `R-GOOGLE` convention; host plans quote verbatim only |
| Directive (2026-09-25, codex baseline and comparison; shared development log) | Codex review BASELINE = `gpt-5.6-terra` / `xhigh` as shipped roster DATA on both hosts (a shipped `null` had left host A's baseline to the operator's personal CLI configuration). Host A additionally runs a COMPARISON entry `codex-astra` = `gpt-6-astra` / `high` in its next round; both entries count, and the terra/astra difference is a ledger observation, never a vote or a policy. The Claude review leg is `claude-opus-5-5` / `xhigh` (the 2026-09-25 default-model handoff). PRD and spec move together; what the other host must fix is written into a shared development log, not a session note | `R-ROSTER` codex paragraph, C35, `contracts/review-legs.example.json`; `authoring/shared-dev-log.md` (`R-DEV-LOG`) |
| Codex verification amendment (2026-09-19; technical disposition) | Earlier F3/F4 verification changes required further corrections A1–A4; the owner authorized Codex to publish the bounded shared-spec amendment. Runtime checks remain NOT RUN, shipped policy bytes unchanged, and Claude acknowledgement on the amended basis is pending | `decisions/rev-1-codex-verification-amendment.md`; procedure only in `contracts/gemini-readonly.verify.toml`, C15, `R-GOOGLE` |

Withdrawn at the owner's word: a usage-measurement item (2026-09-19) is not recorded anywhere.

<a id="d-four-leg-20260921"></a>
## D-FOUR-LEG-20260921: one Codex and three Google reviewers

The owner requested one Codex subagent and three independently invoked Google
legs with different review emphases, with final review approval decided by the
owner. This specializes existing R-ROSTER/R-AGREE; it does not add an automatic
lens field, a majority vote or a new approval token. Four legs cover two families.
The precise request, source evidence and publication boundary are in
[the operating agreement](2026-09-21-codex-google-four-leg-agreement.md), with
[setup and verification](codex-google-four-leg-operating-spec.md) and case C33.
Publication is owner-requested; Claude acknowledgement and exact live-profile
verification remain pending. A's native topology remains distinct from B's.

<a id="gemini-invocation-20260921"></a>
## Gemini invocation briefing: 2026-09-21

The owner reported that Gemini CLI invocation succeeded in the reported
environment. This is the R-GOOGLE service briefing, also reflected in the
[B v0.2.556 release](https://github.com/codefoundry-io/triad-codex-dispatch/releases/tag/v0.2.556).
The report did not supply an exact installed revision, CLI version, authentication
class or transcript. It confirms the reported invocation only; it does not mark
B1-B3, WEB-B-1, three concurrent Google calls, lens coverage or host A adoption
as passed. Preserve those separate verification statuses.

<a id="d-auth-browser-login-20260926"></a>
## D-AUTH-BROWSER-LOGIN-20260926: CLI authentication is the user's own browser login only

Owner, 2026-09-26, ruling on the host A round r18 incident (a codex CLI that
presented an API-key-shaped bearer, `401 Incorrect API key`, on a subscription
login): "api key 형태의 어떤 것도 시도하지 말아야하는데 스펙이나 이런 사양이 있으면
금지시키도록 명시해 사용자 직접 웹을 통한 로그인만 허용 비용 발생 위험" — nothing
API-key-shaped is ever tried; the spec states the ban; only the user's own direct
browser (web) login of a CLI is allowed; the reason is billing risk. Recorded as
rule R-AUTH (`reference/review-rules.md#R-AUTH`), case C37 and dev-log row
DL-16. It sharpens R-NOCOST (CLI only, the user's own login); it adds no
credential handling of any kind to either host — an observed API-key-shaped
authentication is a STOP whose only remedy is the owner's browser re-login.

<a id="d-rulings-20260927"></a>
## D-RULINGS-20260927: operations equivalence, native legs, retention, identity

Owner rulings of 2026-09-27 on the leader's issue list, recorded once here and
carried by the dev-log rows named: item 8 → DL-17 (A's refuse-before-write plus
the committed ledger equals the start-failure record, preparation custody and
export); item 9 → DL-18 ("네이티브 서브에이전트 스폰 … 자체 진단 기능이 있어서 별도
디버그용 감사가 필요 없음 이전 리뷰 히스토리 정도만 필요" — a native same-family
sub-agent leg keeps only its review history); item 16 → DL-19 (the 2026-09-17
retention ruling upheld; item 6 of 2026-09-26 adds "모든 로그와 워크트리 생성이
기간이 지나면 clean up 되어서 용량이 무제한 늘어나는 일이 없어야함"); item 14 →
"일단 지금 체제로": the leader keeps pushing as the owner account for now, every
push and merge under the owner's explicit approval; item 18 → the deploy push of
the directives-only distribution approved.

<a id="d-rulings-20260928b"></a>
## D-RULINGS-20260928B: a fact is written in its present form

Owner, 2026-09-28, on how a vendor failure sentence enters this specification:
"스펙에 이력이 즁요할까? 지금 형태만 나타내면 딻은 인터페이스와 prd규약에 에러로
들어가야할 것같은데" — is history important in the spec; stated as it is now, it
belongs in a short interface and as an error in the rules. On publishing it:
"스펙에도 올려 목적자체가 같은코드와 같은 프롬프트를 가지려는거니까" — publish it
to the spec; the purpose is that the hosts have the same code and the same
prompts. Recorded as rule R-CLASSIFY (`reference/review-rules.md#R-CLASSIFY`),
contract `contracts/vendor-failure-lines.json` and case C43, with no
development-log row. The owner also confirmed the narrow codex match phrase
`selected model is at capacity` in place of the wide `is at capacity`. This
decides this item only; whether other parts of the specification are rewritten
the same way is a later decision of the owner.

