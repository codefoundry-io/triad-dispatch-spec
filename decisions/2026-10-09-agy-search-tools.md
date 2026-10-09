# AGY default search-tool removal: B capability gap

Owner-approved B correction; draft common clarification, not revision adoption.

## Evidence

B U1b R2 (`triad-opus-default-20261009-r2`) returned Claude/Flash/Codex SAFE
and Pro NOT-SAFE with a missing native search-tool coverage question. All
producers exited successfully and ROUND_INTEGRITY_OK matched. The round is
NOT_APPROVED, retained and cleaned; no partial approvals carry forward.

A bounded Pro/high diagnostic on AGY 1.3.2 used B's canonical wrapper in
plan/read-only mode, forcing the existing formal deny set and environment
scrub on the raw custom-schema call, with no autoapproval or web. It reported
no native content-search tool. A view_file control read the actual fixture
marker; captured events contain that read and no search. This report alone
is not a complete tool inventory or proof of every route's capabilities.

Independent primary evidence: the installed CLI's `agy changelog`, version
1.2.7 entry, explicitly retires find_by_name, grep_search and list_dir from
the default agent/subagent baseline while retaining them for custom agents
whose tools list names them. The complete changelog and diagnostic events are
preserved in B's owner workspace under
`_runs/infra/20261009-spec-to-code/agy-tool-discovery-probe/`.
No persistent permission/global-agent change was made.

B still uses the default AGY profile; `bin/review_round.py:68-80` names these
search tools, while `bin/antigravity_wrapper.py:_build_cmd` supplies no agent.
The version/control preflight does not establish runtime tool availability.
This is distinct from the corrected file-list/log-audit defect in
[C70/C71's diagnosis](2026-10-09-review-read-boundary.md).

A was read-only inspected at clean `9e16880dc05e89b15669d42e9f62204d05349c7d`.
`3rd-Agent/wrappers/antigravity_wrapper.py:276-283,322-359` already supplies an
explicit tools profile (mainAgent true, subagent false, model inherit), and
`.claude/skills/triad-cross-family-review/references/leg-contracts.md:358-377`
describes setup-once agent dispatch with a read grant. No live A dispatch ran;
this is source evidence only, not the same demonstrated A defect.

## Proposed B correction and decision

Ship a B-owned AGY main-agent profile with native read/search/finish tools,
check and bind its definition before dispatch, and retain the existing B
plan-mode/sandbox, environment scrub, permission denies and verdict/integrity
controls. Model and effort remain direct CLI parameters. This does not add
an external Claude agent or change either native leg. Final lookup and install
ownership require validation; do not overwrite or silently depend on A's profile.
The owner was asked before this provider execution/install design change.
The owner approved option 1 and continuation on 2026-10-09. The option was
described as AGY-specific read/search profile, definition validation/binding and
setup design/implementation, with global installation separately approved after
the exact path/delta is reviewable. Verbatim answer: "1번이긴 한데 그럼 이전에는
어떻게 검증한거야? 이전까지도 잘 됐잖아". This authorizes B implementation;
global activation remains pending. B uses separate review/research profiles to
preserve existing authorized-web behavior, confined to legacy/v2 formal calls.
Name/path/definition SHA-256 enter the existing preflight receipt and its bound
digest; missing/drifted definitions fail before inference. No new model preset,
routine leader read-log audit or native-leg change is introduced. C72 records
normal/missing/drift/web cases before implementation.

Prior B Pro preflights for Google pins R4, Claude selection R2 and Opus default
R1/R2 all report AGY 1.3.2 and provider_started:false. Earlier success therefore
did not prove native search availability; this was not a new intervening upgrade.

Next proof: a real search and read control under the selected profile, focused
regressions and a fresh complete review. A leader file inventory or majority of
SAFE results cannot substitute for independent discovery.

## Request to Claude maintainer

Confirm current AGY 1.3.2 custom-agent tool exposure and definition lookup with
existing evidence if available: command, agent source hash, successful native
search event and limits. Your source already uses an explicit profile; do not
change your native leg or copy B's plan-mode implementation. Review the shared
implications of this owner-approved correction at this same spec commit. B is
the implementation lead for this correction; no A code change is requested.
