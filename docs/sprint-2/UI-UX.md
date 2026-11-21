# TutorBridge Sprint 2 UI/UX handoff

Owner: Kemal Efe Bilgisiçok (@kbilgisicok). Tracking: [Sprint 2 Issue #66](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/66). Coordinate cross-artifact traceability with Arda. Requirements baseline: [Sprint 2 SRS](SRS.md) and [product backlog](../Initial-Product-Backlog.md) on `develop` at `defcf7549109c20a39eb7fa23ce986df5115076a`.

- [Editable Figma design](https://www.figma.com/design/sUCAuJ5j1WEXdGBJKSc8QJ)
- [Figma prototype — Choose a journey](https://www.figma.com/proto/sUCAuJ5j1WEXdGBJKSc8QJ?page-id=0%3A1&node-id=1-3&starting-point-node-id=1%3A3&scaling=contain)
- [Teacher workspace PNG](ui-ux/teacher-workspace.png)
- [Screen and transition index](ui-ux/Screen-Flows.md)

## Walkthroughs

1. **Connect an existing student.** Teacher workspace → Students → Invite a student → Create invitation → Invitation ready. Share the sample code outside TutorBridge. Follow **Try the student journey** → Accept invitation → Invitation accepted; the invite scenario uses Noah's account. **Preview expired code** opens recovery instructions.
2. **Publish availability and request a lesson.** Teacher workspace → Availability → Add a slot → Publish slot. The student can follow My teachers → Elif's availability → Choose Friday at 16:00 → Send request to preview the newly published slot. The Thursday slot demonstrates the cross-role decision scenario. The UI includes empty availability, overlapping slots, a blocked slot removal and a stale-request conflict.
3. **Decide and cancel.** On the student side, choose Thursday and send the request. From the teacher workspace, open **Review request** to approve, reject, cancel a pending request, or preview an approval conflict. The successful decisions link to the student outcome. Both roles can confirm or dismiss cancellation before the start. Rejected and cancelled screens lead back to navigation or a fresh slot.
4. **Share and read homework.** Teacher workspace → Share homework → select a connected student, title, instructions and sample file → Share assignment. **See student's assignment** opens Maya's detail. She can also reach it via Assignments. The prototype offers a file-validation branch and a download outcome preview.

## Design decisions and traceability

| SRS / story | Screen and decision |
| --- | --- |
| [FR-03](SRS.md#fr-03), US-03 / #17 | Invite a student → Invitation ready. Address the single-use code to the student's account email, state seven-day expiry and share externally. |
| [FR-04](SRS.md#fr-04), US-04 / #18 | Accept an invitation → Invitation accepted or Invitation expired. Production must validate the signed-in email and consume the code atomically. |
| [FR-05](SRS.md#fr-05), US-05 / #19 | Students / My teachers. Limit actions to existing relationships. There is no public directory. |
| [FR-06](SRS.md#fr-06), US-06 / #20 | Add a slot → Slot published or Slot overlaps. Show the local timezone and allow adjacent intervals. |
| [FR-07](SRS.md#fr-07), US-07 / #21 | Elif's availability / No open times. Show future slots with a clear empty state. Pending requests alone leave a slot visible. |
| [FR-08](SRS.md#fr-08), US-08 / #22 | Availability → Slot removed or Slot could not be removed. Preserve slots with active bookings. |
| [FR-09](SRS.md#fr-09), US-09 / #23 | Request a lesson → Request sent or Request could not be sent. Confirm teacher and time, then use Pending until approval. Refresh stale availability after conflict. |
| [FR-10](SRS.md#fr-10), US-10 / #24 | Lesson request from Maya → approved, rejected or approval conflict. Server-side approval must recheck overlapping approved teacher lessons atomically. |
| [FR-11](SRS.md#fr-11), US-11 / #25 | Both lesson calendars show the participant, time and status. The prototype uses a chronological list. Production filters and empty calendar lists remain to be designed. |
| [FR-12](SRS.md#fr-12), US-12 / #26 | Show confirmation before a permitted cancellation and label the final state. The server enforces ownership and the strict before-start cutoff. |
| [FR-13](SRS.md#fr-13), US-13 / #27 | Share homework → Homework shared or File could not be attached. Accept PDF, JPEG or PNG up to 10 MiB and restrict selection to connected students. |
| [FR-14](SRS.md#fr-14), US-14 / #28 | Assignments → detail → download preview. Production checks access separately for metadata and file delivery. |
| [FR-02](SRS.md#fr-02) and [FR-15](SRS.md#fr-15), US-02 / #16 and US-15 / #60 | The demo launcher lets reviewers inspect both workspaces. Production routing derives the role from the authenticated profile. Authentication and registration screens are outside this handoff. |

Status is conveyed using text as well as color. The shared layout keeps the actor visible, presents the current task first and gives failed actions a recovery route. Demo dates and names are synthetic. Scenario jumps model separate actors and outcomes without shared runtime state. Dates use Europe/Istanbul. The prototype makes no cross-teacher conflict policy decision (SRS OD-06).

## Verification and open work

- Figma document inspection confirmed 48 editable frames, three flow starting points, and all 152 configured click destinations.
- Rendered and visually inspected the teacher workspace PNG. The Figma Starter connector limit prevented additional frame exports during this pass.
- The Sprint 2 structural check, all 14 existing delivery-tool unit tests and the staged whitespace check passed locally. The Sprint 1 contract check stopped at import because PyYAML was unavailable in the local Python runtime.
- Still to verify with a teammate: Present-mode playback, reviewer access to the design and prototype, and the remaining screen exports. In Figma, select the student workspace, lesson decision and assignment frames, then use **Export → PNG**.
- Loading, unauthorized/forbidden screens, responsive widths, keyboard focus and accessibility testing need implementation or design follow-up. For production, show a loading state during mutations, preserve user input on recoverable errors and explain forbidden access without revealing protected records.
- The prototype uses fixed demo scenarios. No backend behavior, live file transfer, stakeholder feedback or end-to-end product tests were exercised. AI, parents, payments and video calls are outside scope.
