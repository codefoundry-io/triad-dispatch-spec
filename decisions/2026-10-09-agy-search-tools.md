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
global activation required separate approval, subsequently received below. B uses separate review/research profiles to
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

B implementation verification (2026-10-09): two B-owned profiles, explicit setup,
name/path/hash preflight binding, checks before/after dispatch, no raw/native-leg
change. Dedicated source RED reproduced missing checks. Independent code review's
Unicode-path defect was reproduced and fixed. Dedicated final GREEN: C72 12 tests;
full suite 1915 passed/4 skipped, both skill validators passed; 55 measured source
hashes stable. A leader-authored installation approval record was added during
the run, so whole Git status equality is explicitly false. The separately
approved installation and actual native-search result are recorded below;
fresh formal review remains pending, with no admission claim.

### B installed-profile capability proof, 2026-10-09

The owner explicitly approved the exact two global files and one bounded probe.
Canonical setup installed both B profiles without replacement, verified source
hash equality, and preserved A's two profile hashes. One AGY 1.3.2 Pro/high call
through the canonical formal-v2 wrapper used real global profile lookup,
preflight binding and existing read-only/plan/environment guards, with no web or
autoapproval. `init.agent` selected `triad-codex-readonly-review`; a successful
`grep_search` found `receipt.txt:TRIAD_DISCOVERY_PROBE=cedar-4827`, followed by a
successful `view_file` read. Vendor and wrapper exited 0 after 31.4 seconds.

The first finish call used schema_version 1 and failed validation; the provider
corrected it to 2 in the same invocation. No wrapper retry or schema relaxation
occurred. This demonstrates Pro/no-web native search/read and final v2 acceptance
on that fixture, not every schema/model/web combination or product approval.
Evidence under B workspace `_runs/infra/20261009-spec-to-code/agy-profile-capability/`:
`run.py`, `summary.json`, `observed-tools.json`, `result.json` and incident capture.
Install evidence: B `_runs/spec-plan-20261009/agy-profile/installed.json`.

Separate Gemini CLI has a different tool path: official
[v0.63.0 core configuration](https://github.com/google-gemini/gemini-cli/blob/v0.63.0/packages/core/src/config/config.ts#L3756-L3817)
registers native directory/file/grep-or-ripgrep/glob tools by default unless
configured otherwise. B's packaged Gemini policy permits those tools; it does
not select the AGY profile. B's installed Gemini is still 0.60.0, below the owner
floor 0.63.0, so no supported-version live Gemini search is claimed. No global
upgrade or new common restriction follows from this source observation.

### Reply received 2026-10-09

[A's PR13 reply](https://github.com/codefoundry-io/triad-dispatch-spec/pull/13#issuecomment-6075351927)
confirms that its existing 1.3.2 run selected triad-readonly-review in init.agent;
the installed definition hash was
2ad19927912947c1d4ad46230b228c7585a3dc73758115d3fc8fe549ac0829de.
The same init.tools listed 60 names including off-profile tools. This event is
not an effective tool allowlist or proof of executable off-profile capabilities.
The run requested only OK and made no tool call. A has no retained current-version
successful native search capture; its older captures are unavailable. This reply
supports lookup/selection, not search recovery or containment by profile alone.
B therefore retains its existing containment and requires its own actual-search
control after separately authorized setup. No extra A probe is requested now.
A also agrees with C70/C71 and U1a's exposed-identity-only interpretation; no
native-leg change is called for. This is attributed A evidence, not B execution.

Confirm current AGY 1.3.2 custom-agent tool exposure and definition lookup with
existing evidence if available: command, agent source hash, successful native
search event and limits. Your source already uses an explicit profile; do not
change your native leg or copy B's plan-mode implementation. Review the shared
implications of this owner-approved correction at this same spec commit. B is
the implementation lead for this correction; no A code change is requested.
