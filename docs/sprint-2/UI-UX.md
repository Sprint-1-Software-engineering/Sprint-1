# TutorBridge Sprint 2 UI/UX handoff

Owner: Kemal Efe Bilgisiçok (@kbilgisicok). Tracking: [Sprint 2 Issue #66](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/66). Coordinate cross-artifact traceability with Arda. Requirements baseline: [Sprint 2 SRS](SRS.md) and [product backlog](../Initial-Product-Backlog.md) on `develop` at `defcf7549109c20a39eb7fa23ce986df5115076a`.

- [Editable Figma design](https://www.figma.com/design/sUCAuJ5j1WEXdGBJKSc8QJ)
- [Figma prototype — Choose a journey](https://www.figma.com/proto/sUCAuJ5j1WEXdGBJKSc8QJ?page-id=0%3A1&node-id=1-3&starting-point-node-id=1%3A3&scaling=contain)
- Workspaces: [teacher](ui-ux/teacher-workspace.png), [student](ui-ux/student-workspace.png)
- Lesson request and decision: [student request](ui-ux/student-lesson-request.png), [teacher review](ui-ux/teacher-lesson-request.png), [approved](ui-ux/teacher-lesson-approved.png), [rejected](ui-ux/teacher-lesson-rejected.png)
- Homework: [teacher sharing](ui-ux/teacher-share-homework.png), [student detail](ui-ux/student-assignment-detail.png)
- [Screen and transition index](ui-ux/Screen-Flows.md)

## User flow diagrams

| Journey | Readable export | Editable source |
| --- | --- | --- |
| Invitation and connection | [SVG](ui-ux/invitation-flow.svg) | [Mermaid](ui-ux/invitation-flow.mmd) |
| Availability, lesson decisions and cancellation | [SVG](ui-ux/lesson-flow.svg) | [Mermaid](ui-ux/lesson-flow.mmd) |
| Homework sharing and file access | [SVG](ui-ux/homework-flow.svg) | [Mermaid](ui-ux/homework-flow.mmd) |

The diagrams describe the SRS decision paths. The homework flow checks access before showing metadata and checks it again before serving the file. The transition index records the current Figma links.

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
| [FR-11](SRS.md#fr-11), US-11 / #25 | Both lesson calendars show the participant, time and status. The prototype uses a chronological list. Date/status filters, invalid ranges, loading, results, empty lists and retry states are connected for both roles. |
| [FR-12](SRS.md#fr-12), US-12 / #26 | Show confirmation before a permitted cancellation and label the final state. The server enforces ownership and the strict before-start cutoff. |
| [FR-13](SRS.md#fr-13), US-13 / #27 | Share homework → Homework shared or File could not be attached. Accept PDF, JPEG or PNG up to 10 MiB and restrict selection to connected students. |
| [FR-14](SRS.md#fr-14), US-14 / #28 | Assignments → detail → download preview. Production checks access separately for metadata and file delivery. |
| [FR-02](SRS.md#fr-02) and [FR-15](SRS.md#fr-15), US-02 / #16 and US-15 / #60 | The demo launcher lets reviewers inspect both workspaces. Production routing derives the role from the authenticated profile. Sign-in, registration, invalid credentials, password errors and separate teacher/student loading routes are connected. Demo presets simulate profile roles; authentication is not implemented by Figma. |

Status is conveyed using text as well as color. The shared layout keeps the actor visible, presents the current task first and gives failed actions a recovery route. Demo dates and names are synthetic. Scenario jumps model separate actors and outcomes without shared runtime state. Dates use Europe/Istanbul. The prototype makes no cross-teacher conflict policy decision (SRS OD-06).

## Completed entry, recovery and calendar states — 23 November 2026

Toprak added 25 editable frames to the shared Figma file: seven authentication frames, two recovery frames, and eight calendar states per role. The original journeys remain available. A named Figma version records this completion.

- [Editable local Figma backup](ui-ux/completion/TutorBridge-Sprint2-2026-11-23.fig)
- Entry: [sign in](ui-ux/completion/auth-sign-in.png), [registration](ui-ux/completion/auth-create-account.png), [password error](ui-ux/completion/auth-registration-error.png).
- Recovery: [session expired](ui-ux/completion/auth-session-expired.png), [access denied](ui-ux/completion/s-access-denied.png).
- Calendar: [teacher filters](ui-ux/completion/t-calendar-filters.png), [student filters](ui-ux/completion/s-calendar-filters.png), [empty result](ui-ux/completion/s-calendar-empty.png), [retry](ui-ux/completion/s-calendar-retry.png).
- The completion folder contains 29 PNG exports: 25 new frames and four updated original screens. The editable design is the current source; older PNGs show earlier snapshots.

Sign-in uses explicitly labelled teacher/student demo accounts. Each passes through a separate progress screen and reaches the corresponding workspace after a 1.2-second prototype delay. The registration form shows the role field and 12–128-character password rule, with password-error and confirmation routes. Registration is a static scenario and does not persist a selected role or account.

Both calendars offer From, To and status presets, Europe/Istanbul (UTC+03:00), invalid-range feedback, loading with inactive Apply, results, empty results, Clear filters and recovery after a failed request. Loading uses an explicit Continue demo control. Retry retains the matching preset. These are fixed prototype scenarios, not working editable filters or API calls.

Session expiry leads to sign-in and then the role workspace, requiring deliberate re-entry instead of replaying a write. The denied-access screen contains no protected title, participant, filename or file URL. Both metadata and download-denial previews return to Assignments.

## Verification — 23 November 2026

Toprak's account had edit access to the shared design. The following paths were clicked in the Figma player:

| Path | Observed result |
| --- | --- |
| Start → Sign in → teacher preset | Progress → teacher workspace |
| Teacher calendar → Filters → no matches → Continue → Clear | Empty state → original teacher calendar |
| Teacher calendar → expired session → Sign in → student preset | Student workspace; no pending write replayed in the prototype |
| Student calendar → Filters → invalid range → Edit dates | Returned to the filter form |
| Student filters → failed request → Continue → Retry → Continue → Open lesson | Retry/loading/results → existing pending request |
| Start → Create account → password error → Edit details → Create account | Error recovery → confirmation → sign-in |
| Sign in → invalid credentials → Try again | Generic error → sign-in |
| Assignments → access denied → Back to assignments | Neutral denial → list |
| Assignment detail → download denied | Same neutral denial, without protected details |

All calendar button destinations were inspected in the editor; the table records representative clicked paths rather than claiming every combination was exercised. These checks are prototype navigation checks. No backend authorization, real login, file download, accessibility audit or user study was performed. A teammate must review the latest changes before merge; the author does not approve their own work.
