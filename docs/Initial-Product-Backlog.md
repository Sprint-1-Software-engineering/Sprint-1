# Initial Product Backlog

This is the planned first-release backlog, not completed implementation. Estimates are initial team estimates. SP means story points; hours are task estimates. Refine them before committing work to a sprint.

## Epics and Features

| Epic | Features | Priority | Estimate | Owner | Dependency |
|---|---|---|---|---|---|
| [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) Accounts and connections | [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9), [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) | High | 14 SP | Toprak | None |
| [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) Lesson scheduling | [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11), [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) | High | 21 SP | Toprak | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) |
| [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) Assignment sharing | [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13), [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) | High | 8 SP | Toprak | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) |

| Feature | Parent | Estimate | Owner |
|---|---|---|---|
| [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) Accounts | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) | 6 SP | Mehmet Ali Demircioğlu |
| [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) Teacher-student connections | [E-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/6) | 8 SP | Toprak Daldal |
| [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) Availability | [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) | 7 SP | Osman Berke Özdemir |
| [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) Booking lifecycle | [E-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/7) | 14 SP | Mehmet Ali Demircioğlu |
| [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) Assignment creation | [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) | 5 SP | Kemal Efe Bilgisiçok |
| [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) Assignment access | [E-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/8) | 3 SP | Kemal Efe Bilgisiçok |

Epic/Feature acceptance: all linked child criteria pass. Their priority is High. Dependencies are the child dependencies below. Estimates roll up from the stories.

## Stories and Tasks

### [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15): Register an account
As a teacher or student, I want an account so that my records belong to me.
Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Owner: Mehmet Ali Demircioğlu · High · 3 SP · Depends: None
API: `POST /auth/register`
- Valid teacher/student details create one account.
- Duplicate email returns 409; missing/invalid fields return 400.
Task: [T-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/29), implement and test this story, 4 h.

### [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16): Sign in
As a user, I want to sign in so that I can access my own records.
Parent: [F-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/9) · Owner: Mehmet Ali Demircioğlu · High · 3 SP · Depends: [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15)
API: `POST /auth/login`
- Correct credentials return a token valid for one hour.
- Wrong credentials return generic 401; protected requests reject expired tokens.
Task: [T-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/30), implement and test this story, 4 h.

### [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17): Invite an existing student
As a teacher, I want to invite an existing student so that we can share lessons.
Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Owner: Toprak Daldal · High · 3 SP · Depends: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
API: `POST /invitations`
- A teacher creates a single-use, email-bound code valid for seven days.
- Students cannot invite; an existing connection returns 409.
Task: [T-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/31), implement and test this story, 4 h.

### [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18): Accept a teacher invitation
As a student, I want to accept my invitation so that I can access my teacher.
Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Owner: Toprak Daldal · High · 3 SP · Depends: [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17)
API: `POST /invitations/accept`
- A valid code and matching student email create one relationship.
- Wrong email: 403; unknown code: 404; expired/used code: 409; missing input: 400.
Task: [T-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/32), implement and test this story, 4 h.

### [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19): View my connections
As a user, I want my connection list so that I can choose the right teacher or student.
Parent: [F-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/10) · Owner: Arda Demir · High · 2 SP · Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18)
API: `GET /teachers/me/students; GET /students/me/teachers`
- Teachers see connected students; students see connected teachers.
- Wrong roles cannot read the other role-only list.
Task: [T-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/33), implement and test this story, 3 h.

### [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20): Publish availability
As a teacher, I want to publish a lesson slot so that students can request it.
Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Owner: Osman Berke Özdemir · High · 3 SP · Depends: [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16)
API: `POST /availability`
- A future interval with offset and end after start creates a slot.
- Invalid/past interval: 400; overlapping own availability: 409.
Task: [T-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/34), implement and test this story, 4 h.

