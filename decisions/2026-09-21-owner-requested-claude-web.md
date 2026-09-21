# Owner-requested Claude web verification — candidate and host handoff

Status: owner-authorized amendment; B implementation/verification in progress. No revision tag or host adoption.
The owner request and its exact clarification are in the owner register; the normative rule is
[R-REVIEW-WEB](../reference/review-rules.md#R-REVIEW-WEB). Research methodology work remains a proposal.

## Evidence and change

Shared pre-change basis: `140dda4ce66dfb5b34ba86d7e4c1356dafd026a0`.
Remote main fetched before authoring: `2eb883fee59e66556ee7c7f87189b38231136622`; no main-only changes.
B pre-change source: `add5805d8dec70f5e133164c49bc0fe3bff75095`.

B `bin/claude_wrapper.py:391` builds fixed native argv without web preapproval; `:226` exposes no `--web`.
An authorized research call returned exit zero but four native permission denials and no fetched pages.
The prompt's authorization could not grant native tool permission. A task-scoped native probe using
`--allowedTools WebSearch WebFetch` succeeded with no denials; the shared wrapper was still unchanged.
Official references: [Claude permissions](https://code.claude.com/docs/en/permissions),
[CLI reference](https://code.claude.com/docs/en/cli-reference); local CLI help confirmed the native flag.
This is an adapter authorization omission, not a confirmed vendor defect or a reason to loosen global policy.

The owner extended the correction to every leg, then requested minimal prompt wording and no leader judgment
about new technology. B adds fixed Claude `--web`, legacy `--web-authorized`, and transient v2
`review_web_authorized`. Google preflight and wrappers bind the same option; native Codex receives the same
short common permission clause. Gemini selects the complete web-enabled B profile while default bytes stay.
Raw Claude forwards the caller prompt unchanged. Existing raw Google evidence procedure remains unchanged.
Cases C31/C32 bind this behavior. Production implementation, dedicated RED/GREEN and formal review remain pending.

## Host A review request for this commit

Claude maintainer: review this exact amendment commit, including rules, Claude clause and C31/C32, before adopting.
Acknowledgement is PENDING; no previous agreement is carried forward. Under the owner-designated B-first sequence,
B proceeds on the owner's settled scope and records its result for your later implementation. Do not infer adoption
from this shared branch publication or copy B CLI controls into A's native agent route.

Current A read-only source inspected at `55e0c677da8a6b0011013cfcc96aa04ed4f01b55`:

- `.claude/skills/triad-cross-family-review/lib/review_scratch.py:2841` renders the native Claude review prompt
  with no transient web condition. Add the condition to the shared review basis and every family rendering;
  select the common web clause in every participating leg only when that current request is true.
- `.claude/agents/triad-reviewer.md:6` exposes `Read, Grep, Glob`; web tools are absent.
  `.claude/agents/triad-researcher.md:6` exposes web, but selecting that investigation agent is not review parity.
  Preserve the native review path and raw-reply admission; implement a scoped review capability only when you adopt.
- `review_scratch.py:3525` explicitly forbids Codex `--search` for REVIEW. At A adoption, select its native search control only under the same bound current permission. Preserve A's live AGY hook/load/read-audit and existing auth controls.

No A edits were made. Existing unrelated A files were preserved. Default Google policies and their unrun verification manifests are unchanged. A requested unsupported web verification remains an explicit evidence gap until supported.

## Verification boundary

Before B implementation: root-authored tests and a fresh dedicated source-skill RED executor.
After: fresh dedicated GREEN, full regression suite, source skill validator, applicable lifecycle checks, bounded
real wrapper web probe and the workspace's complete formal multi-family review. Shared schema tests and anchor/
case/unit checks verify document structure only. Record unrun host/service checks as NOT RUN; do not turn search
summaries, prose URLs, successful exit, or prefix-only fetched bodies into complete evidence.

Known AGY delivered-body limitation remains independently documented as KI-AGY-URL-BODY-PREFIX; no new failure token,
automatic retry, provider-fix claim or permanent raw web-content store is introduced.
