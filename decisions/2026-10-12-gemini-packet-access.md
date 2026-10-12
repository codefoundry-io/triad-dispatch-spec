# Gemini packet availability (C79)

## Evidence and cause

- Shared main inspected: `fcd96a15d18f3131c1f0111bdb10c3faceae34f8`.
- [B issue 42](https://github.com/codefoundry-io/triad-codex-dispatch/issues/42)
  reports Gemini CLI 0.63.0, B 0.2.559 / `6cc7271f`, guarded-worktree:
  native `read_file` rejects external `shared/TASK.md` and `shared/REVIEW.diff`
  with `Path not in workspace`. Vendor/wrapper exit 0 and schema-valid
  DO NOT MERGE describe missing coverage, not a transport failure.
- B `bin/review_round_v2.py` selects product cwd and renders packet paths from
  the separate prepared directory. `bin/gemini_wrapper.py` only forwards raw
  `--add-dir` to native `--include-directories`, while refusing raw extra roots
  for formal review. Provider-free version/policy preflight cannot prove reads.
- A `1de943af4436b3eca2aea903d05c223c8d56f92d`:
  `.claude/skills/triad-cross-family-review/lib/review_scratch.py` creates its
  worktree inside the packet directory (3208-3213) and writes brief/patch/history
  inside that worktree (3619-3633). `lib/roster_v2.py` launches from it (845-850,
  905-920). A's Gemini wrapper has no include-directories fix to copy.
- Official [Gemini CLI configuration](https://geminicli.com/docs/reference/configuration/)
  documents `--include-directories`; exact task-local 0.63.0 `--help` exposes it.
  The owner's global 0.60.0 installation is unchanged. Native read verification
  and the generated formal call are recorded separately below when run.

## Bounded implementation and preserved behavior

R-PREPARE already requires available packet inputs. Clarify its observable
meaning and add C79 before changing host code. Keep B's existing external packet
lifecycle; moving custody or embedding the entire diff would change more scope.

1. Add a failing actual-wrapper/producer regression for the external packet.
2. Propagate the exact `prepared_dir` only to guarded Gemini launch controls,
   using a dedicated internal wrapper option. Bind the value through the existing
   preflight digest, adapter and allocation; reject invalid or changed controls.
3. Verify packet reads, related product discovery, rejected broad/sibling grants,
   unchanged negative-result collection, and existing raw/prepared-directory paths.
4. Verify the provider-free 0.63 file-tool behavior and review the bounded change.
   The owner will test authenticated Gemini inside the company after release;
   that live test is not a prerequisite for this release and remains NOT RUN here.

Expected production scope: four Python modules, approximately 50-90 added lines;
focused regressions plus short user/reference documentation. No prompt clause,
verdict schema, authentication, model/effort, user setting or native-host change.
The packaged read-only policy and exact executed-command custody remain intact.
Changing these launch controls requires a fresh review basis; no hand-edited
same-basis argv or relabelled old verdict is admitted.

On A: retain co-location and exercise C79 at its next conformance run; no host
rewrite is requested. On B: fix the confirmed missing propagation. Other-host
review is requested on the same specification commit; the owner has authorized
B to continue independently under settled contracts.

## Verification status

The task-local official Gemini 0.63.0 package's actual `Config`, `WorkspaceContext`
and `ReadFileTool` reproduce `path_not_in_workspace` without the packet root, read
the marker with only `shared` added, and still deny an unrelated sibling. The
probe uses the installed entry point's core chunk `chunk-RWBXO4OP.js`; network is
disabled. It applies the native pending-directory registration loop without full
Config initialization and replaces only the storage temp getter with an isolated
fixture path. It therefore proves native file-tool behavior, not CLI parsing,
authentication, a model call, or effective enterprise policy.

B implementation/regressions: pending. A current read-only source inspected;
runtime C79 NOT RUN. The owner requested implementation and release with actual
Gemini validation afterward in their company environment. No live Gemini success
or change to A, user settings, installation or tagged spec adoption is claimed.
