# TutorBridge: Proposal and System Vision

SENG 321 · Sprint 1 · Team review draft

## Project proposal

### Problem and current process

Private tutors arrange lessons and send homework to their existing students. Our starting hypothesis is that using separate messages, calendars and files makes this work hard to track. A changed lesson time can be missed. Students may struggle to find their latest homework.

We have not interviewed teachers or students yet. The frequency of these problems and the time spent resolving them are unknown. We do not claim measured results.

For context, [OECD TALIS 2024](https://www.oecd.org/en/publications/results-from-talis-2024_90df6235-en/full-report/the-demands-of-teaching_0e941e2f.html) reports that about half of teachers across OECD education systems identify excessive administrative work as a source of stress. This is school-teacher evidence, not a survey of private tutors. It supports investigating administrative burden; it does not prove our scheduling hypothesis.

Before implementation, Toprak and Arda will arrange short conversations with teachers and students. They will ask how lessons are scheduled, how often changes happen and how homework is shared. Findings will go in [Problem Validation](Problem-Validation.md).

### Stakeholders

| Stakeholder | Need | Influence |
|---|---|---|
| Teacher | Organize current students, lessons and homework | High: defines the tutoring workflow |
| Student | Find lesson times and assigned materials | High: uses the main student journey |
| Team | Agree a feasible scope and deliver working increments | High: owns product decisions |
| Application operator | Maintain storage, access and backups | Medium: sets operating limits |
| Course staff | Review the project and individual evidence | High: assesses the work |
| Hosting provider, when chosen | Supply hosting within its limits | Medium: external infrastructure dependency |

Parents are a possible future stakeholder. They have no account in the MVP.

### Solution and intended value

TutorBridge is a small web application for existing teacher-student relationships. A teacher invites a student, publishes available lesson slots and assigns PDF/image homework. Students accept invitations, request lessons and access their own materials. Teachers approve or reject requests.

The intended value is clearer schedules and easier access to assignments. We will test these targets:

| Target | How to check it |
|---|---|
| A logged-in, connected student requests a lesson within two minutes | Timed usability task |
| A teacher never has two overlapping approved lessons | Sequential and concurrent booking tests |
| Students cannot access another student's assignments | Negative API tests |
| A teacher shares a permitted file and the student retrieves it | End-to-end assignment test |

These are targets. They are not completed test results.

### Feasibility

| Area | Plan and constraint |
|---|---|
| Frontend | Plain HTML, CSS and JavaScript. The repository already has placeholders for these files. |
| Backend | Node.js with Express. One language can serve the browser and API work. |
| Database | SQLite for the small course deployment. It needs no separate database server. Only the backend opens the database file. |
| Concurrent bookings | Check availability and write the approval in one transaction. Test simultaneous approvals. SQLite's single-writer limit suits a small evaluation, not a high-traffic service. |
| Files | Store assignment files outside the public web directory. Validate type and size. Authorize every download. |
| Integrations | No AI, email or external calendar API is required. Users share invitation codes themselves. |
| Skills and schedule | Six members share product, process, architecture, quality, DevOps and implementation work. Estimates and dependencies are in the backlog. The team still needs to confirm capacity. |
| Cost and operations | Local development needs no paid service. A hosting provider, storage budget and backup process must be chosen before deployment. |
| Legal and ethical constraints | Use test or authorized data. Minimize personal data and control file access. MIT covers code, not ownership of uploaded learning materials. |

This is the planned stack, not an implemented backend. Hosting and implementation package versions are not selected yet.

### First release

- Teacher and student registration and login.
- Teacher invitations and student acceptance.
- A teacher's connected student list.
- Creating, viewing and removing available lesson slots.
- Lesson requests, approval, rejection, cancellation and calendar lists.
- PDF/image assignment upload and access by the assigned student.
- Server-side role and relationship checks.

### Outside the first release

AI question generation; parent accounts; teacher discovery; payments; built-in video; chat; external calendar sync; native mobile apps; advanced analytics; student homework submissions and teacher feedback.

### Assumptions

- Teachers bring their existing students.
- Each user registers as a teacher or a student.
- A student can connect to several teachers.
- Users have a browser and internet access.
- The first deployment has a small evaluation dataset.
- All API times include an offset. Times are stored in UTC and displayed in the user's local zone.

### Main risks

| Risk | Mitigation | Owner |
|---|---|---|
| Overlapping approvals | Use a transaction and test concurrent requests | Mehmet Ali |
| Wrong access to student data | Check role, relationship and record ownership on every request | Mehmet Ali, Berat |
| Unsafe or excessive files | Permit PDF/JPEG/PNG, limit files to 10 MiB and protect downloads | Osman Berke, Kemal Efe |
| Too much scope | Keep deferred features out of the API and first-release stories | Toprak |
| Integration or uneven workload | Small Issues and reviewed PRs; record each member's actual work | Arda |
| Unvalidated user problem | Conduct and record real interviews before claiming user evidence | Toprak, Arda |

### License

We use [MIT](../LICENSE.md). It permits reuse, modification and redistribution with the required notice. This suits a course project that others may extend. MIT does not require derivatives to use MIT and does not add a separate explicit patent grant. We will check dependency licenses and third-party notices before implementation.

Sources for the planned tools: [Express](https://expressjs.com/) and [SQLite use cases](https://sqlite.org/whentouse.html).

## System vision and boundary

### Vision

Give tutors and their existing students one place to manage lesson requests and homework. Keep the first release focused on these everyday tasks.

### Actors and responsibilities

| Actor | Actions |
|---|---|
| Teacher | Invite students, manage availability, decide lesson requests, assign files and view own lessons |
| Student | Accept an invitation, see connected teachers' slots, request/cancel lessons and access own assignments |

The application owns authentication, relationship records, availability, booking rules, assignment records and protected file access. Teaching, payment collection and live lesson delivery remain outside it.

### Context diagram

![TutorBridge system boundary](diagrams/system-boundary.svg)

Actors and browsers are outside the service boundary. The backend, database and application-managed file storage are inside it. No external application integration is required for the MVP. If hosting or storage is outsourced, update the provider boundary and exchanged data before implementation. GitHub and Teams support development and submission; they are not tutoring-system runtime services.

### Agreed design rules for review

1. A protected action requires a valid access token. The server also checks role and ownership.
2. Only a teacher can create an invitation. It contains the intended student's email, expires after seven days and can be used once.
3. Only a student with that email can accept it. An existing relationship cannot be duplicated.
4. A student can view availability and request lessons only from connected teachers.
5. A booking references one availability slot. Its start and end come from that slot. The end is exclusive, so adjacent lessons do not overlap.
6. A request starts as `pending`. Only the relevant teacher can approve or reject it.
7. Pending requests do not exclusively hold a slot. Approval rechecks conflicts in the same transaction. Two overlapping lessons for the same teacher cannot both be approved.
8. Either participant may cancel their own pending or approved booking before it starts. Rejected or cancelled bookings cannot change state again.
9. A slot with pending or approved bookings cannot be removed. Cancel permitted bookings first.
10. Teachers can assign files only to connected students. Students can access only files assigned to them.
11. Uploads accept PDF, JPEG or PNG, up to 10 MiB. Files stay outside public static storage. Downloads require authorization.
12. Dates use RFC 3339 timestamps with a timezone offset. Invalid or past booking intervals are rejected.

The API and backlog use these rules. They remain subject to the team's peer review before implementation.

### Constraints and next checks

This Sprint 1 contract does not implement the application. Interviews, hosting, team capacity and implementation tests remain outstanding. Review this document with the API, RACI and backlog before merging. The official foundation PDF and the assistant announcement are the submission baseline; the separate Examples file has not been supplied.
