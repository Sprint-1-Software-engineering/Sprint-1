# TutorBridge - Software Requirements Specification

Version: 0.2 draft, 19 November 2026. Owner: Toprak Daldal (Product / Requirements).
Review state: prepared for technical and quality peer review; no team or stakeholder approval is claimed.
Tracking: [requirements task #59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59).

## 1. Purpose, evidence and scope

TutorBridge helps private tutors coordinate lessons and share homework with their existing students. This SRS refines the Sprint 1 product scope into verifiable requirements for later implementation. The Sprint 2 deliverable is requirements and design; it is not a claim that the complete MVP runs.

The team reported one conversation on 3 November 2026 with an anonymous tutor who teaches mathematics and software. The tutor arranges lesson times through WhatsApp, teaches through Google Meet and sends homework individually through WhatsApp. Manual coordination and organizing these messages were reported problems; willingness to use the proposed system was reported. Frequency, time cost and actual adoption were not measured. No new interview or usability result is claimed in this revision. See the [original evidence](../Project-Proposal-and-System-Vision.md) and the [future validation guide](Stakeholder-Validation-Guide.md).

Included: teacher/student accounts; invitation-based connections; teacher availability; lesson requests, decisions, calendars and permitted cancellation; assignment upload, listing, detail and protected download; own-profile retrieval for role-specific entry.

Excluded: AI question generation, parent accounts, teacher discovery/marketplace, payments, university OBS administration, grades/transcripts, integrated chat/video, external calendar sync, native mobile apps, analytics, homework submission and academic feedback. Google Meet remains an outside lesson tool with no runtime integration.

## 2. Actors and operating assumptions

| Actor | Responsibility and access |
|---|---|
| Teacher | Invite current students, view own connections, publish own availability, decide own requests, view/cancel own lessons and share assignments with connected students. |
| Student | Accept an invitation addressed to own email, view connected teachers, request their slots, view/cancel own lessons and read assigned homework. |
| Team/operator | Maintain the application and its configuration. No administrative product account or academic powers are implied by this role. |
| Course reviewers | Inspect artifacts and engineering evidence; they are not application users by default. |

A registered account has one stored role, teacher or student. Role changes and account editing/deletion are outside the MVP. A student may connect to multiple teachers; each teacher may connect to multiple students. Users have a browser and internet access. Teachers bring existing students; public discovery is not required. Test data is synthetic or authorized. Initial per-user lists are small; the contract caps list responses at 200 items. The team must decide how to handle larger datasets before exceeding that assumption (OD-07).

The target uses a browser client, an HTTP API under one selected base URL, database records and protected file storage. Backend technology, hosting and token format remain architecture decisions in section 9. Their unresolved state does not change the functional behavior below.

## 3. Shared business and interface rules

- **BR-01 - Authentication and ownership.** All operations except registration/login require an unexpired bearer session. Authenticate, then check stored role, connection and record ownership on the server. Caller-supplied identity cannot grant access. Registration, profile and domain responses expose no password, hash or session secret; login returns its bearer token only to the successful caller. No homework response exposes an unrestricted storage URL.
- **BR-02 - Account input.** JSON fields retain their declared types; null or an object is not coerced to a valid string. Trim names/email and normalize email case for uniqueness. Name: 1-100 non-blank characters; email: valid email format, at most 254 characters; password: 12-128 characters. Only teacher/student roles are accepted. Required/unknown request fields follow the contract schemas.
- **BR-03 - Invitations.** A code is single-use, bound to a student email and expires seven days after creation. At now >= expiresAt it is expired. Relationship creation and code consumption are atomic. Sharing happens outside the app; no email provider is required.
- **BR-04 - Time.** API date-times include timezone offsets; store instants in UTC and display a consistent local time to users. Reject malformed/offset-free/reversed intervals. New availability and requests refer to future starts. Use the server clock for expiry, start and cancellation checks.
- **BR-05 - Overlap.** Intervals are half-open. A overlaps B when A.start < B.end and A.end > B.start. Adjacent intervals are allowed. Teacher availability cannot overlap the same teacher availability. Teacher approvals cannot overlap the same teacher approved lessons; student conflicts across different teachers are unresolved in OD-06.
- **BR-06 - Date filters.** If both from/to exist, require from < to; supplied values have offsets. A booking/availability interval matches when its end > from (if supplied) and its start < to (if supplied). Missing bounds are open. Availability still excludes past starts and approved-overlapping slots. Calendar queries may include past lessons.
- **BR-07 - Requests and approval.** A request starts pending, uses its slot's stored owner/times and does not reserve the slot exclusively. Duplicate active requests from the same student for the same slot return 409. Approval rechecks conflicts in one transaction; a stale client view does not guarantee approval.
- **BR-08 - Cancellation and deletion.** Either participant may cancel pending/approved lessons strictly before startTime. Rejected/cancelled are terminal. Slots with pending/approved bookings cannot be deleted; permitted bookings must be cancelled first.
- **BR-09 - Files.** Accept actual PDF/JPEG/PNG content up to 10485760 bytes (10 MiB). Check content type, sanitize names and keep stored files outside public static paths. Authorize metadata and download independently; an opaque id does not replace authorization.
- **BR-10 - Lists.** Return only permitted records, at most 200 per response. Connections sort by name, slots/bookings by startTime and assignments newest first. Valid empty lists return 200, not an error. No pagination or full results above the cap are promised.
- **BR-11 - HTTP errors.** Use the operation's documented response codes and JSON {code, message}. 400: invalid input; 401: missing/invalid/expired credentials; 403: authenticated but forbidden; 404: missing referenced resource where documented; 409: duplicate/state/time conflict; 413/415: oversized/unsupported assignment. Failures must not leave a partially created domain record. Success bodies match the current OpenAPI schemas; 204 has no body.
- **BR-12 - Client behavior.** Identify the signed-in account from its profile, route by its stored role and provide visible success/error/empty/loading states. Demo data and unimplemented links must be identified. A static student OBS page is not evidence of teacher/student lesson and assignment workflows.

### Booking state transitions

| Current | Requested | Authorized actor | Condition/result |
|---|---|---|---|
| pending | approved | Owning teacher | Atomic conflict/availability recheck; 200 or 409. |
| pending | rejected | Owning teacher | Own pending request; 200. |
| pending / approved | cancelled | Either participant | Strictly before startTime; 200, otherwise 409. |
| rejected / cancelled | any supported target | Participant | Terminal state; 409. |
| any | any | Unrelated user | 403 before permitting a transition. |

Other transitions are invalid. A malformed status value returns 400; an otherwise valid but disallowed transition returns 409.

## 4. Functional requirements

Each FR maps to an existing product story or the explicitly proposed profile story. Actor, precondition, trigger and acceptance criteria define its behavior; shared rules also apply. Acceptance criteria are requirements, not passed test results.

<a id="fr-01"></a>
### FR-01: Register an account

Actor: Teacher or student.
Precondition: No account exists for the supplied email.
Trigger: Submit a registration form.
Story: [US-01 / #15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15). Owner: Mehmet Ali Demircioğlu.
Contract operation(s): `POST /auth/register`.

- **AC-01.1:** Given a string name (1-100 non-blank characters), a valid email (at most 254 characters), a string password (12-128 characters) and teacher/student role, registration creates one account and returns 201 with id, name, email and role only.
- **AC-01.2:** Given an email already registered after trimming and case normalization, registration returns 409 and does not create a second account.
- **AC-01.3:** Given missing, null, wrong-type or invalid input, registration returns 400 and creates no account. Unknown request properties are rejected according to the contract.
- **AC-01.4:** The password is stored as a salted hash; plaintext passwords, hashes and session secrets are absent from registration responses.

<a id="fr-02"></a>
### FR-02: Sign in

Actor: Registered user.
Precondition: The account exists.
Trigger: Submit email and password.
Story: [US-02 / #16](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16). Owner: Mehmet Ali Demircioğlu.
Contract operation(s): `POST /auth/login`.

- **AC-02.1:** Valid credentials return 200 with a bearer accessToken, tokenType Bearer and expiresIn 3600; the token identifies the account and its stored role.
- **AC-02.2:** Incorrect credentials return generic 401 without identifying which credential was wrong; malformed input returns 400.
- **AC-02.3:** Protected operations reject missing, malformed, unknown and expired credentials with 401. The session is invalid at its expiry time.
- **AC-02.4:** The client uses the authenticated profile to select the teacher or student journey; neither role is silently treated as the other. This UI requirement remains unaccepted in PR #58.

<a id="fr-03"></a>
### FR-03: Invite an existing student

Actor: Teacher.
Precondition: The teacher is authenticated; the intended student is an existing real-world student.
Trigger: Submit the student email.
Story: [US-03 / #17](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17). Owner: Toprak Daldal.
Contract operation(s): `POST /invitations`.

- **AC-03.1:** A teacher creates an email-bound, single-use invitation and receives 201 with code and expiry. The code expires seven days after creation.
- **AC-03.2:** An authenticated student attempting to create an invitation receives 403; missing/invalid email receives 400.
- **AC-03.3:** An already connected student email returns 409 instead of creating a duplicate relationship.
- **AC-03.4:** The teacher shares the code outside TutorBridge. Automatic email delivery is not required by this release.

<a id="fr-04"></a>
### FR-04: Accept a teacher invitation

Actor: Student.
Precondition: The student has an authenticated account and an invitation code.
Trigger: Submit the invitation code.
Story: [US-04 / #18](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18). Owner: Toprak Daldal.
Contract operation(s): `POST /invitations/accept`.

- **AC-04.1:** A valid, unused, unexpired code for the signed-in student email creates one teacher-student relationship and returns 201. Consuming the code and creating the relationship are atomic.
- **AC-04.2:** A mismatched student email or wrong role returns 403; unknown code returns 404; malformed/missing code returns 400.
- **AC-04.3:** Expired, already used or duplicate-relationship invitations return 409. Two simultaneous uses cannot create duplicate relationships.
- **AC-04.4:** A code is expired when server time reaches expiresAt. Invitations do not change the account role.

<a id="fr-05"></a>
### FR-05: View my connections

Actor: Teacher or student.
Precondition: The user is authenticated.
Trigger: Open the connections list.
Story: [US-05 / #19](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19). Owner: Arda Demir.
Contract operation(s): `GET /teachers/me/students; GET /students/me/teachers`.

- **AC-05.1:** A teacher receives only their connected students from the teacher-only operation; a student receives only their connected teachers from the student-only operation. A valid empty list returns 200.
- **AC-05.2:** Calling the other role-only list returns 403; missing/invalid credentials return 401.
- **AC-05.3:** Results are ordered by name and contain at most 200 items. They contain no password, token or other account secret.

<a id="fr-06"></a>
### FR-06: Publish availability

Actor: Teacher.
Precondition: The teacher is authenticated.
Trigger: Submit a startTime and endTime for availability.
Story: [US-06 / #20](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20). Owner: Osman Berke Özdemir.
Contract operation(s): `POST /availability`.

- **AC-06.1:** A future interval with explicit timezone offsets and endTime after startTime returns 201. Teacher identity is taken from the session, not a caller-supplied owner.
- **AC-06.2:** Malformed, missing-offset, past or reversed intervals return 400. Overlap with the same teacher availability returns 409.
- **AC-06.3:** An authenticated student receives 403. Adjacent intervals are permitted: one may end exactly when the next starts.

<a id="fr-07"></a>
### FR-07: View teacher availability

Actor: Connected student or owning teacher.
Precondition: The user is authenticated; a student is connected to the queried teacher.
Trigger: Request teacher availability, optionally with date filters.
Story: [US-07 / #21](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21). Owner: Arda Demir.
Contract operation(s): `GET /availability`.

- **AC-07.1:** A valid teacherId returns future slots for that teacher without overlaps with approved lessons, ordered by startTime and limited to 200 items. The teacher may query self; a student may query a connected teacher.
- **AC-07.2:** Pending requests do not hide the slot. No matching slots returns 200 with an empty list.
- **AC-07.3:** Missing/invalid teacherId or invalid date ranges return 400; unknown teacher returns 404; unrelated students or other unauthorized role/owner combinations return 403.
- **AC-07.4:** If date filters are supplied, apply the common half-open overlap rule in BR-06. Dates include offsets.

<a id="fr-08"></a>
### FR-08: Remove an unused slot

Actor: Teacher.
Precondition: The teacher owns the referenced availability slot.
Trigger: Request removal of the slot.
Story: [US-08 / #22](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22). Owner: Osman Berke Özdemir.
Contract operation(s): `DELETE /availability/{id}`.

- **AC-08.1:** The owner removes a slot without pending or approved bookings and receives 204 with no response body.
- **AC-08.2:** A slot with a pending or approved booking returns 409 and remains unchanged; cancel permitted bookings first.
- **AC-08.3:** Wrong owner returns 403, unknown slot 404 and malformed id 400. Student accounts cannot delete teacher slots.

<a id="fr-09"></a>
### FR-09: Request a lesson

Actor: Connected student.
Precondition: The authenticated student is connected to the owner of a future availability slot.
Trigger: Request the selected availabilityId.
Story: [US-09 / #23](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23). Owner: Mehmet Ali Demircioğlu.
Contract operation(s): `POST /bookings`.

- **AC-09.1:** A valid request returns 201 with status pending and copies the selected slot times and teacher identity; the student cannot override these fields.
- **AC-09.2:** No teacher-student relationship or wrong role returns 403; malformed input returns 400; unknown slot returns 404.
- **AC-09.3:** A duplicate active request for the same student/slot, or an unavailable/approved-overlapping slot, returns 409. Pending requests alone do not reserve the slot.
- **AC-09.4:** An input/time conflict creates no extra booking. Cross-teacher student clashes remain an explicit decision in OD-06; this criterion does not claim their prevention.

<a id="fr-10"></a>
### FR-10: Approve or reject a lesson

Actor: Owning teacher.
Precondition: The authenticated teacher owns a pending booking.
Trigger: Submit approved or rejected as the new status.
Story: [US-10 / #24](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24). Owner: Mehmet Ali Demircioğlu.
Contract operation(s): `PATCH /bookings/{id}/status`.

- **AC-10.1:** The owning teacher changes their pending booking to approved or rejected and receives 200 with the updated booking.
- **AC-10.2:** Wrong owner/role returns 403, unknown booking 404 and invalid status/input 400. Invalid or terminal transitions return 409.
- **AC-10.3:** Approval rechecks availability and all overlapping approved lessons for the teacher in one atomic transaction. Concurrent conflicting approvals produce at most one approved lesson; the conflicting request receives 409.
- **AC-10.4:** Overlap means start < otherEnd and end > otherStart. Adjacent lessons are allowed. The rule is checked at approval time, not only when the request is created.

<a id="fr-11"></a>
### FR-11: View my lesson calendar

Actor: Teacher or student.
Precondition: The user is authenticated.
Trigger: Open the personal lesson list/calendar.
Story: [US-11 / #25](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25). Owner: Kemal Efe Bilgisiçok.
Contract operation(s): `GET /bookings`.

- **AC-11.1:** The user receives only bookings in which they are the teacher or student, with current states, ordered by startTime; empty results return 200.
- **AC-11.2:** Optional from/to filters select intervals by BR-06. Optional status accepts only pending, approved, rejected or cancelled; invalid filters return 400.
- **AC-11.3:** Results contain at most 200 items. Unrelated users cannot obtain another participant list by supplying their identity; ownership is session-derived.

<a id="fr-12"></a>
### FR-12: Cancel a permitted lesson

Actor: Booking participant.
Precondition: The user is the booking teacher or student.
Trigger: Request status cancelled.
Story: [US-12 / #26](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26). Owner: Osman Berke Özdemir.
Contract operation(s): `PATCH /bookings/{id}/status`.

- **AC-12.1:** Either participant can cancel their pending or approved booking strictly before startTime; the operation returns 200 with status cancelled.
- **AC-12.2:** An unrelated user returns 403. A terminal booking or a booking whose startTime has been reached returns 409; unknown id returns 404 and malformed input returns 400.
- **AC-12.3:** Rejected and cancelled are terminal states. A cancelled booking no longer blocks future approval or slot removal under the common rules.

<a id="fr-13"></a>
### FR-13: Assign a homework file

Actor: Teacher.
Precondition: The authenticated teacher is connected to the target student.
Trigger: Submit studentId, title, optional instructions and an assignment file.
Story: [US-13 / #27](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27). Owner: Kemal Efe Bilgisiçok.
Contract operation(s): `POST /assignments`.

- **AC-13.1:** A valid multipart upload returns 201 for the connected student. Title is 1-120 characters; optional instructions are at most 2000 characters.
- **AC-13.2:** PDF, JPEG or PNG files of at most 10 MiB (10485760 bytes) are accepted; larger files return 413 and unsupported actual types return 415. Actual content is checked, not only the extension.
- **AC-13.3:** Wrong role or an unconnected student returns 403; invalid required fields return 400 and unknown referenced student returns 404.
- **AC-13.4:** Filenames are sanitized and files are stored outside public static paths. Responses expose protected metadata, not an unrestricted public storage URL.

<a id="fr-14"></a>
### FR-14: Read my assignments

Actor: Creating teacher or assigned student.
Precondition: The user is authenticated and is entitled to the requested assignment.
Trigger: List assignments, open details or download a file.
Story: [US-14 / #28](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28). Owner: Kemal Efe Bilgisiçok.
Contract operation(s): `GET /assignments; GET /assignments/{id}; GET /assignments/{id}/file`.

- **AC-14.1:** The teacher sees own created assignments and the student sees assignments addressed to them; list results are newest first, at most 200 items, with 200 and an empty list when appropriate.
- **AC-14.2:** Only the creating teacher or assigned student can read details and download the file. Unrelated users return 403; unknown assignment returns 404 and malformed id returns 400.
- **AC-14.3:** File download applies the same ownership check as metadata, uses the actual media type and a safe Content-Disposition filename, and never reveals a public storage path.
- **AC-14.4:** Student homework submission, grading and feedback are outside this first release; retrieving an assigned file does not submit work.

<a id="fr-15"></a>
### FR-15: Read my current profile

Actor: Teacher or student.
Precondition: The user has a valid authenticated session.
Trigger: Request the current profile to initialize the user journey.
Story: [US-15 / #60](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60). Owner: Mehmet Ali Demircioğlu.
Proposed operation: `GET /users/me` is defined in unmerged [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58); develop contract integration is tracked in [T-15 / #61](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61).

- **AC-15.1:** A valid session returns 200 with only the signed-in user id, name, email and teacher/student role, matching the User schema.
- **AC-15.2:** Missing, malformed, unknown or expired credentials return 401 and no profile. No password, hash or token is included in the profile.
- **AC-15.3:** Caller-supplied identity/role cannot select a different user. The stored role supports the correct teacher or student entry screen.
- **AC-15.4:** The proposed GET /users/me operation is integrated into the reviewed develop contract before this story can be accepted. PR #58 alone is not proof of integration or complete UI behavior.

## 5. Data requirements

Identifiers are UUIDs where declared by the OpenAPI schema. Ownership/relationship identifiers are derived or checked on the server. Client-side validation helps users but does not replace server validation.

| Concept | Required information and integrity |
|---|---|
| User | id, name, normalized unique email, stored teacher/student role; salted password hash stays private. Input bounds follow BR-02. |
| Session | User identity and one-hour expiry; precise representation/revocation decision is OD-02. Profile output never returns session secrets. |
| Invitation | id, teacherId, studentEmail, private code and expiresAt; single-use/relationship uniqueness is enforced atomically. |
| Relationship | teacherId/studentId pair is unique; it authorizes the relevant lesson and assignment operations. |
| Availability | id, owning teacherId, startTime/endTime; future, offset-aware, valid and non-overlapping for that teacher. |
| Booking | id, teacherId, studentId, availabilityId, copied times and pending/approved/rejected/cancelled status; valid state and conflict rules apply. |
| Assignment | id, teacherId, studentId, title, optional instructions and file metadata. Title is 1-120 characters and instructions at most 2000. |
| Protected file | Safe display filename, actual media type, byte size and private storage reference. A public file URL is not an authorized download mechanism. |

These are logical requirements, not a database migration or a claim that every table is implemented. Architecture owns primary/foreign-key and storage decisions. Retention/backup choices are OD-04; this SRS does not invent a legal retention period.

## 6. External interfaces and journeys

- **API:** the reviewed [OpenAPI draft](../Openapi.yaml) is the structural contract for its existing 16 operations. It covers request formats, fields, schemas, enums and declared responses. FR-15 adds a proposed 17th operation from PR #58; it is not silently treated as present in develop. SRS and contract conflicts must be resolved before affected story acceptance.
- **Browser:** role-specific teacher/student journeys initialize from the signed-in identity. Assignment upload is multipart; other declared request bodies are JSON. Protected file downloads use authorized API requests and safe response headers.
- **Outside systems:** WhatsApp/Google Meet are the tutor's outside workflow tools, not runtime dependencies. No calendar, AI, email, payment or university identity integration is required.
- **UX handoff:** Kemal owns the Figma prototype and Arda the cross-artifact/user-flow links. Required journeys are teacher invite -> student accept; teacher publishes slot -> student requests -> teacher decides; teacher assigns -> student accesses. Include forbidden/conflict/empty/loading outcomes. No Figma artifact is claimed complete here.

## 7. Existing quality constraints and handoffs

These inherited product constraints remain applicable: one-hour credential expiry; private record/file access; atomic teacher-conflict protection; type/size-limited uploads; HTTPS outside local development. The initial usability target is for a logged-in, connected student to request a lesson within two minutes in a prototype task. It is an unmeasured target, not a finding.

Berat owns the separate Sprint 2 NFR and quality-measure specification: measurable thresholds, method, environment/load, owner and status. Osman owns repeatable environment/CI/deployment documentation. This SRS does not claim either work is completed, set an unapproved production availability target or represent document validation as runtime coverage.

## 8. Implementation evidence and verification boundary

Baseline reviewed for refinement: develop 1e50523cda7b06ece5b5be4927353390c4aab562 and unmerged PR #58 at 7f3fa7735987dc59bc54be5257f9e2145c529a1c (19 November 2026).

PR #58 contains local Python/SQLite registration, login and profile code, plus static sample student dashboard content. An isolated review passed ten basic auth checks and reproduced two input failures: invalid@ email and JSON null name returned 201 rather than 400. Full browser behavior, teacher routing, Figma and the remaining domain operations are not accepted by that check. The bearer value is an opaque database-backed token although the old contract describes JWT; resolve OD-02.

US-01, US-02 and US-15 therefore remain partial/unaccepted. Other stories remain planned implementation. Every accepted story needs its listed positive/error/boundary criteria, real evidence, contract alignment and peer review; a document addition or a proposed estimate does not satisfy implementation acceptance.

## 9. Open decisions and assumptions to validate

| ID | Decision/question | Owner | Required before |
|---|---|---|---|
| OD-01 | Adopt the existing Python/SQLite direction or retain the earlier Node.js/Express plan; record rationale and one consistent environment/base URL. | Mehmet with Toprak and Osman | Architecture sign-off and environment integration. |
| OD-02 | JWT versus database-backed bearer sessions; login concurrency and logout/revocation semantics. Only the one-hour bearer behavior is fixed here. | Mehmet with Toprak | Auth contract/implementation acceptance. |
| OD-03 | Role-specific entry screens and handling of reset-password/remember-me placeholder controls. These extras are not committed MVP capabilities. | Toprak with Kemal and Mehmet | Prototype/auth acceptance. |
| OD-04 | Hosting, data/file retention and backup/recovery assumptions; no made-up deployment or policy result. | Osman with Mehmet | Deployment design sign-off. |
| OD-05 | Prototype feedback and measurements from an actual user; no new session has been reported for this revision. | Toprak with Kemal | Stakeholder validation claims. |
| OD-06 | Whether approved student lessons must also be non-overlapping across different teachers. Current baseline guarantees only teacher conflicts; any extension needs an explicit requirement/contract/test change. | Toprak with Mehmet and Berat | Booking design/implementation acceptance. |
| OD-07 | Behavior beyond the initial 200-item list cap, such as pagination; no completeness guarantee is implied above that capacity. | Toprak with Mehmet | Exceeding the initial dataset assumption. |

The following review also remains open: team confirmation of estimates/capacity. These are tracked questions, not approvals. New choices must update affected FRs, contract, backlog, prototype and tests together.

## 10. Functional traceability and acceptance

The table below is the requirements-side mapping. Arda's wider matrix will add real Figma, architecture and test artifact links when available. No missing artifact is replaced with an invented link.

| Requirement | Story / Issue | Contract operation(s) | Integration status |
|---|---|---|---|
| [FR-01](#fr-01) | [US-01 / #15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15) | `POST /auth/register` | Existing draft; runtime acceptance pending |
| [FR-02](#fr-02) | [US-02 / #16](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16) | `POST /auth/login` | Existing draft; runtime acceptance pending |
| [FR-03](#fr-03) | [US-03 / #17](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17) | `POST /invitations` | Existing draft; runtime acceptance pending |
| [FR-04](#fr-04) | [US-04 / #18](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18) | `POST /invitations/accept` | Existing draft; runtime acceptance pending |
| [FR-05](#fr-05) | [US-05 / #19](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19) | `GET /teachers/me/students; GET /students/me/teachers` | Existing draft; runtime acceptance pending |
| [FR-06](#fr-06) | [US-06 / #20](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20) | `POST /availability` | Existing draft; runtime acceptance pending |
| [FR-07](#fr-07) | [US-07 / #21](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21) | `GET /availability` | Existing draft; runtime acceptance pending |
| [FR-08](#fr-08) | [US-08 / #22](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22) | `DELETE /availability/{id}` | Existing draft; runtime acceptance pending |
| [FR-09](#fr-09) | [US-09 / #23](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) | `POST /bookings` | Existing draft; runtime acceptance pending |
| [FR-10](#fr-10) | [US-10 / #24](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24) | `PATCH /bookings/{id}/status` | Existing draft; runtime acceptance pending |
| [FR-11](#fr-11) | [US-11 / #25](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25) | `GET /bookings` | Existing draft; runtime acceptance pending |
| [FR-12](#fr-12) | [US-12 / #26](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26) | `PATCH /bookings/{id}/status` | Existing draft; runtime acceptance pending |
| [FR-13](#fr-13) | [US-13 / #27](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27) | `POST /assignments` | Existing draft; runtime acceptance pending |
| [FR-14](#fr-14) | [US-14 / #28](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28) | `GET /assignments; GET /assignments/{id}; GET /assignments/{id}/file` | Existing draft; runtime acceptance pending |
| [FR-15](#fr-15) | [US-15 / #60](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60) | `GET /users/me` | Proposed in #58; pending develop integration |

A requirement is ready for implementation when its actor/value, rules, acceptance criteria, dependencies and contract impact are clear and blocking decisions have owners. Implementation is done only after criteria pass with actual evidence, correct contract/UI behavior, checks and teammate review. Sprint 2 document review alone does not close the implementation stories.

References: [refined backlog](../Initial-Product-Backlog.md), [team/RACI](../Team-Members-and-RACI.md), [individual contributions](../../CONTRIBUTIONS.md), [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58), and the course Sprint 2 Teams announcement plus BM321 Semester Team Project Specification and Assessment Rubric supplied by the team.