### [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21): View teacher availability
As a connected student, I want available slots so that I can choose a lesson.
Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Owner: Arda Demir · High · 2 SP · Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20)
API: `GET /availability`
- Connected students see future slots without approved overlaps, ordered by start.
- Unconnected students get 403.
Task: [T-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/35), implement and test this story, 3 h.

### [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22): Remove an unused slot
As a teacher, I want to remove a slot so that my availability stays correct.
Parent: [F-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/11) · Owner: Osman Berke Özdemir · Medium · 2 SP · Depends: [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20)
API: `DELETE /availability/{id}`
- The owner removes a slot without pending/approved bookings; response: 204.
- Wrong owner: 403; active bookings: 409.
Task: [T-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/36), implement and test this story, 3 h.

### [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23): Request a lesson
As a connected student, I want to request a slot so that I can arrange a lesson.
Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Mehmet Ali Demircioğlu · High · 3 SP · Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18), [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21)
API: `POST /bookings`
- A connected student requests a future slot; it becomes pending with the slot times.
- No relationship: 403; duplicate active request or unavailable time: 409.
Task: [T-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/37), implement and test this story, 4 h.

### [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24): Approve or reject a lesson
As a teacher, I want to decide requests so that I control my schedule.
Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Mehmet Ali Demircioğlu · High · 5 SP · Depends: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
API: `PATCH /bookings/{id}/status`
- The teacher approves/rejects their own pending request.
- Concurrent overlapping approvals produce at most one approved lesson; conflict: 409. Adjacent lessons are allowed.
Task: [T-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/38), implement and test this story, 8 h.

### [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25): View my lesson calendar
As a user, I want my lessons and their states so that I know what is planned.
Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Kemal Efe Bilgisiçok · High · 3 SP · Depends: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
API: `GET /bookings`
- Users see only their own lessons and current statuses.
- Date filters use interval overlap; invalid ranges return 400.
Task: [T-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/39), implement and test this story, 4 h.

### [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26): Cancel a permitted lesson
As a participant, I want to cancel before the start so that my calendar stays accurate.
Parent: [F-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/12) · Owner: Osman Berke Özdemir · Medium · 3 SP · Depends: [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23)
API: `PATCH /bookings/{id}/status`
- Either participant can cancel pending/approved lessons before the start.
- Unrelated user: 403; terminal or started lesson: 409.
Task: [T-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/40), implement and test this story, 4 h.

### [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27): Assign a homework file
As a teacher, I want to assign a PDF or image so that my student can practise.
Parent: [F-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/13) · Owner: Kemal Efe Bilgisiçok · High · 5 SP · Depends: [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18)
API: `POST /assignments`
- Teacher assigns PDF/JPEG/PNG to a connected student.
- Unconnected student: 403; file over 10 MiB: 413; unsupported type: 415.
Task: [T-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/41), implement and test this story, 8 h.

### [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28): Read my assignments
As a student, I want to find and download my assignments so that I can study.
Parent: [F-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/14) · Owner: Kemal Efe Bilgisiçok · High · 3 SP · Depends: [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27)
API: `GET /assignments; GET /assignments/{id}; GET /assignments/{id}/file`
- Teacher sees their own assignments; student sees work assigned to them.
- Unrelated users get 403 for metadata and file; valid downloads use the correct type and safe filename.
Task: [T-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/42), implement and test this story, 4 h.

Each task inherits its parent story's owner, priority and dependencies. It passes when the parent criteria pass and a reviewed PR links actual test evidence.

## Ready and Done

Ready: the user/value, criteria, dependencies, API impact and owner are clear, and the work fits one sprint. Done: criteria pass, checks and teammate review are recorded, and contribution links are updated. All implementation items here remain planned.

AI, parent access, payments, teacher discovery, video, chat, analytics and homework submission/feedback remain outside the MVP.

### API and Backlog Consistency
The API and backlog specify 409 for booking conflicts and 403 for unauthorized assignment access. Oversized files return 413, and unsupported file types return 415. These cases are consistent across both documents. This is a document review; application behavior has not been tested.
