# DevOps Verification Report

Owner/operator: Osman Berke Özdemir (@makucheez), with AI-assisted execution. Date: 19 November 2026. Tracking: [#63](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/63).
Status: local and published CI evidence recorded for the implementation SHA below. No teammate approval or independent run is claimed.

## Sources and boundaries

- Current develop: `1e50523cda7b06ece5b5be4927353390c4aab562` (no backend).
- Current main: `178f93138f678e45d6f74ee36e7a554d409172ab`; develop is an ancestor and has no content difference against main.
- Auth source: PR #58, `7f3fa7735987dc59bc54be5257f9e2145c529a1c`, open with main target, no reviews at inspection.
- Requirements source: PR #62, `50f42988f6a10d5f44f7095f0e1f377818e84cdc`, open with develop target. It is not merged or copied into this change.
- No automated auth test files were found in develop, #58 or #62. The new environment smoke is Osman's authored infrastructure verification; it is not attributed to Berat/Mehmet.

## Runtime reproduction

Python 3.9.6 / SQLite 3.54.0 on macOS arm64; source files extracted directly from the tracked PR SHA into a fresh temporary directory. The environment runner copies only `src` again into disposable storage, starts the actual `python src/server.py` entry point, creates synthetic accounts, stops/restarts the server and removes generated DB/logs. No actual user data was touched. Port 8000 was used as hard-coded by the source. No npm packages, runtime pip dependencies or environment values were required.

Command: `python3 scripts/check_auth_environment.py --source-root <isolated-reference> --report /tmp/tutorbridge-auth-smoke.json`

**Observed: 15 passed, 0 failed.**

| Cases | Observed |
|---|---|
| Registration and login pages served | HTTP 200 for each; HTML serving only, no browser interaction |
| Initial database | users/auth_tokens tables created under data/tutorbridge.db |
| Valid registration | 201, public profile fields only |
| Duplicate email / short password / invalid role | 409 / 400 / 400 |
| Wrong password / valid login | 401 / 200 with bearer and expiresIn 3600 |
| Valid own-profile token | 200, matches registered public profile |
| Missing / invalid / expired token | 401 each; expiry set only in disposable DB |
| Public /data/tutorbridge.db URL | 404; DB outside src |
| Stop/restart and login | Persisted synthetic account accepted after restart |

The runner's initial port preflight incorrectly treated TIME_WAIT as an occupied listener on a rapid rerun. It was corrected to permit address reuse while still rejecting an active listener; the full validation-probe rerun then completed. This was a tooling correction, not an application defect.

## Failed acceptance probes

Command: same runner with `--validation-probes --report /tmp/tutorbridge-auth-probes.json`.

**Observed: 15 passed, 2 failed; exit code 1.**

| Input | Required | Observed / disposition |
|---|---|---|
| Email invalid@ | 400 | 201; known source defect reproduced, Mehmet's auth fix needed |
| JSON null name | 400 | 201; source coerces null into text, Mehmet's auth fix needed |

These inputs use separate synthetic accounts. Failures are not xfailed or presented as success. Basic smoke excludes these extra acceptance probes by explicit scope; therefore a green smoke does not close US-01/US-02/US-15. Role-specific browser routing and logout remain unaccepted.

## Structural checks and hygiene

Actual local results:

| Command/check | Result | Scope |
|---|---|---|
| Existing check_submission.py | PASS: OpenAPI 3.0.3, 16 operations, 27 examples, links, SVG XML, RACI | Contract/documents only |
| check_sprint2.py | PASS with explicit missing-team-document notices | Structural/hygiene only |
| check_sprint2.py --release-ready | FAIL, exit 1 | Seven proposed team-document paths not integrated; expected release blocker |
| python3 -m unittest discover -s tests -v | 8/8 PASS | Packaging/structural-check safety and integrity, not application tests |
| git diff --check | PASS | Whitespace only |

The local Python 3.9.6 document validator emitted urllib3's LibreSSL compatibility warning; structural checks still passed. No external HTTPS access was validated by that local command. CI uses the separate Python 3.12 environment.

Synthetic recovery rehearsal: loaded the pinned server module with its DATABASE_PATH redirected into a fresh temporary directory, initialized the real schema, inserted one synthetic hashed account, used SQLite's backup API, obtained integrity_check = ok, preserved the original DB, restored from the backup, and verified the recovered account/hash. PASS. The temporary directory was removed; no real user-data restore, time-based recovery target or deployment rollback was tested.

Tooling tests use independent temporary Git repositories. They verify exact source/binary round-trip and DRAFT labeling; reject untagged final refs, missing team paths, private config and tag/main mismatches; accept matching-main tagged source packages without claiming human approval; and catch broken local links and incomplete structural readiness. No test tag is created in the real repository.

 Existing `Sprint 1 checks` remains unchanged. Its purpose is contract/example/link/SVG/RACI validation, not runtime behavior. Sprint 2 adds tracked-document structure, local file links, basic diagram-source checks and runtime-file hygiene; missing team documents are reported separately and fail `--release-ready`.

The pre-existing tracked .env contained only one newline and zero configuration entries; no credential value was present in that file. It is removed from tracking without altering history, and `.env.example` explicitly states the prototype loads no environment configuration. Ignore rules cover data, uploads, SQLite sidecars and test artifacts. This is not a full historical secret audit.

## Access, review and release findings

Using authenticated makucheez / Write: both branch summaries report protected, required Sprint 1 checks and everyone enforcement. Detailed protection endpoints returned 404; effective rules returned empty lists. No rule was changed. Administrator verification of approval/conversation/admin settings remains pending.

Accepted collaborators include mhmttemin with Read but do not list goksuyldrm/nedima68. No account invitations or permission changes were attempted. Live Teams/Figma access was not available or verified; only the supplied Teams text was reviewed.

No complete Sprint 2 NFR/Figma/C4/UML/user-flow/traceability set exists in the reviewed trees. No Sprint 2 release/tag/final package or live deployment has been created. A prepared release description and explicit checklist gates are supplied. Missing artifacts and independent human review block final delivery.

## Published implementation and CI evidence

[PR #64](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/64) targets develop and is authored by makucheez. GitHub maps [implementation commit 7b5cea90befd2336eaac6358c2eae4a07f1fb0e8](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/7b5cea90befd2336eaac6358c2eae4a07f1fb0e8) to makucheez, with commit name Osman Berke Özdemir and the account's numeric noreply address.

- [Sprint 1 workflow](https://github.com/Sprint-1-Software-engineering/Sprint-1/actions/runs/44579543261): SUCCESS on that implementation SHA.
- [Sprint 2 workflow](https://github.com/Sprint-1-Software-engineering/Sprint-1/actions/runs/44579543410): SUCCESS on that implementation SHA. Structural/hygiene and eight tooling tests passed; the integrated-runtime job was SKIPPED because server.py is absent. Its explicit absence notice is not an application test result.
- The separately labeled PR #58 reference smoke in that Sprint 2 run passed 15/15 checks on Ubuntu with Python 3.12.16. Its uploaded JSON artifact was downloaded and inspected; failed count 0, validation_probes false. That result covers pinned auth source 7f3fa7735987dc59bc54be5257f9e2145c529a1c, not an integrated backend in the DevOps PR.

The two additional validation probes were run locally and failed as recorded above; they are not silently included in the successful basic CI smoke. Documentation-only evidence updates after the implementation commit have their own checks visible in [the PR checks](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/64/checks); do not infer results for an untested later release SHA.

At the PR inspection GitHub reported REVIEW_REQUIRED / BLOCKED. No self-approval, bypass or merge was attempted. The final release remains pending external artifacts, access decisions and genuine teammate reviews.
