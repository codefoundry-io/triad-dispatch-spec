# Codex + three Google legs: operating specification

This is the operating profile authorized by
[the agreement](2026-09-21-codex-google-four-leg-agreement.md). The shared rules and
schemas remain authoritative; this document supplies a concrete setup and
verification procedure. It introduces no new configuration or result fields.

<a id="SPEC-FOUR-LEG-SCOPE"></a>
## Topology and review emphasis

The following names and emphases are a maintainer-proposed example, not additional
owner rulings. They can be changed before the review basis is frozen.

| Enabled entry | Family | Review emphasis |
|---|---|---|
| `codex` | codex | Complete independent correctness and integration review |
| `google-contracts` | google | Requirements, contracts, interfaces and affected consumers |
| `google-failures` | google | Boundary inputs, failure paths and regression evidence |
| `google-state` | google | State transitions, ordering and interactions between components |

All four inspect the same complete approved scope and common criteria, including
R-SMELL. Emphasis is additional attention, not permission to omit relevant
findings, tests or unchanged consumers. Do not create a dedicated smell-only leg.

On host B the Codex entry stays a fresh native Codex child. On host A, a Codex
entry uses A's existing Codex CLI route; A's native family is Claude. Do not add a
native Codex mechanism to A or silently substitute native Claude for the specified
Codex entry. Report that topology distinction in the resolved run description.

## Project roster example for B's Legacy Gemini CLI route

This example uses the existing B project file `.agents/triad-review-legs.json`.
It assumes the host's existing authentication and capability checks permit the
Gemini route. `null` uses the adapter's supported default; it is not proof of the
actual runtime model. Do not bypass a route, version, login or policy refusal.

```json
{
  "schema": "triad-review-legs.v2",
  "legs": [
    {"name": "claude", "enabled": false},
    {"name": "google", "enabled": false},
    {"name": "codex", "enabled": true},
    {
      "name": "google-contracts", "vendor": "google", "enabled": true,
      "acceptance": "participating", "timeout_s": 600,
      "google": {"route": "gemini"},
      "gemini": {"model": null, "effort": null}
    },
    {
      "name": "google-failures", "vendor": "google", "enabled": true,
      "acceptance": "participating", "timeout_s": 600,
      "google": {"route": "gemini"},
      "gemini": {"model": null, "effort": null}
    },
    {
      "name": "google-state", "vendor": "google", "enabled": true,
      "acceptance": "participating", "timeout_s": 600,
      "google": {"route": "gemini"},
      "gemini": {"model": null, "effort": null}
    }
  ]
}
```

Overrides merge by name. Disabling the shipped `google` entry avoids accidentally
running it alongside the three named replacements. Inspect the actual resolved
roster: it must contain exactly the four enabled names above, even if the existing
project configuration has other optional entries. Preserve unrelated owner
configuration; apply a reviewed project-local delta rather than replacing it.
For AGY, use its existing route/configuration and capability checks instead; never
copy a Gemini model identifier into an AGY control or change a started route.

Host A keeps its own project-roster location and adapter defaults. This B example
is not a command to copy B's installation paths or auth policy into A.

## B: bound task mapping, not a new lens field

Put the emphasis table in the common bound `TASK.md` before preparation and give
the reviewer this short task framing:

```text
Use your bound leg_name to select the emphasis in the table. Review the complete
shared scope and criteria, applying that emphasis. Return one bound verdict for
your own leg and report only evidence you inspected.
```

Use the existing task/brief and common objective channel. The renderer already
supplies `leg_name`; the roster's `note` is not a prompt override. Do not add
unsupported `lens`, `focus` or `prompt` keys, mutate a rendered prompt after
allocation, or pretend the host mechanically validates lens coverage.

The leader checks the returned criteria and evidence against the intended
emphasis. This is a semantic review check, not a new wire field or automatic
coverage guarantee. Changing the table, shared criteria, roster or controls
changes the basis and requires every participating leg to review again.

These are verified B integration seams. A's published main still uses advisory
X legs and its older family renderer; it does not establish this named v2 task
mapping. Claude must reconcile its in-progress v2 checkout against
[the current-source handoff](claude-codex-google-four-leg-handoff.md) first.

<a id="SPEC-FOUR-LEG-COLLECTION"></a>
## B: dispatch, collection and owner decision

Use B's existing explicit v2 workflow. Resolve and show the four entries,
prepare and bind the common packet, validate every adapter, and allocate all four
independent invocations. Start their native/CLI calls using the host's supported
concurrent dispatch; provider capacity or account failures remain observable
failures, not permission to drop a leg or weaken controls. No new scheduler is
needed. Preserve each name/attempt's prompt, result, read evidence and receipt.

Expected outcomes specialize R-AGREE without changing it:

| Observed state | Existing outcome |
|---|---|
| An enabled entry is missing or recorded as failed-to-run | `INCOMPLETE` on B; preserve the actual host outcome/evidence |
| Invalid verdict, binding or custody evidence | Validation refusal or a recorded failed attempt; never agreement |
| All enabled entries complete and one has a blocking finding or unresolved question | `BLOCKED` on B; no silent majority override |
| All four complete without blockers, with Codex and Google coverage | `OWNER_DECISION_REQUIRED` on B; two families, not four |
| The owner decides after reading that result | Record the decision against that round and content digest; retain the original machine result |

Owner approval is a separate record using the existing decision channel.
It identifies the round/basis, actual four entries and two families, findings and
their dispositions, and the owner's explicit decision. Do not rewrite a raw
verdict, fabricate three-family coverage, change `OWNER_DECISION_REQUIRED` into
`AGREED`, or apply a blanket approval to future/changed bytes. The choice to use
this profile is not final approval of an unrun round.

A failed-to-run entry may retry only after diagnosis with unchanged conditions.
A completed negative review is not a transport retry. Evidence export, cleanup,
read-only containment and direct-owner-request-only web policy remain unchanged.

## Verification and Claude deliverable

[Case C33](../cases/cases.json) owns the profile's expected behavior; C12, C14,
C19 and C20 retain the underlying roster, binding and retry/re-review cases.
Claude should first inspect its actual current implementation. For an A v2 port,
use its existing approved migration scope; do not treat A's published legacy X
legs as proof that the following checks already pass. Then:

1. Validate the override and resolve exactly four enabled entries/two families.
2. Confirm four exclusive invocation/result/read-evidence locations. Prove a
   same-family sibling's result or receipt cannot satisfy another entry.
3. Verify clean two-family completion requests an owner decision; missing,
   invalid and blocking results remain distinguishable.
4. Check that the frozen task mapping and each leg's bound identity reach the
   actual prompt; describe the mapping as semantic, not mechanically enforced.
5. Verify failed-entry-only retry and full re-review when a lens/task changes.
6. Where the exact live route is available and a bounded run is authorized,
   execute the four invocations and retain terminal results and the owner decision.
   Otherwise record that live scenario as NOT RUN with a concrete run procedure.

This authoring change does not execute that live scenario. A single successful
Gemini call is not evidence of four concurrent calls, host policy enforcement,
the lens assignments or a completed review/admission. Do not add an application
UI, automatic technology detection, a voting policy, or a new lens schema while
implementing this operating profile.
