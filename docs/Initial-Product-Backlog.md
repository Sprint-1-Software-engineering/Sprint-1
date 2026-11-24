# TutorBridge Product Backlog - Sprint 2 Refinement

Owner: Toprak Daldal. Revision: 19 November 2026, prepared for peer review under [Issue #59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59).

This refines the original backlog; existing Epic/Feature/Story/Task identities remain intact. All estimates are proposals, not measured effort or confirmed team capacity. SP means story points; task hours are a separate initial planning estimate. The MVP scope is unchanged; a small own-profile story makes PR #58's extra operation traceable.

Implementation status is not Sprint 2 document status. US-01/02/15 have partial code in unmerged PR #58, not accepted functionality. The other stories are planned. No new interview, Figma prototype, full-system test or stakeholder approval is claimed. See [SRS](sprint-2/SRS.md) for detailed rules, acceptance IDs and open decisions; Arda owns the later cross-artifact matrix.

## Priority and estimates

High-priority work establishes identity/connections and the two core journeys. Slot removal and cancellation remain Medium. Order below is a proposed implementation order, not a Sprint 2 capacity commitment; prerequisites still govern parallel work. Team refinement/review is pending.

Roll-up: **45 SP** across 15 stories. T-01 through T-15 total **64 initial task hours**; do not add SP to hours. Existing 14 stories total 43 SP; proposed US-15 adds 2 SP. No estimate reduction or completion is claimed from partial code.

## Epics and Features

| Epic | Features | Priority | Story roll-up | Owner | Dependency |
|---|---|---|---|---|---|
| [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) Accounts and connections | [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9), [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) | High | 16 SP | Toprak Daldal | None |
| [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) Lesson scheduling | [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11), [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) | High | 21 SP | Toprak Daldal | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) |
| [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) Assignment sharing | [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13), [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) | High | 8 SP | Toprak Daldal | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) |

| Feature | Parent | Story roll-up | Planned owner | Child stories |
|---|---|---|---|---|
| [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) Accounts | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) | 8 SP | Mehmet Ali Demircioğlu | [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15), [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16), [US-15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60) |
| [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) Teacher-student connections | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) | 8 SP | Toprak Daldal | [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17), [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19) |
| [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) Availability | [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) | 7 SP | Osman Berke Özdemir | [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20), [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21), [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22) |
| [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) Booking lifecycle | [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) | 14 SP | Mehmet Ali Demircioğlu | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23), [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24), [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25), [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26) |
| [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) Assignment creation | [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) | 5 SP | Kemal Efe Bilgisiçok | [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27) |
| [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) Assignment access | [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) | 3 SP | Kemal Efe Bilgisiçok | [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28) |

Epic/Feature acceptance means all linked child criteria pass; their dependencies are the linked story prerequisites. Feature priority is High. These are planned implementation groupings, not completed Sprint 2 features.

## Proposed implementation order

| Order | Story | Priority | SP | Owner | Prerequisites | Status |
|---|---|---|---|---|---|---|
| 1 | [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15) Register an account | High | 3 | Mehmet Ali Demircioğlu | None | Auth code merged via PR #58/#79; QA evidence recorded; full story acceptance pending |
| 2 | [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16) Sign in | High | 3 | Mehmet Ali Demircioğlu | US-01 | Auth code merged via PR #58/#79; QA evidence recorded; full story acceptance pending |
| 3 | [US-15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60) Read my current profile | High | 2 | Mehmet Ali Demircioğlu | US-02 | Auth code merged via PR #58/#79; QA evidence recorded; full story acceptance pending |
| 4 | [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17) Invite an existing student | High | 3 | Toprak Daldal | US-02 | Planned implementation |
| 5 | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18) Accept a teacher invitation | High | 3 | Toprak Daldal | US-03 | Planned implementation |
| 6 | [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19) View my connections | High | 2 | Arda Demir | US-04 | Planned implementation |
| 7 | [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20) Publish availability | High | 3 | Osman Berke Özdemir | US-02 | Planned implementation |
| 8 | [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21) View teacher availability | High | 2 | Arda Demir | US-04, US-06 | Planned implementation |
| 9 | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) Request a lesson | High | 3 | Mehmet Ali Demircioğlu | US-04, US-07 | Planned implementation |
| 10 | [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24) Approve or reject a lesson | High | 5 | Mehmet Ali Demircioğlu | US-09 | Planned implementation |
| 11 | [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25) View my lesson calendar | High | 3 | Kemal Efe Bilgisiçok | US-09 | Planned implementation |
| 12 | [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27) Assign a homework file | High | 5 | Kemal Efe Bilgisiçok | US-04 | Planned implementation |
| 13 | [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28) Read my assignments | High | 3 | Kemal Efe Bilgisiçok | US-13 | Planned implementation |
| 14 | [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22) Remove an unused slot | Medium | 2 | Osman Berke Özdemir | US-06 | Planned implementation |
| 15 | [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26) Cancel a permitted lesson | Medium | 3 | Osman Berke Özdemir | US-09 | Planned implementation |

