# TutorBridge - Review and Test Plan

Version: 0.1 draft, 23 November 2026. Owner: Berat Erdem Yalçın (Quality / Testing). Tracking: [Issue #72](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/72). Quality targets: [NFR and Quality Measures](NFR-and-Quality-Measures.md).
Review state: prepared for peer review. No team approval is claimed.

## 1. Purpose, scope and status values

The plan lists normal, negative and boundary cases for registration, login, roles, connections, lessons and assignments. Each case names the expected HTTP response from the [SRS](SRS.md) and the [OpenAPI draft](../Openapi.yaml) and is mapped to a functional requirement (FR), acceptance criterion (AC) and story (US). Expected values come from those documents, not from the code.

Only registration, login and `GET /users/me` exist in the code today. Every other area is **Planned**: nothing was run and no result is claimed.

| Status | Meaning |
|---|---|
| Pass / Fail | Executed on 23 November 2026 against `develop` at `ec696e3`; re-tested at `7fccc47` where the text says so. Local API only. |
| Expected failure | Executed; fails because of a known defect that has an Issue. CI treats it as expected. No case has this status at `7fccc47`; P-01 had it until #71 was fixed. |
| Observation | Executed; the specification gives no expected value, so the observed behavior is recorded. |
| Planned | Not executed. The feature, the browser session or the Figma review does not exist yet. |
| Static | Judged by reading the source files; no browser was used. |
| Browser | Executed in headless Chromium 159 (Playwright) on 23 November 2026 against the `develop` front end at `7fccc47`, served by the local handler. The scripts are not committed (they need Playwright). Not a test on a real desktop browser, a device or assistive technology. |

## 2. Environment and how to run

- Local Python 3.12 HTTP server from `src/server.py`, temporary SQLite database, random localhost port, synthetic accounts only. CI uses `ubuntu-latest`.
- Repeatable suite: `python -m unittest tests.test_auth_quality -v` (cases below marked "QA suite"). Whole suite: `python -m unittest discover -s tests`; the delivery-tool tests need `git` on `PATH`.
- Latency baseline: `python scripts/measure_auth_latency.py`.
- No real token, password or personal data is written to any report or log. Test passwords are synthetic.
- Not covered: real desktop browsers, devices and assistive technology (only a headless Chromium run was done), the live Figma file, a hosted environment, load beyond 10 concurrent users, code coverage.

## 3. Results executed so far (23 November 2026)

| Run | Scope | Result |
|---|---|---|
| QA suite, `tests/test_auth_quality.py` (committed) | Registration, login, token and profile, hashing, simultaneous registration | At `ec696e3`: 23 tests, 22 pass, 1 expected failure (P-01, Issue [#71](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/71)). At `7fccc47`, after the fix in PR #79: 23 tests, all pass; P-01 is now a normal test that the code owner extended in PR #79 to cover `abc` and `-1` on both auth endpoints. About 6.4 s; identical result in 4 consecutive runs at `ec696e3` and 2 at `7fccc47`. The CI log of the Sprint 2 validation run for `develop` at `7fccc47` shows these tests passing on `ubuntu-26.04`. |
| Existing `tests/test_auth_api.py` (written by the team) | 5 registration and login cases | Executed by QA as part of the whole suite: pass. Not counted as new QA cases. |
| Whole suite, `unittest discover -s tests` | 42 tests including DevOps delivery-tool tests | At `ec696e3`: OK with 1 expected failure. At `7fccc47`: 42 tests OK, no expected failures (also in CI). Needs `git` on `PATH`; without it 14 delivery-tool tests error with `FileNotFoundError`, which is an environment gap, not an application result. |
| Exploratory run (script not committed) | The same cases plus probes: 77 checks | At `ec696e3`: 66 pass, 1 fail (P-01), 10 observations, identical in two runs. At `7fccc47`: 67 pass, 0 fail, 10 observations, 0 unhandled server exceptions, identical in two runs. Source of the Observations in section 4.8. |
| Mutation check | Three deliberately broken copies of `server.py` (password minimum 8, two-hour sessions, login accepts any password) | All three were detected by the QA suite (R-05, T-06, L-03). A fourth copy with the #71 fix reverted made the new P-01 test fail (2 sub-cases). The repository files were not changed. |
| Headless browser runs (Playwright, Chromium 159; scripts not committed) | Login and registration pages, dashboards, Tab order and focus | Main script, 30 checks: 14 pass, 2 fail (error messages not announced, UI-04), 14 observations. Two follow-up scripts compared the teacher and student dashboards (2 of 77 text lines differ after the name is replaced; the difference is the avatar initial) and the Tab order (login 8 stops, register 13 plus the radio group; every stop is `:focus-visible` and changes style on focus). The first run of the main script contained script errors (reversed expected and observed values, a wrong Tab-order assumption); they were corrected and the results here come from the corrected script. Source of UI-01 to UI-06 and UI-09 to UI-11 in section 4.9. |

### Re-test of the defects reproduced on 19 November

The [SRS](SRS.md) section 8 and the [Verification Report](Verification-Report.md) describe two input defects found in the PR #58 snapshot: `invalid@` as e-mail and JSON `null` as name were accepted with 201.

QA ran the same checks on the PR #58 snapshot (`7f3fa77`, from the team's reference ZIP) and on current `develop` (`ec696e3`):

| Check | PR #58 snapshot | `develop` `ec696e3` |
|---|---|---|
| R-10 `invalid@` and R-10b to R-10f other malformed e-mails | 201 (not rejected) | 400 |
| R-11 name `null` and R-12 name of another JSON type | 201 | 400 |
| R-20 unknown request property on registration | 201 | 400 |
| L-05 missing password, L-06 e-mail `null`, L-07 unknown property on login | 401, 401, 200 | 400, 400, 400 |
| P-01 non-numeric `Content-Length` | no response | no response at `ec696e3` (Issue #71); 400 with the JSON error body at `7fccc47` |

Of 15 checks that failed on the snapshot, 14 passed on `develop` at `ec696e3` and all 15 pass at `7fccc47`. Twelve of the failing checks are additional to the two defects named in the SRS (other malformed e-mails, other name types, unknown properties, login validation). The fixes arrived in the two later commits to `src/server.py` on `develop`; this document does not attribute them further. P-01 existed in both versions, so it was not a regression; it was fixed in PR #79 and QA re-tested it at `7fccc47` (Issue #71 closed).

### Defects and findings

| ID | Finding | Severity | Record |
|---|---|---|---|
| BUG-1 | A non-numeric `Content-Length` closes the connection without a response | Low | Issue [#71](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/71): fixed in PR #79, re-tested by QA at `7fccc47` (400 with the JSON error body on register and login), closed |
| F-1 | Login form states a 6-character minimum; registration and API require 12 | Low | Static finding. Issue [#74](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/74) (see [NFR](NFR-and-Quality-Measures.md) USE-04). PR #79 removed the 6-character check; browser re-test at `7fccc47` passed (empty password, wrong short password, correct password); Issue closed |
| F-2 | Login redirects every role to `main_page.html`; no role routing found | Medium | Static finding, covered by US-15 / [#60](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60) and T-15 / [#61](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61); confirmed in a browser at `7fccc47` (comment on #61): both roles land on `/main_page.html`, the "Öğrenci Bilgi Sistemi" dashboard |
| F-3 | Form error messages are not announced (no `aria-live` or `aria-describedby`) | Low | Static finding, confirmed in a browser (the message has no `role` or `aria-live`; the password input has `aria-invalid="false"` after a server-side error). Proposal Issue [#75](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/75), awaiting a team decision |
| F-4 | `GET /server.py` is served by the static handler | Low | Observation. Proposal Issue [#75](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/75). A `GET` to an unknown API path returning an HTML 404 has no Issue |
| F-5 | No limit on repeated failed logins | Low | Observation; scope decision needed (NFR SEC-10). Proposal Issue [#75](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/75) |
| F-6 | Figma exports: two pairs of byte-identical files named "failure" and "results", unclear role field on registration, missing input limits and timezone on two screens | Low | Issue [#76](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/76); exports only, the live Figma file was not opened |

F-1 and F-6 and BUG-1 are Issues for the code and design owners. F-3, F-4 and F-5 are proposals, not violations of the current SRS, so they were opened as one proposal Issue for a team decision.

## 4. Test cases

Columns: **Type** is N (normal), X (negative) or B (boundary). **Requirement** gives the FR and AC. **Story** gives the user story and its Issue. "QA suite" means the case is part of `tests/test_auth_quality.py`; "Exploratory" means it was only run in the exploratory run.

### 4.1 Registration (FR-01, US-01 / #15)

| ID | Type | Case | Expected | Requirement | Status |
|---|---|---|---|---|---|
| R-01 | N | Valid teacher registration | 201; body has only id, name, e-mail, role | FR-01 AC-01.1 | Pass (QA suite) |
| R-02 | N | Valid student registration | 201 | FR-01 AC-01.1 | Pass (QA suite) |
| R-03 | X | Same e-mail again | 409 | FR-01 AC-01.2 | Pass (QA suite) |
| R-04 | X | Same e-mail with other case and surrounding spaces | 409; one account row | FR-01 AC-01.2 | Pass (QA suite) |
| R-05 | B | Password of 11 characters | 400 | FR-01 AC-01.3, BR-02 | Pass (QA suite) |
| R-06 | B | Password of 12 characters | 201 | BR-02 | Pass (QA suite) |
| R-07 | B | Password of 128 characters | 201 | BR-02 | Pass (QA suite) |
| R-08 | B | Password of 129 characters | 400 | BR-02 | Pass (QA suite) |
| R-09 | X | Role `admin` | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-10 | X | E-mail `invalid@` and other malformed e-mails (R-10b to R-10f) | 400 | FR-01 AC-01.3 | Pass (QA suite, existing suite, Exploratory) |
| R-11 | X | Name `null` | 400 | FR-01 AC-01.3 | Pass (existing suite, Exploratory) |
| R-12 | X | Name as number, list, object or boolean | 400 | FR-01 AC-01.3, BR-02 | Pass (QA suite for number; Exploratory for the rest) |
| R-13 | X | Name of only spaces | 400 | BR-02 | Pass (QA suite) |
| R-14 | B | Name of 100 characters | 201 | BR-02 | Pass (QA suite) |
| R-15 | B | Name of 101 characters | 400 | BR-02 | Pass (QA suite) |
| R-16 | N | Name with Turkish characters ("Yalçın") | 201; name returned unchanged | BR-02 | Pass (QA suite) |
| R-17 | B | E-mail of 254 characters | 201 | BR-02 | Pass (QA suite) |
| R-18 | B | E-mail of 255 characters | 400 | BR-02 | Pass (QA suite) |
| R-19 | X | Each of name, e-mail, password, role missing | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-20 | X | Unknown request property | 400 | FR-01 AC-01.3 | Pass (existing suite, Exploratory) |
| R-21 | X | Empty body | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-22 | X | Malformed JSON | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-23 | X | JSON array instead of object | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-24 | X | Password `null` | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-25 | X | Role as number | 400 | FR-01 AC-01.3 | Pass (QA suite) |
| R-26 | N | Password stored as salted hash, absent from responses | Hash format `pbkdf2_sha256$`; no password in body | FR-01 AC-01.4 | Pass (QA suite) |
| R-27 | X | 8 simultaneous registrations with one e-mail | One 201, seven 409; one account row | FR-01 AC-01.2 | Pass (QA suite) |

### 4.2 Login (FR-02, US-02 / #16)

| ID | Type | Case | Expected | Requirement | Status |
|---|---|---|---|---|---|
| L-01 | N | Valid credentials | 200; `accessToken`, `tokenType` Bearer, `expiresIn` 3600; no other fields | FR-02 AC-02.1 | Pass (QA suite) |
| L-02 | N | E-mail in other letter case | 200 | BR-02 | Pass (QA suite) |
| L-03 | X | Wrong password | 401, generic message | FR-02 AC-02.2 | Pass (QA suite) |
| L-04 | X | Unknown e-mail | 401, body identical to L-03 | FR-02 AC-02.2 | Pass (QA suite) |
| L-05 | X | Password missing | 400 | FR-02 AC-02.2 | Pass (QA suite) |
| L-06 | X | E-mail `null` | 400 | FR-02 AC-02.2 | Pass (QA suite) |
| L-07 | X | Unknown request property | 400 | FR-02 AC-02.2 | Pass (QA suite) |
| L-08 | X | Empty body | 400 | FR-02 AC-02.2 | Pass (QA suite) |

### 4.3 Profile and session (FR-02 AC-02.3, FR-15, US-02 / #16, US-15 / #60)

| ID | Type | Case | Expected | Requirement | Status |
|---|---|---|---|---|---|
| T-01 | N | Valid token on `GET /users/me` | 200; only id, name, e-mail, role; own account | FR-15 AC-15.1 | Pass (QA suite) |
| T-02 | X | No `Authorization` header | 401, `{code, message}` | FR-15 AC-15.2 | Pass (QA suite) |
| T-03 | X | Malformed header: `Bearer`, `Bearer ` (empty), `Token abc`, `abc`, `Basic ...` | 401 | FR-02 AC-02.3 | Pass (QA suite) |
| T-04 | X | Well-formed but unknown token | 401 | FR-02 AC-02.3 | Pass (QA suite) |
| T-05 | X | Expired token (expiry set one second in the past in the temporary database) | 401 | FR-02 AC-02.3 | Pass (QA suite) |
| T-06 | B | Stored expiry after login | 3590 to 3600 s remaining | FR-02 AC-02.1 | Pass (QA suite) |
| T-07 | B | Token with 3 s left: call before and after expiry | 200, then 401 | FR-02 AC-02.3 | Pass (QA suite) |
| T-08 | N | Teacher token and student token | Each returns its own role and account | FR-15 AC-15.3 | Pass (QA suite) |
| T-09 | B | Real one-hour wait, then call | 401 after 3600 s | FR-02 AC-02.1 | Planned (one manual run; not done) |
| T-10 | X | Token after an operator revokes the session or the user logs out | Behavior undefined (SRS OD-02) | FR-02 | Planned after OD-02 is decided |

### 4.4 Roles and access (cross-cutting, BR-01)

| ID | Type | Case | Expected | Requirement | Status |
|---|---|---|---|---|---|
| ROL-01 | X | Student calls `POST /invitations` | 403 | FR-03 AC-03.2 | Planned |
| ROL-02 | X | Teacher calls `POST /invitations/accept` | 403 | FR-04 AC-04.2 | Planned |
| ROL-03 | X | Student calls `GET /teachers/me/students`; teacher calls `GET /students/me/teachers` | 403 each | FR-05 AC-05.2 | Planned |
| ROL-04 | X | Student calls `POST /availability` | 403 | FR-06 AC-06.3 | Planned |
| ROL-05 | X | Teacher calls `POST /bookings` | 403 | FR-09 AC-09.2 | Planned |
| ROL-06 | X | Student sends status `approved` | 403 | FR-10 AC-10.2 | Planned |
| ROL-07 | X | Student calls `POST /assignments` | 403 | FR-13 AC-13.3 | Planned |
| ROL-08 | X | Every protected operation with no token, a malformed token and an expired token | 401 | FR-02 AC-02.3 | Planned (done for `/users/me`) |
| ROL-09 | X | Body field that names another owner (for example `teacherId` on `POST /availability`) | 400; identity always comes from the token | BR-01, FR-06 AC-06.1 | Planned |
| ROL-10 | X | Cross-account matrix: 2 teachers x 2 students (one connected pair each) against every resource | 0 cross-account successes | BR-01 | Planned |

### 4.5 Connections (FR-03, FR-04, FR-05)

| ID | Type | Case | Expected | Requirement | Story | Status |
|---|---|---|---|---|---|---|
| INV-01 | N | Teacher invites a student e-mail | 201; code and `expiresAt` | FR-03 AC-03.1 | US-03 / #17 | Planned |
| INV-02 | X | E-mail missing or malformed | 400 | FR-03 AC-03.2 | US-03 / #17 | Planned |
| INV-03 | X | Student is already connected | 409; no second relationship | FR-03 AC-03.3 | US-03 / #17 | Planned |
| INV-04 | B | `expiresAt` minus creation time | 7 days (within 5 s) | FR-03 AC-03.1 | US-03 / #17 | Planned |
| INV-05 | X | Second active invitation to the same e-mail | Not specified; record the observed result and report it as a specification gap | FR-03 | US-03 / #17 | Planned |
| ACC-01 | N | Student with the matching e-mail accepts a valid code | 201; one relationship; role unchanged | FR-04 AC-04.1, AC-04.4 | US-04 / #18 | Planned |
| ACC-02 | X | Code used a second time | 409 | FR-04 AC-04.3 | US-04 / #18 | Planned |
| ACC-03 | B | Code at the moment `expiresAt` is reached | 409 | FR-04 AC-04.4 | US-04 / #18 | Planned |
| ACC-04 | X | Unknown code | 404 | FR-04 AC-04.2 | US-04 / #18 | Planned |
| ACC-05 | X | Missing code, or a code shorter than 16 characters | 400 | FR-04 AC-04.2 | US-04 / #18 | Planned |
| ACC-06 | X | Code for another student's e-mail | 403 | FR-04 AC-04.2 | US-04 / #18 | Planned |
| ACC-07 | X | Two simultaneous accepts of one code | One 201, one 409; one relationship | FR-04 AC-04.3 | US-04 / #18 | Planned |
| LST-01 | N | Teacher lists students; student lists teachers | 200; own connections only, ordered by name, no secret fields | FR-05 AC-05.1, AC-05.3 | US-05 / #19 | Planned |
| LST-02 | B | No connections | 200 with an empty list | FR-05 AC-05.1 | US-05 / #19 | Planned |
| LST-03 | B | 201 connections seeded | 200 with exactly 200 items | FR-05 AC-05.3, BR-10 | US-05 / #19 | Planned |

### 4.6 Availability and lessons (FR-06 to FR-12)

| ID | Type | Case | Expected | Requirement | Story | Status |
|---|---|---|---|---|---|---|
| AVL-01 | N | Teacher publishes a future slot with a timezone offset | 201; owner from the token | FR-06 AC-06.1 | US-06 / #20 | Planned |
| AVL-02 | X | Malformed, offset-free, past or reversed interval (each separately) | 400 | FR-06 AC-06.2 | US-06 / #20 | Planned |
| AVL-03 | X | Overlap with the teacher's own slot | 409 | FR-06 AC-06.2 | US-06 / #20 | Planned |
| AVL-04 | B | Slot that starts exactly when another ends | 201 | FR-06 AC-06.3, BR-05 | US-06 / #20 | Planned |
| AVL-05 | N | Connected student views the teacher's slots | 200; future slots, no approved overlap, ordered by start | FR-07 AC-07.1 | US-07 / #21 | Planned |
| AVL-06 | N | A pending request exists for a slot | Slot is still listed | FR-07 AC-07.2 | US-07 / #21 | Planned |
| AVL-07 | B | No matching slots | 200 with an empty list | FR-07 AC-07.2 | US-07 / #21 | Planned |
| AVL-08 | X | `teacherId` missing or invalid; unknown teacher; unconnected student | 400; 404; 403 | FR-07 AC-07.3 | US-07 / #21 | Planned |
| AVL-09 | B | `from` equal to or after `to`; slot ending exactly at `from`; slot starting exactly at `to` | 400; excluded; excluded | FR-07 AC-07.4, BR-06 | US-07 / #21 | Planned |
| AVL-10 | N | Owner deletes a slot with no active booking | 204, no body | FR-08 AC-08.1 | US-08 / #22 | Planned |
| AVL-11 | X | Delete a slot with a pending or approved booking | 409; slot unchanged | FR-08 AC-08.2 | US-08 / #22 | Planned |
| AVL-12 | X | Wrong owner; unknown slot; malformed id; student | 403; 404; 400; 403 | FR-08 AC-08.3 | US-08 / #22 | Planned |
| BKG-01 | N | Connected student requests a future slot | 201; `pending`; slot times and teacher copied; client-supplied values rejected or ignored | FR-09 AC-09.1 | US-09 / #23 | Planned |
| BKG-02 | X | Unconnected student; malformed input; unknown slot | 403; 400; 404 | FR-09 AC-09.2 | US-09 / #23 | Planned |
| BKG-03 | X | Same student requests the same slot twice | 409; one booking | FR-09 AC-09.3 | US-09 / #23 | Planned |
| BKG-04 | N | Two different students request the same slot | Both 201 (pending does not reserve) | FR-09 AC-09.3, BR-07 | US-09 / #23 | Planned |
| BKG-05 | X | Request for a slot whose start has passed | Not specified (400 or 409); record the observed result | FR-09 | US-09 / #23 | Planned |
| BKG-06 | N | Owning teacher approves; owning teacher rejects | 200 with the updated booking | FR-10 AC-10.1 | US-10 / #24 | Planned |
| BKG-07 | X | Wrong teacher; unknown booking; invalid status value; transition from a terminal state | 403; 404; 400; 409 | FR-10 AC-10.2 | US-10 / #24 | Planned |
| BKG-08 | X | Approve a booking that overlaps an approved lesson | 409 | FR-10 AC-10.4, BR-05 | US-10 / #24 | Planned |
| BKG-09 | B | Approve a booking that starts exactly when an approved lesson ends | 200 | FR-10 AC-10.4 | US-10 / #24 | Planned |
| BKG-10 | X | 10 simultaneous approvals of overlapping requests, 100 rounds | Exactly one 200 per round, others 409; one approved lesson | FR-10 AC-10.3 | US-10 / #24 | Planned |
| BKG-11 | X | Approve a pending request whose start has passed | Not specified; record the observed result | FR-10 | US-10 / #24 | Planned |
| BKG-12 | N | User lists lessons | 200; only own bookings, ordered by start, at most 200 | FR-11 AC-11.1, AC-11.3 | US-11 / #25 | Planned |
| BKG-13 | X | Invalid `status`, `from` after `to`, offset-free dates | 400 | FR-11 AC-11.2 | US-11 / #25 | Planned |
| BKG-14 | B | No bookings | 200 with an empty list | FR-11 AC-11.1 | US-11 / #25 | Planned |
| BKG-15 | N | Student and teacher each cancel a pending or approved lesson before it starts | 200; `cancelled` | FR-12 AC-12.1 | US-12 / #26 | Planned |
| BKG-16 | B | Cancel one second before `startTime`; cancel exactly at `startTime` | 200; 409 | FR-12 AC-12.1, AC-12.2 | US-12 / #26 | Planned |
| BKG-17 | X | Cancel a terminal booking; unrelated user; unknown id; malformed input | 409; 403; 404; 400 | FR-12 AC-12.2 | US-12 / #26 | Planned |
| BKG-18 | N | After cancellation, delete the slot and approve another overlapping request | Both succeed | FR-12 AC-12.3 | US-12 / #26 | Planned |

### 4.7 Assignments (FR-13, FR-14)

| ID | Type | Case | Expected | Requirement | Story | Status |
|---|---|---|---|---|---|---|
| ASG-01 | N | Teacher uploads a PDF, a JPEG and a PNG to a connected student | 201 each | FR-13 AC-13.1, AC-13.2 | US-13 / #27 | Planned |
| ASG-02 | B | Title of 1, 120 and 121 characters; instructions of 2000 and 2001 | 201, 201, 400; 201, 400 | FR-13 AC-13.1 | US-13 / #27 | Planned |
| ASG-03 | B | File of 10485760 bytes; file of 10485761 bytes | 201; 413 | FR-13 AC-13.2 | US-13 / #27 | Planned |
| ASG-04 | B | Empty (0-byte) file | Not specified (the OpenAPI schema requires at least 1 byte); record the observed result | FR-13 | US-13 / #27 | Planned |
| ASG-05 | X | Text file; executable renamed to `.pdf`; PNG content named `.exe` | 415 for unsupported actual content | FR-13 AC-13.2 | US-13 / #27 | Planned |
| ASG-06 | X | Student calls the endpoint; unconnected student; required field missing; unknown student | 403; 403; 400; 404 | FR-13 AC-13.3 | US-13 / #27 | Planned |
| ASG-07 | X | Filename with path separators or `..`; fetch the stored file by a static URL | Name sanitized; static URL returns 404; response has no public path | FR-13 AC-13.4 | US-13 / #27 | Planned |
| ASG-08 | X | Upload rejected with 413 or 415 | No metadata row and no stored file remain | BR-11 | US-13 / #27 | Planned |
| ASG-09 | N | Teacher lists; student lists | Own assignments only, newest first, at most 200; empty list returns 200 | FR-14 AC-14.1 | US-14 / #28 | Planned |
| ASG-10 | N | Creating teacher and assigned student read details and download | 200; actual media type; safe `Content-Disposition`; no storage path | FR-14 AC-14.2, AC-14.3 | US-14 / #28 | Planned |
| ASG-11 | X | Unrelated student; other teacher; connected but non-assigned student | 403 on metadata and file | FR-14 AC-14.2 | US-14 / #28 | Planned |
| ASG-12 | X | Unknown id; malformed id; no token | 404; 400; 401 | FR-14 AC-14.2 | US-14 / #28 | Planned |

### 4.8 Observations from the executed run (no expected value in the SRS)

| ID | Observation | Related NFR |
|---|---|---|
| O-01 | A second login for the same user invalidates the earlier token: first token 401, second 200 | SEC-01, OD-02 |
| O-02 | `POST /api/v1/users/me` returns a JSON 404 | REL-03 |
| O-03 | `GET /api/v1/auth/login` returns an HTML 404 | REL-03 |
| O-04 | `Access-Control-Allow-Origin: *` is sent on API responses | SEC-02 |
| O-05 | 12 consecutive wrong passwords for one account all returned 401 | SEC-10 |
| O-06 | `GET /server.py` returned 200; `GET /tutorbridge.db`, `/../data/tutorbridge.db` and the encoded form returned 404 | SEC-09 |
| P-02 | A 3 MiB request body was read in full and then rejected by field validation (400) | REL-03 |
| P-01 | Non-numeric `Content-Length`: no response, unhandled `ValueError`. Expected 400. Fixed in PR #79; at `7fccc47` it returns 400 on register and login. | REL-03, Issue #71 |

### 4.9 Interface and prototype checks (browser or Figma needed)

| ID | Type | Case | Expected | Requirement | Status |
|---|---|---|---|---|---|
| UI-01 | N | Log in as a teacher and as a student | Each lands on their own entry screen | FR-02 AC-02.4, FR-15 AC-15.3 | Fail in a browser (F-2): a teacher and a student both land on `/main_page.html`, a student-information (OBS) sample dashboard; after the user's name is replaced, 2 of 77 text lines differ |
| UI-02 | X | Read the login and registration password messages | Both state 12 characters | BR-02 | Pass in a browser: registration says 12 characters; login states no minimum (empty: "&#350;ifrenizi girin.", wrong: "E-posta veya şifre hatalı.") |
| UI-03 | N | Complete login and registration using only the keyboard | Logical Tab order, visible focus, Enter submits | NFR USE-03 | Pass in a browser: login has 8 Tab stops in logical order, register has 13 plus the radio group; every stop is `:focus-visible` and changes style on focus; keyboard-only login (type, Tab twice past the "forgot password" link, type, Enter) succeeded. Choosing an option with the arrow keys inside the radio group was not tested |
| UI-04 | X | Trigger validation errors with a screen reader or the accessibility tree | Message text is announced | NFR USE-03 | Fail in a browser (F-3): no live region or `role` on the message; the password input has `aria-invalid="false"` and no `aria-describedby` after a server-side error. Not tested with a screen reader |
| UI-05 | N | Check that all form fields have labels | Every input has a label | NFR USE-03 | Pass in a browser: the accessibility tree gives every input reached by Tab an accessible name (for example "E-posta adresi", "&#350;ifre", "Beni hatırla", "Ad", "Soyad"). No automated accessibility scan was run |
| UI-06 | X | Open the dashboard with an expired token | Redirect to the login page | FR-02 AC-02.3 | Pass in a browser: the dashboard redirected to `/login.html` and the token was removed from `localStorage` |
| UI-07 | N | Review the Figma prototype for error, empty, loading and success states on the three required journeys | No journey step without its applicable state | BR-12, NFR USE-02 | Partly reviewed from the repository exports (10 of 37 PNGs viewed, all 37 hash-compared); findings in F-6 / Issue #76. The text of the states named in the handoff was found in the local `.fig` backup (strings only; layout and connections not checked). Planned for the live Figma file, which was not opened |
| UI-08 | N | Student requests a lesson in the prototype | At least 80% of 5 or more participants finish within 120 s without help | SRS section 7, NFR USE-01 | Planned. No session held |
| UI-09 | X | Submit the registration form empty, with a short password and a mismatching confirmation, and with an e-mail that already exists | One message per problem; the password message states the 12-character rule | FR-01 AC-01.3, BR-02 | Pass in a browser: seven field messages when empty; "&#350;ifre en az 12 karakter olmalıdır."; "&#350;ifreler eşleşmiyor."; "Bu e-posta zaten kayıtlı." |
| UI-10 | N | Open `/main_page.html` with no token | Not specified for the static dashboard (SRS BR-01 covers API operations) | BR-12 | Observation: the page stays open and shows sample content with a banner that it is not connected to real data; there is no redirect to login |
| UI-11 | N | Log in as each role and check where the access token is kept | Not specified; recorded for the security discussion | NFR SEC-01 | Observation: the token is stored in `localStorage` for both roles; no console or page errors on the dashboards |

## 5. Requirement coverage

Every functional requirement has at least one case. "Executed" counts cases with status Pass, Fail, Expected failure or Observation.

| FR | Cases | Executed |
|---|---|---|
| FR-01 | R-01 to R-27 | Yes |
| FR-02 | L-01 to L-08, T-03 to T-10, ROL-08, UI-01, UI-06 | Yes |
| FR-03 | INV-01 to INV-05, ROL-01 | No |
| FR-04 | ACC-01 to ACC-07, ROL-02 | No |
| FR-05 | LST-01 to LST-03, ROL-03 | No |
| FR-06 | AVL-01 to AVL-04, ROL-04, ROL-09 | No |
| FR-07 | AVL-05 to AVL-09 | No |
| FR-08 | AVL-10 to AVL-12 | No |
| FR-09 | BKG-01 to BKG-05, ROL-05 | No |
| FR-10 | BKG-06 to BKG-11, ROL-06 | No |
| FR-11 | BKG-12 to BKG-14 | No |
| FR-12 | BKG-15 to BKG-18 | No |
| FR-13 | ASG-01 to ASG-08, ROL-07 | No |
| FR-14 | ASG-09 to ASG-12 | No |
| FR-15 | T-01, T-02, T-04, T-05, T-08, UI-01 | Yes |

Executed requirements: 3 of 15 (FR-01, FR-02, FR-15). The other 12 are Planned because their endpoints do not exist yet.

## 6. Specification gaps found while writing the plan

These cases have no expected value in the SRS or OpenAPI. The Product Owner (Toprak) decides each answer; the plan records the observed behavior once the feature exists.

- INV-05: behavior of a second active invitation to the same e-mail.
- BKG-05: status code for a lesson request on a slot whose start has already passed, and what "active request" means in AC-09.3.
- BKG-11: whether a teacher may approve a pending request whose start has passed.
- ASG-04: how a 0-byte file is handled.

## 7. Hand-off to CI

- The QA suite `tests/test_auth_quality.py` should run inside the existing "Sprint 2 document and hygiene checks" job, because that job already runs `python -m unittest discover -s tests`. CI confirms it: the log of the Sprint 2 validation run for `develop` at `7fccc47` (`ubuntu-26.04`) lists the QA tests, including P-01, and ends with "Ran 42 tests ... OK". The DevOps owner has since renamed the step to "Python unittest suite (auth API, QA, and delivery tooling)". This plan does not edit the workflow.
- P-01 was an expected failure until #71 was fixed; PR #79 turned it into a normal test, so no expected-failure marker remains.
- Not suitable for CI yet: the browser checks, the real one-hour wait (T-09), the Figma review and the usability session.

## 8. Limits of this plan

- Only the registration, login and profile cases were executed. The remaining cases describe expected behavior and are not results.
- The executed results are local API checks against the Python handler and a headless Chromium run of the login and registration pages. No real desktop browser, assistive technology, live Figma file or end-to-end run is included.
- Coverage was not measured; the 50% unit-test coverage target belongs to Sprint 3.
- Re-run the QA suite after any change to `src/server.py`.

References: [SRS](SRS.md), [NFR and Quality Measures](NFR-and-Quality-Measures.md), [OpenAPI draft](../Openapi.yaml), [backlog](../Initial-Product-Backlog.md), [Verification Report](Verification-Report.md), [UI-UX](UI-UX.md).
