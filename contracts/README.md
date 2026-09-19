# contracts/ — machine-readable contracts

| File | Status (current draft) | Consumers |
|---|---|---|
| `gemini-readonly.toml` | seed = host A's shipped file; header EXPANDED with the version-pinned source cite (A's shipped substance was already right: `--policy` replaces the user tier; admin/workspace/defaults still load — `packages/core/src/policy/config.ts` at tags v0.46.0 and v0.60.0, raw source fetched 2026-09-19) | A `gemini_wrapper.py` attaches it on the read-only posture; B keeps `gemini-formal-readonly.toml` until the rename is specified (codex second pass) |
| `exit-tokens.json` | seed = host A's 18-token map as data; B delta noted inside | both hosts' `_common.py` tables, membership-tested (D-11) |
| `review-legs.example.json` | post-cut roster example (owner Q-M/Q-O; codex High #1) | both loaders; schema file to follow |
| `leg-verdict.schema.json` | NOT YET — round r2 (all three families) converged on a superset v2 wire; the mapping and proposed shape are in `leg-verdict-mapping.md`; the schema file follows codex's co-review | both validators; prompt shape pins |
| `leg-verdict-mapping.md` | round r2 output: A↔B mapping table, losses per direction, the proposed v2 shape, the three release properties that must survive | both maintainers (D-3) |
| `review-legs.schema.json` | NOT YET — written from the example once codex confirms the per-vendor blocks | both loaders |
| `receipt-fields.json` | NOT YET — transport receipt vocabulary (`stdin_delivery` class, route/version fields) | both `_common.py` |

Proposed changes to `gemini-readonly.toml` (NOT applied to the seed; each becomes a case before it lands): add a
`grep_search` allow row beside `search_file_content` (current registered name per the Gemini CLI tools reference,
2026-09-01); explicit rows for `google_web_search` / `web_fetch` per the D-9 decision; a `toolName = "*"` deny at a
priority below the allows (NOTE from round r2: a user-tier `*` deny also overrides the DEFAULT tier's allows for every
unlisted tool, including `google_web_search` — intended only if D-9 = deny). Effective postures TODAY (round r2, v0.60.0
default policies): A = search ALLOWED by inheritance, fetch denied by the default headless rule; B = both allowed at user
priority 999 with a `*` deny at 998.
