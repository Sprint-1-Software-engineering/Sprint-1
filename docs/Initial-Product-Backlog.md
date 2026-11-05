# Initial Product Backlog

This is the first-release product backlog, prepared in Sprint 1. Implementation items are planned, not completed. Estimates are starting points for team refinement; story points are not hours. Owners follow the RACI plan and require team review.

## Epic and Feature hierarchy

| Epic | Features | Priority | Estimate | Owner | Dependency |
|---|---|---|---|---|---|
| [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) Accounts and connections | [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) Accounts, [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) Teacher-student connections | High | 14 SP | Toprak | None |
| [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) Lesson scheduling | [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) Availability, [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) Booking lifecycle | High | 21 SP | Toprak | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) |
| [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) Assignment sharing | [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) Assignment creation, [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) Assignment access | High | 8 SP | Toprak | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) |

| Feature | Parent | Estimate | Owner | Acceptance |
|---|---|---|---|---|
| [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) Accounts | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) | 6 SP | Mehmet Ali Demircioğlu | All linked story criteria pass |
| [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) Teacher-student connections | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) | 8 SP | Toprak Daldal | All linked story criteria pass |
| [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) Availability | [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) | 7 SP | Osman Berke Özdemir | All linked story criteria pass |
| [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) Booking lifecycle | [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) | 14 SP | Mehmet Ali Demircioğlu | All linked story criteria pass |
| [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) Assignment creation | [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) | 5 SP | Kemal Efe Bilgisiçok | All linked story criteria pass |
| [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) Assignment access | [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) | 3 SP | Kemal Efe Bilgisiçok | All linked story criteria pass |

## User Stories

### [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15): Register an account
As a teacher or student, I want an account so that my records belong to me.

Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Priority: High · Estimate: 3 SP · Owner: Mehmet Ali Demircioğlu · Status: Planned
Dependencies: None
API: `POST /auth/register`

- Valid teacher/student input creates one user without exposing the password.
- Duplicate email returns 409; missing or invalid fields return 400.

### [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16): Sign in
As a user, I want to sign in so that I can access my own records.

Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Priority: High · Estimate: 3 SP · Owner: Mehmet Ali Demircioğlu · Status: Planned
Dependencies: [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15)
API: `POST /auth/login`

- Valid credentials return a one-hour bearer token.
- Wrong credentials return generic 401; protected requests reject invalid/expired tokens.

### [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17): Invite an existing student
As a teacher, I want to invite an existing student so that we can share lessons.

Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Priority: High · Estimate: 3 SP · Owner: Toprak Daldal · Status: Planned
Dependencies: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
API: `POST /invitations`

- Teacher creates a single-use invitation tied to an email, valid seven days.
- Students cannot create invitations; an existing connection returns 409.

### [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18): Accept a teacher invitation
As a student, I want to accept my invitation so that I can access my teacher.

Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Priority: High · Estimate: 3 SP · Owner: Toprak Daldal · Status: Planned
Dependencies: [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17)
API: `POST /invitations/accept`

- Matching student email and valid code create one relationship.
- Wrong email returns 403; unknown code 404; expired/used code or duplicate relationship 409. Missing input returns 400.

### [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19): View my connections
As a user, I want my connection list so that I can choose the right teacher or student.

Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Priority: High · Estimate: 2 SP · Owner: Arda Demir · Status: Planned
Dependencies: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18)
API: `GET /teachers/me/students; GET /students/me/teachers`

- Teacher sees only connected students; student sees only connected teachers.
- The wrong role cannot retrieve the other role-only list.

### [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20): Publish availability
As a teacher, I want to publish a lesson slot so that students can request it.

Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Priority: High · Estimate: 3 SP · Owner: Osman Berke Özdemir · Status: Planned
Dependencies: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
API: `POST /availability`

- A future interval with offset and end after start creates a slot.
- Invalid/past interval returns 400; overlap with own availability returns 409.

### [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21): View teacher availability
As a connected student, I want available slots so that I can choose a lesson.

Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Priority: High · Estimate: 2 SP · Owner: Arda Demir · Status: Planned
Dependencies: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20)
API: `GET /availability`

- Connected student sees future slots without overlapping approved lessons.
- Unconnected student gets 403; results are ordered by startTime.

### [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22): Remove an unused slot
As a teacher, I want to remove a slot so that my availability stays correct.

Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Priority: Medium · Estimate: 2 SP · Owner: Osman Berke Özdemir · Status: Planned
Dependencies: [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20)
API: `DELETE /availability/{id}`

- Owner can remove a slot with no pending/approved bookings; response is 204.
- Wrong owner gets 403; a slot with active bookings returns 409.

### [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23): Request a lesson
As a connected student, I want to request a slot so that I can arrange a lesson.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Priority: High · Estimate: 3 SP · Owner: Mehmet Ali Demircioğlu · Status: Planned
Dependencies: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21)
API: `POST /bookings`