## Stories and Tasks

### [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15): Register an account
As a teacher or student, I want an account so that my records belong to me.

Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Owner: Mehmet Ali Demircioğlu · Priority: High · Order: 1 · 3 SP
Depends: None
Requirement: [FR-01](sprint-2/SRS.md#fr-01)
API: `POST /auth/register`
Status: Auth code merged via PR #58/#79; QA evidence recorded; full story acceptance pending.

Acceptance criteria (not passed results):
- **AC-01.1:** Given a string name (1-100 non-blank characters), a valid email (at most 254 characters), a string password (12-128 characters) and teacher/student role, registration creates one account and returns 201 with id, name, email and role only.
- **AC-01.2:** Given an email already registered after trimming and case normalization, registration returns 409 and does not create a second account.
- **AC-01.3:** Given missing, null, wrong-type or invalid input, registration returns 400 and creates no account. Unknown request properties are rejected according to the contract.
- **AC-01.4:** The password is stored as a salted hash; plaintext passwords, hashes and session secrets are absent from registration responses.

Task: [T-01 / #29](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/29), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16): Sign in
As a user, I want to sign in so that I can access my own records.

Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Owner: Mehmet Ali Demircioğlu · Priority: High · Order: 2 · 3 SP
Depends: [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15)
Requirement: [FR-02](sprint-2/SRS.md#fr-02)
API: `POST /auth/login`
Status: Auth code merged via PR #58/#79; QA evidence recorded; full story acceptance pending.

Acceptance criteria (not passed results):
- **AC-02.1:** Valid credentials return 200 with a bearer accessToken, tokenType Bearer and expiresIn 3600; the token identifies the account and its stored role.
- **AC-02.2:** Incorrect credentials return generic 401 without identifying which credential was wrong; malformed input returns 400.
- **AC-02.3:** Protected operations reject missing, malformed, unknown and expired credentials with 401. The session is invalid at its expiry time.
- **AC-02.4:** The client uses the authenticated profile to select the teacher or student journey; neither role is silently treated as the other. This UI requirement remains unaccepted in PR #58.

Task: [T-02 / #30](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/30), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17): Invite an existing student
As a teacher, I want to invite an existing student so that we can share lessons.

Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Owner: Toprak Daldal · Priority: High · Order: 4 · 3 SP
Depends: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
Requirement: [FR-03](sprint-2/SRS.md#fr-03)
API: `POST /invitations`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-03.1:** A teacher creates an email-bound, single-use invitation and receives 201 with code and expiry. The code expires seven days after creation.
- **AC-03.2:** An authenticated student attempting to create an invitation receives 403; missing/invalid email receives 400.
- **AC-03.3:** An already connected student email returns 409 instead of creating a duplicate relationship.
- **AC-03.4:** The teacher shares the code outside TutorBridge. Automatic email delivery is not required by this release.

Task: [T-03 / #31](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/31), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18): Accept a teacher invitation
As a student, I want to accept my invitation so that I can access my teacher.

Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Owner: Toprak Daldal · Priority: High · Order: 5 · 3 SP
Depends: [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17)
Requirement: [FR-04](sprint-2/SRS.md#fr-04)
API: `POST /invitations/accept`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-04.1:** A valid, unused, unexpired code for the signed-in student email creates one teacher-student relationship and returns 201. Consuming the code and creating the relationship are atomic.
- **AC-04.2:** A mismatched student email or wrong role returns 403; unknown code returns 404; malformed/missing code returns 400.
- **AC-04.3:** Expired, already used or duplicate-relationship invitations return 409. Two simultaneous uses cannot create duplicate relationships.
- **AC-04.4:** A code is expired when server time reaches expiresAt. Invitations do not change the account role.

Task: [T-04 / #32](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/32), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19): View my connections
As a user, I want my connection list so that I can choose the right teacher or student.

Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Owner: Arda Demir · Priority: High · Order: 6 · 2 SP
Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18)
Requirement: [FR-05](sprint-2/SRS.md#fr-05)
API: `GET /teachers/me/students; GET /students/me/teachers`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-05.1:** A teacher receives only their connected students from the teacher-only operation; a student receives only their connected teachers from the student-only operation. A valid empty list returns 200.
- **AC-05.2:** Calling the other role-only list returns 403; missing/invalid credentials return 401.
- **AC-05.3:** Results are ordered by name and contain at most 200 items. They contain no password, token or other account secret.

Task: [T-05 / #33](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/33), implement/integrate and test the parent criteria, 3 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20): Publish availability
As a teacher, I want to publish a lesson slot so that students can request it.

Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Owner: Osman Berke Özdemir · Priority: High · Order: 7 · 3 SP
Depends: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
Requirement: [FR-06](sprint-2/SRS.md#fr-06)
API: `POST /availability`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-06.1:** A future interval with explicit timezone offsets and endTime after startTime returns 201. Teacher identity is taken from the session, not a caller-supplied owner.
- **AC-06.2:** Malformed, missing-offset, past or reversed intervals return 400. Overlap with the same teacher availability returns 409.
- **AC-06.3:** An authenticated student receives 403. Adjacent intervals are permitted: one may end exactly when the next starts.

Task: [T-06 / #34](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/34), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21): View teacher availability
As a connected student, I want available slots so that I can choose a lesson.

Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Owner: Arda Demir · Priority: High · Order: 8 · 2 SP
Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20)
Requirement: [FR-07](sprint-2/SRS.md#fr-07)
API: `GET /availability`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-07.1:** A valid teacherId returns future slots for that teacher without overlaps with approved lessons, ordered by startTime and limited to 200 items. The teacher may query self; a student may query a connected teacher.
- **AC-07.2:** Pending requests do not hide the slot. No matching slots returns 200 with an empty list.
- **AC-07.3:** Missing/invalid teacherId or invalid date ranges return 400; unknown teacher returns 404; unrelated students or other unauthorized role/owner combinations return 403.
- **AC-07.4:** If date filters are supplied, apply the common half-open overlap rule in BR-06. Dates include offsets.

Task: [T-07 / #35](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/35), implement/integrate and test the parent criteria, 3 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22): Remove an unused slot
As a teacher, I want to remove a slot so that my availability stays correct.

Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Owner: Osman Berke Özdemir · Priority: Medium · Order: 14 · 2 SP
Depends: [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20)
Requirement: [FR-08](sprint-2/SRS.md#fr-08)
API: `DELETE /availability/{id}`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-08.1:** The owner removes a slot without pending or approved bookings and receives 204 with no response body.
- **AC-08.2:** A slot with a pending or approved booking returns 409 and remains unchanged; cancel permitted bookings first.
- **AC-08.3:** Wrong owner returns 403, unknown slot 404 and malformed id 400. Student accounts cannot delete teacher slots.

Task: [T-08 / #36](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/36), implement/integrate and test the parent criteria, 3 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23): Request a lesson
As a connected student, I want to request a slot so that I can arrange a lesson.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Mehmet Ali Demircioğlu · Priority: High · Order: 9 · 3 SP
Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21)
Requirement: [FR-09](sprint-2/SRS.md#fr-09)
API: `POST /bookings`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-09.1:** A valid request returns 201 with status pending and copies the selected slot times and teacher identity; the student cannot override these fields.
- **AC-09.2:** No teacher-student relationship or wrong role returns 403; malformed input returns 400; unknown slot returns 404.
- **AC-09.3:** A duplicate active request for the same student/slot, or an unavailable/approved-overlapping slot, returns 409. Pending requests alone do not reserve the slot.
- **AC-09.4:** An input/time conflict creates no extra booking. Cross-teacher student clashes remain an explicit decision in OD-06; this criterion does not claim their prevention.

Task: [T-09 / #37](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/37), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24): Approve or reject a lesson
As a teacher, I want to decide requests so that I control my schedule.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Mehmet Ali Demircioğlu · Priority: High · Order: 10 · 5 SP
Depends: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
Requirement: [FR-10](sprint-2/SRS.md#fr-10)
API: `PATCH /bookings/{id}/status`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-10.1:** The owning teacher changes their pending booking to approved or rejected and receives 200 with the updated booking.
- **AC-10.2:** Wrong owner/role returns 403, unknown booking 404 and invalid status/input 400. Invalid or terminal transitions return 409.
- **AC-10.3:** Approval rechecks availability and all overlapping approved lessons for the teacher in one atomic transaction. Concurrent conflicting approvals produce at most one approved lesson; the conflicting request receives 409.
- **AC-10.4:** Overlap means start < otherEnd and end > otherStart. Adjacent lessons are allowed. The rule is checked at approval time, not only when the request is created.

Task: [T-10 / #38](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/38), implement/integrate and test the parent criteria, 8 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25): View my lesson calendar
As a user, I want my lessons and their states so that I know what is planned.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Kemal Efe Bilgisiçok · Priority: High · Order: 11 · 3 SP
Depends: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
Requirement: [FR-11](sprint-2/SRS.md#fr-11)
API: `GET /bookings`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-11.1:** The user receives only bookings in which they are the teacher or student, with current states, ordered by startTime; empty results return 200.
- **AC-11.2:** Optional from/to filters select intervals by BR-06. Optional status accepts only pending, approved, rejected or cancelled; invalid filters return 400.
- **AC-11.3:** Results contain at most 200 items. Unrelated users cannot obtain another participant list by supplying their identity; ownership is session-derived.

Task: [T-11 / #39](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/39), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26): Cancel a permitted lesson
As a participant, I want to cancel before the start so that my calendar stays accurate.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Osman Berke Özdemir · Priority: Medium · Order: 15 · 3 SP
Depends: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
Requirement: [FR-12](sprint-2/SRS.md#fr-12)
API: `PATCH /bookings/{id}/status`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-12.1:** Either participant can cancel their pending or approved booking strictly before startTime; the operation returns 200 with status cancelled.
- **AC-12.2:** An unrelated user returns 403. A terminal booking or a booking whose startTime has been reached returns 409; unknown id returns 404 and malformed input returns 400.
- **AC-12.3:** Rejected and cancelled are terminal states. A cancelled booking no longer blocks future approval or slot removal under the common rules.

Task: [T-12 / #40](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/40), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27): Assign a homework file
As a teacher, I want to assign a PDF or image so that my student can practise.

Parent: [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) · Owner: Kemal Efe Bilgisiçok · Priority: High · Order: 12 · 5 SP
Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18)
Requirement: [FR-13](sprint-2/SRS.md#fr-13)
API: `POST /assignments`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-13.1:** A valid multipart upload returns 201 for the connected student. Title is 1-120 characters; optional instructions are at most 2000 characters.
- **AC-13.2:** PDF, JPEG or PNG files of at most 10 MiB (10485760 bytes) are accepted; larger files return 413 and unsupported actual types return 415. Actual content is checked, not only the extension.
- **AC-13.3:** Wrong role or an unconnected student returns 403; invalid required fields return 400 and unknown referenced student returns 404.
- **AC-13.4:** Filenames are sanitized and files are stored outside public static paths. Responses expose protected metadata, not an unrestricted public storage URL.

Task: [T-13 / #41](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/41), implement/integrate and test the parent criteria, 8 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28): Read my assignments
As a student, I want to find and download my assignments so that I can study.

Parent: [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) · Owner: Kemal Efe Bilgisiçok · Priority: High · Order: 13 · 3 SP
Depends: [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27)
Requirement: [FR-14](sprint-2/SRS.md#fr-14)
API: `GET /assignments; GET /assignments/{id}; GET /assignments/{id}/file`
Status: Planned implementation.

Acceptance criteria (not passed results):
- **AC-14.1:** The teacher sees own created assignments and the student sees assignments addressed to them; list results are newest first, at most 200 items, with 200 and an empty list when appropriate.
- **AC-14.2:** Only the creating teacher or assigned student can read details and download the file. Unrelated users return 403; unknown assignment returns 404 and malformed id returns 400.
- **AC-14.3:** File download applies the same ownership check as metadata, uses the actual media type and a safe Content-Disposition filename, and never reveals a public storage path.
- **AC-14.4:** Student homework submission, grading and feedback are outside this first release; retrieving an assigned file does not submit work.

Task: [T-14 / #42](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/42), implement/integrate and test the parent criteria, 4 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

### [US-15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60): Read my current profile
As a signed-in teacher or student, I want to read my own profile so that the interface can identify me and select the correct role-specific journey.

Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Owner: Mehmet Ali Demircioğlu · Priority: High · Order: 3 · 2 SP
Depends: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
Requirement: [FR-15](sprint-2/SRS.md#fr-15)
Contract operation integrated through [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58): `GET /users/me`. It is present in the develop contract; [T-15 / #61](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61) tracks remaining profile/role-entry acceptance.
Status: Auth code merged via PR #58/#79; QA evidence recorded; full story acceptance pending.

Acceptance criteria (not passed results):
- **AC-15.1:** A valid session returns 200 with only the signed-in user id, name, email and teacher/student role, matching the User schema.
- **AC-15.2:** Missing, malformed, unknown or expired credentials return 401 and no profile. No password, hash or token is included in the profile.
- **AC-15.3:** Caller-supplied identity/role cannot select a different user. The stored role supports the correct teacher or student entry screen.
- **AC-15.4:** The proposed GET /users/me operation is integrated into the reviewed develop contract before this story can be accepted. PR #58 alone is not proof of integration or complete UI behavior.

Task: [T-15 / #61](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61), implement/integrate and test the parent criteria, 3 initial hours. It inherits this story owner, priority and dependencies; no completion is claimed.

## Readiness, evidence and handoff

Ready: actor/value, acceptance criteria, owner, dependencies, contract impact and relevant decision owners are clear; split work that does not fit the agreed sprint capacity. Done for implementation: criteria pass, actual checks and teammate review are linked, contract/UI behavior aligns and contributions are recorded. A review of this document does not complete the implementation tasks.

Release backlog: 15 stories, 15 tasks, 6 features and 3 epics. Profile addition is tracked in #60/#61. Other Issue identities are retained. Toprak's Sprint 2 document work is #59; future implementation task hours do not estimate the whole Sprint 2 deliverable effort.

The previous API/backlog document consistency review in [PR #54](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/54) is historical evidence. It is not a runtime test result. This revision preserves the response-code intent and expands traceable acceptance criteria.

Architecture/token/deployment decisions remain in SRS section 9. Figma, the dedicated NFR specification and the [cross-artifact traceability matrix](sprint-2/Traceability.md) remain separate team deliverables. AI, parents, payments, university OBS, teacher discovery, integrated video/chat, analytics and homework submission/feedback remain outside the MVP.
