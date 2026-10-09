# DL-106 — B removal boundary

Remote main verified at3afc4d7e931e55d601dd74877bdbe65e610a8e59.
B632f426 plus completed U4c candidate has three vendor maps containing only
0:ok and an unreferenced _json_len helper. Success returns before the maps;
on a failed wrapper result, an ok map entry does not determine classification.
Current source/test/script searches find no named consumer of those symbols
outside their definitions and classify's own map selection. They can be removed
while preserving supported extension mapping and every current outcome.

DL-106's historical claim that B's AGY zero:extraction-error fallback is dead
does not describe the current code. It is reachable through no-answer/extraction
classification with raw exit0 and a failed wrapper result. Preserve that
fallback and the stronger auth/capacity/token/schema outcomes ahead of it.
Likewise, removal of classify's optional vendor_exit_code argument is not part
of this private cleanup: B retains its callable compatibility. A's mechanism
does not determine B's internal interface. No new common key-range restriction.

Read-only A a5afdd5a has already removed the three maps and _json_len. A tests
are not run by B. PR13reply6088729953 agrees with C76 and supplies C77 source
evidence; its reported F3-c plan amendment is not independently confirmed in
the local plan inspected at that revision. F3-c remains A's pending Phase7 work.
This does not reopen B's reviewed verifier or request a combined apply/verify
command port. A will synchronize its own C77 tests.A after the case reaches main.

B's next bounded change removes only demonstrated redundancy. Existing complete
classifier/wrapper/replay modules run before and after, with isolated child
log/TMPDIR roots. No synthetic vendor incident, new classifier vocabulary or
private-name absence test is added. Formal review and completion evidence follow.
