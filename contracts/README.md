# contracts/ — machine-readable contracts

| File | Status (current draft) | Consumers |
|---|---|---|
| `gemini-readonly.toml` | D-9 RULED 2026-09-19 (owner): review legs have no web tools — explicit `google_web_search` / `web_fetch` deny rows at 200 (before: search inherited from the default tier, `--policy` replaces only the user tier — `packages/core/src/policy/config.ts` at v0.46.0 / v0.60.0). Rules are the contract, vendored byte-for-byte (A test t50 checks parity); applied without a live run | A `gemini_wrapper.py` attaches it on the read-only posture; B drops the two web tools from its 999 allow list (`bin/policies/gemini-formal-readonly.toml:12-13`) |
| `gemini-readonly.verify.toml` | NEW — verification manifest for the effects that cannot be exercised where only agy runs (R-GOOGLE convention): V1 web denies, V2 reads/search control, V3 `grep_search` alias, V4 mutation denies, V5 proposed `*` catch-all; all NOT RUN | the owner, where gemini is in service; results → `decisions/owner-register.md` + C15 test column |
| `exit-tokens.json` | seed = host A's 18-token map as data; B delta noted inside | both hosts' `_common.py` tables, membership-tested (D-11) |
| `review-legs.example.json` | post-cut roster example (owner Q-M/Q-O; codex High #1) | both loaders; schema file to follow |
| `leg-verdict.schema.json` | NOT YET — round r2 (all three families) converged on a superset v2 wire; the mapping and proposed shape are in `leg-verdict-mapping.md`; the schema file follows codex's co-review | both validators; prompt shape pins |
| `leg-verdict-mapping.md` | round r2 output: A↔B mapping table, losses per direction, the proposed v2 shape, the three release properties that must survive | both maintainers (D-3) |
| `review-legs.schema.json` | NOT YET — written from the example once codex confirms the per-vendor blocks | both loaders |
| `receipt-fields.json` | NOT YET — transport receipt vocabulary (`stdin_delivery` class, route/version fields) | both `_common.py` |

Remaining proposals for `gemini-readonly.toml` (each lands only after its manifest check passes — `gemini-readonly.verify.toml`): a `grep_search` allow row beside `search_file_content` (V3: current registered name per the Gemini CLI tools reference, 2026-09-01); a `toolName = "*"` deny below the allows (V5: a user-tier `*` deny also overrides the DEFAULT tier's allows for every unlisted tool — B ships this shape at 998/999). Effective postures TODAY (v0.60.0 default policies): A = web tools DENIED by explicit rows (D-9), fetch also denied by the default headless rule; B = both allowed at user priority 999 with a `*` deny at 998 until codex applies D-9.
