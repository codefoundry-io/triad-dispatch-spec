# DL-102 — B terminal turn-timeout implementation scope

2026-10-10; main3afc4d7, B632f426 plus candidate, read-only A a5456b13.
The existing vendor-failure-lines row records AGY1.1.26 (2026-09-04): terminal
result.error begins `timeout waiting for response`, status ERROR, empty response,
vendor exit1 -> vendor-timeout/65. No new vendor incident or common rule is added.

B's _interpret_run currently classifies nonzero exits from stderr/status alone;
the typed error appears only in a later diagnostic. Implement that measured row
with one bounded carrier check, preserving auth, host timeout and transport
priority. Retain stdout for custody, withhold the answer and use the existing
token/exit. A's _is_vendor_turn_timeout has an anchored phrase predicate; its
broader matching is A implementation evidence, not new B carrier authority.

No raw-output/answer/tool/stderr phrase search, new error catalog, retry or native
change. DL-113's pending admission questions do not affect this independent row.
DL-102's answer-truncation half stays pending; no whole-case completion claim.

Before code, fresh dedicated RED will exercise the actual interpreter with
constructed row inputs and boundary controls. GREEN covers complete related
wrapper/auth/transport/replay/token modules, full suite and source validators;
the required independent review follows. B test: tests/test_agy_turn_timeout.py.
A changes: none requested. Please flag any concrete conflict with this settled row.
