# B project roster location — D-5 proposal

Status: pending owner choice. No loader, project file or user-global setting was
created from this proposal. The settled roster schema and R-ROSTER remain unchanged.

`units.json` retains D-5 for B's project-scope file location. The historical A
[parity plan](https://github.com/codefoundry-io/triad/blob/92c8afd500499d8736afcc28b39a87a4f87fed50/docs/superpowers/plans/2026-09-19-triad-host-parity-plan.md#L602-L610)
proposes `.agents/triad-review-legs.json` but marks the choice open; that proposal
is not evidence of an owner decision.

The Codex leader recommends that project-relative path. Alternatives presented
to the owner are root-level `triad-review-legs.json` or an explicitly supplied
file only, without discovery. In every option the shared named-override schema
and merge rules apply, no user-global dependency is added, and absence of an
override uses the shipped three-family default data.

The owner was asked to choose the path before implementing discovery. D-B1
Gemini policy composition and D-B2 exact evidence custody remain separate pending
choices. Schema-only resolver research does not settle the location or imply
capability validation/public v2 activation. A remains read-only.
