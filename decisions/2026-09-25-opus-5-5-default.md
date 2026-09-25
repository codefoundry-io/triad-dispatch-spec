# Claude Opus 5.5 default and host handoff

Owner request: "codex traid dispatch에 기본모델 opus 5.5로 업데이트하고 spen에도 업데이트해"
The leader interprets "spen" as the shared specification in this request.

## Evidence and change

Authoring base: remote `main` at
`af5533c6b412b60b3ef44750ddcd05bbedb8065a`, fetched before this change.
Codex host source base: `2d4d71b1a6df09b26fae44d228229cd9aa43218d`;
remote main merge: `5a12f822b6e19f5ecd162e4cc54888269ec0ffd9`.
The B implementation is commit `45e21f5d32fce88ba674f4783bd1391d678ef662`
in [draft PR #38](https://github.com/codefoundry-io/triad-codex-dispatch/pull/38).

Anthropic documents `claude-opus-5-5` in its
[Claude Code model guide](https://support.claude.com/en/articles/11940350-claude-code-model-configuration).
Its [effort table](https://code.claude.com/docs/en/model-config#adjust-effort-level)
lists `low`, `medium`, `high`, `xhigh` and `max` for Opus 5.5.
The locally observed Claude Code version was 2.1.282. Documentation and version
inspection establish supported controls, not account entitlement or inference.

B currently ships `opus` in `contracts/review-legs.default.json` and in
`bin/claude_wrapper.py:FORMAL_CLAUDE_MODEL`. Its capability document recognizes
Opus 5 but lacks Opus 5.5. A new capability row alone cannot pin the CLI alias.

The owner-selected behavior is defined once in
[R-ROSTER](../reference/review-rules.md#R-ROSTER) and exercised by C12/C34.
B updates the default roster, legacy formal pin, capability row and their
consuming skill/documentation/test surfaces. Raw calls keep their existing
passthrough; v2 overrides, null selection, older supported models, timeout,
web authorization, authentication and no-fallback guards retain their meanings.
No shared schema enum, prompt payload or adoption manifest needs changing.

## Host handoff and verification

B implements the requested default first. A's maintainer should review this
same shared commit and check the roster/agent defaults at the existing `roster`
unit paths in `units.json`; preserve its native topology and override behavior.
A's source and installed configuration have not been changed. A implementation,
acknowledgement and conformance remain pending; they are not inferred from B.

Verify no-file default selection, explicit older-model override, null selection,
Opus 5.5 capability recognition and refusal when that pin reports Opus 5.
For B, additionally verify legacy exact-model/effort/timeout/no-fallback behavior,
raw passthrough and the existing web/schema/transport regressions. Retain original
RED and final verification outcomes separately from provider or release claims.

Verification completed in B's existing source worktree:

- Fresh dedicated RED: 22 failed, 103 passed; the source skill still prescribed
  `opus`, and the new model selection/capability assertions failed.
- Final fresh dedicated GREEN: focused suite 127 passed; full suite 1,686 passed;
  both source skills passed validation. Source fingerprints stayed unchanged.
- One intervening failure came from a pre-existing AGENTS relocation. Its test
  now follows the explicitly linked verification guide, while retaining support
  for the original inline guide. Existing policy edits were preserved.
- Shared-spec suite: 106 passed. Authoring map check: 1 valid, 0 invalid.
- Actual B adapter preflight against installed Claude Code 2.1.282 recorded
  requested and selected `claude-opus-5-5`, requested effort `xhigh`, and
  `provider_started: false`. This was session-only selection, not inference.
- Independent read-only source audit found no actionable issues.

The required multi-family gate remains pending: both existing AGY projects for
the selected B worktree lack the default-review `read_url(*)` deny and fail the
read-only project guard. Their bytes were unchanged and no review provider was
started. No permission change, authenticated inference, installation, revision
tag, host adoption or public release is claimed.
