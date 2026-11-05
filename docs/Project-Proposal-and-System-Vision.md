# Project Proposal and System Vision: TutorBridge

## 1. Problem and expected value

Teachers need time to teach, prepare lessons and manage their students. Students need lesson times that fit their schedules and a clear place to find homework. TutorBridge brings these tasks into one web application for private tutors and their existing students.

Our starting assumption is that arranging lessons and sharing homework through separate messages makes these tasks hard to organize.

### User conversation: 3 November 2026

The team spoke with one private tutor who gives mathematics and software lessons. We refer to this person as T1, without recording their name or contact details.

| Topic | What T1 reported |
|---|---|
| Current lesson process | Arrange the time with each student on WhatsApp, then give the lesson through Google Meet. |
| Current homework process | Send homework to students individually on WhatsApp. |
| Problem | Repeated communication is needed to arrange lessons. T1 handles planning manually and finds individual homework messages complicated to organize. |
| Response to the proposal | T1 said they would be willing to use the proposed system. This is stated interest, not evidence of actual use. |

These findings support our focus on availability, lesson requests and one place for assignments. Google Meet can remain the tutor's separate lesson tool; the MVP does not need video or a Meet integration.

This is one qualitative conversation, reported by the team. Problem frequency and time spent were not measured. The findings do not establish how common the problem is. After a prototype is available, test the lesson-request and homework-access tasks and measure the success targets below.

## 2. Users and stakeholders

| Group | Need and role |
|---|---|
| Teachers | Manage current students, availability, lesson requests and homework. Primary user and workflow decision maker. |
| Students | Find available times, request lessons and access their own assignments. Primary user. |
| Team | Agree the scope, build the system and maintain its records. Product owner and operator. |
| Hosting provider, when selected | Supply hosting and storage within its limits. External infrastructure dependency. |
| Course staff | Review the project, workflow and individual contributions. Assessment stakeholder. |

Parents may use a later version. They do not have an account in the first release.

## 3. Proposed solution and first release

1. A teacher invites an existing student. The student accepts and becomes connected to that teacher.
2. The teacher publishes lesson slots. A connected student requests one; the teacher approves or rejects it.
3. The teacher assigns a PDF or image. The student can view and download their own assignment.

The first release also includes registration, login, personal lesson lists, permitted cancellations and removal of unused slots. Only the relevant teacher and student can access their private records.

Outside this release: AI question generation, parent access, teacher discovery, payments, video, chat, external calendar sync, native mobile apps and advanced analytics. Homework submission and feedback can be considered later.

## 4. Feasibility, assumptions and risks

| Area | Plan |
|---|---|
| Technology | HTML, CSS and JavaScript; Node.js with Express; SQLite. This is a small course application. The backend is not implemented yet. |
| Skills and schedule | Six members share the work in the RACI plan. The backlog contains initial estimates and dependencies. The team still needs to confirm capacity. |
| Data and integration | Use test or authorized data. Store files outside the public web directory. No external AI, email or calendar service is needed. |
| Operations and cost | Start locally without a paid service. Select hosting, storage limits and backups before deployment. SQLite suits a small deployment; concurrent approvals need transactional tests. |
| Legal and ethical limits | Protect student information and file access. Share learning materials only with permission. Check dependency licenses before implementation. |

Assumptions: users have a browser and internet access; teachers bring their existing students; each account is a teacher or student; a student may connect to several teachers. The evaluation dataset is small.

| Risk | Mitigation | Owner |
|---|---|---|
| Double booking | Check and approve in one transaction; test simultaneous requests | Mehmet Ali, Berat |
| Access to another student's records | Check role, relationship and ownership on the server | Mehmet Ali, Berat |
| Unsafe or large files | Permit PDF/JPEG/PNG up to 10 MiB; authorize downloads | Osman Berke, Kemal Efe |
| Too much scope or uneven work | Use small Issues, clear owners and reviewed PRs | Toprak, Arda |
| Wrong assumptions about users | Check the first tutor findings with more users and prototype tasks | Toprak, Arda |

## 5. Success criteria and license

Targets, not completed results:
- A logged-in, connected student can request a lesson within two minutes in a usability task.
- A teacher cannot have overlapping approved lessons, including concurrent approval attempts.
- A student cannot retrieve another student's assignment or file.
- A teacher can assign a permitted file and the student can retrieve it.

We chose [MIT](../LICENSE.md) because it is a short, permissive license that allows others to reuse and extend the code with the required notice. It does not make uploaded student data or learning materials public.

## 6. System vision and boundary

The system manages relationships, lesson requests and assignments. Teachers conduct lessons and make academic decisions outside the application. Payment collection and live lesson delivery are also outside it.

![System boundary](diagrams/system-boundary.svg)

The arrows show the information exchanged. Human actors and browsers are outside the service boundary. The application, database and protected file storage are inside. T1's Google Meet lessons remain outside the system, with no application-to-application integration. Update the diagram if a hosted identity, storage or notification service is later selected.

## 7. Main rules and constraints

- Protected actions require a valid token plus server-side role and ownership checks.
- Invitations match one student email, expire after seven days and are single-use.
- A student can request lessons only from a connected teacher. The booking uses the selected slot's stored times.
- Requests start as `pending`. Pending requests do not hold a slot exclusively. Only the teacher approves or rejects them.
- Approval rechecks availability and overlaps in one transaction. Adjacent lessons are allowed; overlapping approved lessons are not.
- Either participant can cancel a pending/approved booking before it starts. Rejected and cancelled states are final.
- A slot with pending or approved bookings cannot be removed until permitted bookings are cancelled.
- Teachers assign files only to connected students. Only that teacher and assigned student can retrieve them.
- Use PDF/JPEG/PNG files up to 10 MiB. Check their actual type and use safe filenames.
- API dates include a timezone offset. Store UTC; display local time. Reject invalid or past intervals.

The API and backlog use these rules. Hosting is not selected. The first tutor conversation is recorded above; broader user validation and usability tests remain planned.