- Valid future slot creates a pending booking using its stored times.
- No relationship returns 403; duplicate active request or unavailable slot returns 409.

### [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24): Approve or reject a lesson
As a teacher, I want to decide requests so that I control my schedule.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Priority: High · Estimate: 5 SP · Owner: Mehmet Ali Demircioğlu · Status: Planned
Dependencies: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
API: `PATCH /bookings/{id}/status`

- Own pending request can become approved or rejected; another user cannot decide it.
- Two concurrent overlapping approvals yield at most one approved booking; the other returns 409. Adjacent intervals are allowed.

### [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25): View my lesson calendar
As a user, I want my lessons and their states so that I know what is planned.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Priority: High · Estimate: 3 SP · Owner: Kemal Efe Bilgisiçok · Status: Planned
Dependencies: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
API: `GET /bookings`

- Teacher/student sees only their own bookings and current statuses.
- Date filters use interval overlap; invalid ranges return 400.

### [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26): Cancel a permitted lesson
As a participant, I want to cancel before the start so that my calendar stays accurate.

Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Priority: Medium · Estimate: 3 SP · Owner: Osman Berke Özdemir · Status: Planned
Dependencies: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
API: `PATCH /bookings/{id}/status`

- Either participant can cancel pending/approved booking before start.
- Unrelated user gets 403; terminal or already-started booking returns 409.

### [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27): Assign a homework file
As a teacher, I want to assign a PDF or image so that my student can practise.

Parent: [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) · Priority: High · Estimate: 5 SP · Owner: Kemal Efe Bilgisiçok · Status: Planned
Dependencies: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18)
API: `POST /assignments`

- Connected student, title and valid PDF/JPEG/PNG produce an assignment.
- Unconnected student returns 403; over 10 MiB returns 413; unsupported type returns 415.

### [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28): Read my assignments
As a student, I want to find and download my assignments so that I can study.

Parent: [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) · Priority: High · Estimate: 3 SP · Owner: Kemal Efe Bilgisiçok · Status: Planned
Dependencies: [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27)
API: `GET /assignments; GET /assignments/{id}; GET /assignments/{id}/file`

- Teacher sees own created assignments; student sees only work addressed to them.
- Unrelated user gets 403 for metadata and file; permitted download has correct type and safe filename.

## Tasks

Each task implements its parent story and tests its positive and failure cases. The parent links provide the detailed acceptance criteria and API impact. A task is done only after tests and teammate review. All tasks below are planned.

| Task | Parent | Priority | Estimate | Owner | Dependencies |
|---|---|---|---|---|---|
| [T-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/29): implement/test register an account | [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15) | High | 4 h | Mehmet Ali Demircioğlu | None |
| [T-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/30): implement/test sign in | [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16) | High | 4 h | Mehmet Ali Demircioğlu | [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15) |
| [T-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/31): implement/test invite an existing student | [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17) | High | 4 h | Toprak Daldal | [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16) |
| [T-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/32): implement/test accept a teacher invitation | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18) | High | 4 h | Toprak Daldal | [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17) |
| [T-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/33): implement/test view my connections | [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19) | High | 3 h | Arda Demir | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18) |
| [T-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/34): implement/test publish availability | [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20) | High | 4 h | Osman Berke Özdemir | [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16) |
| [T-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/35): implement/test view teacher availability | [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21) | High | 3 h | Arda Demir | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20) |
| [T-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/36): implement/test remove an unused slot | [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22) | Medium | 3 h | Osman Berke Özdemir | [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20) |
| [T-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/37): implement/test request a lesson | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) | High | 4 h | Mehmet Ali Demircioğlu | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21) |
| [T-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/38): implement/test approve or reject a lesson | [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24) | High | 8 h | Mehmet Ali Demircioğlu | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) |
| [T-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/39): implement/test view my lesson calendar | [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25) | High | 4 h | Kemal Efe Bilgisiçok | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) |
| [T-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/40): implement/test cancel a permitted lesson | [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26) | Medium | 4 h | Osman Berke Özdemir | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) |
| [T-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/41): implement/test assign a homework file | [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27) | High | 8 h | Kemal Efe Bilgisiçok | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18) |
| [T-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/42): implement/test read my assignments | [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28) | High | 4 h | Kemal Efe Bilgisiçok | [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27) |

## Readiness and completion

Ready means the user, capability and value are clear; criteria are testable; dependencies and API impact are known; an owner accepts the work; and the item can fit one sprint. Split it if it cannot.

Done means criteria pass, checks are recorded, a teammate reviews the PR, and actual contribution links are updated. A task assignment is not completed-work evidence.

Owners without repository access are named in the Issue body. Their GitHub Assignee field is pending access. No implementation milestone has been assigned yet.

## Deferred

AI question generation, parent access, homework submission/feedback, payments, teacher discovery, video, chat and analytics remain outside the MVP. They are ideas for later prioritization, not committed first-release stories.
