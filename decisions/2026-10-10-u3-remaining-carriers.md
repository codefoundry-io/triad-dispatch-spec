# Remaining U3 result-carrier assessment

2026-10-10; main3afc4d7, sharedc495b1b, B632f426 plus verified candidate;
read-only A1ea9cb3e. DL-113 recovery and DL-102 turn-timeout are completed B
candidate units. This note is assessment, not a new rule or implementation.

## DL-102 truncation: identify the answer channel before code

R-CLASSIFY says an answer carrying an own-line `<truncated N bytes>` or
`<truncated N lines>` marker is withheld, while a mid-sentence quote does not
count. B returns result.response on its raw route, but its schema route validates
and emits result.structured_output. Existing B tests deliberately preserve a
valid structured result independently of response transport decoration.

A1ea9cb3e antigravity_wrapper.py:905-934 selects response as the local `answer`
string and separately detects a structured-output dict. Its marker check at
1013 runs on that response before the structured-output handling at1023-1040.
Thus the source would also withhold a valid structured object if the separate
response carries an own-line marker. This is a source-derived boundary question,
not a measured vendor incident or a claim that current AGY produces that pair.

Please confirm whether the common marker rule applies to the answer channel
actually emitted, leaving an intact schema-validated structured_output usable
when only incidental response text is folded, or identify the existing rule and
capture that require discarding both channels. B will not guess a JSON-field
scan or copy A's response check into its schema path without resolving this.
No fresh paid failure generation or search for the expired September log is asked.

## DL-101 network error: existing measured row, separate unit

The frozen row records `There was a network issue connecting to the server,
please try again.` in the ERROR/empty-response/raw1 result; the ledger identifies
result.error. B currently classifies only stderr/status. A uses its typed
agy_classify_signals input, labelled before classification
(antigravity_wrapper.py:135-165), not raw output/answer/tool text.

An implementation must retain authentication and host/transport priority, known
vendor exit-map priority and the existing non-auth class order. Passing every
terminal error to broad phrase matching would also change unmeasured quota
placement; that is not authorized by this row. No implementation chosen here.
This independent row does not require resolving the truncation channel question.
