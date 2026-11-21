# TutorBridge prototype transitions

Each action moves to the named destination frame. Screens after the launcher also offer **Switch demo journey** to return to Start.

| Frame | Click target → destination |
| --- | --- |
| Start · One place for tutoring | Teacher workspace → T Home<br>Student workspace → S Home |
| T Home · Your workspace | Review request → T Request<br>Students → T Students<br>Availability → T Availability<br>Lesson calendar → T Calendar<br>Share homework → T Homework |
| T Students · Students | Invite a student → T Invite<br>Workspace → T Home |
| T Invite · Invite a student | Create invitation → T Code<br>Back to students → T Students |
| T Code · Invitation ready | Back to students → T Students<br>Try the student journey → S Invite |
| T Availability · Availability | Add a slot → T Slot<br>Remove unused slot → T Removed<br>Try removing booked slot → T Slot Locked<br>Workspace → T Home |
| T Slot · Add a slot | Publish slot → T Published<br>Preview overlap → T Slot Conflict<br>Back to availability → T Availability |
| T Published · Slot published | Back to availability → T Availability |
| T Removed · Slot removed | Back to availability → T Availability |
| T Slot Locked · Slot could not be removed | Review request → T Request<br>Back to availability → T Availability |
| T Slot Conflict · Slot overlaps | Edit times → T Slot |
| T Calendar · Lesson calendar | Review Maya’s request → T Request<br>Open Leo’s lesson → T Leo<br>Workspace → T Home |
| T Leo · Lesson with Leo | Cancel lesson → T Cancel<br>Back to calendar → T Calendar |
| T Request · Lesson request from Maya | Approve → T Approved<br>Reject → T Rejected<br>Cancel request → T Cancel Pending<br>Preview approval conflict → T Conflict<br>Back to calendar → T Calendar |
| T Approved · Lesson approved | Cancel lesson → T Cancel Approved<br>Back to workspace → T Home<br>See student’s approved state → S Approved |
| T Rejected · Request rejected | Back to workspace → T Home<br>See student’s rejected state → S Rejected |
| T Conflict · Approval could not be saved | Back to request → T Request<br>Back to calendar → T Calendar |
| T Cancel · Cancel Leo’s lesson? | Confirm cancellation → T Cancelled Leo<br>Keep lesson → T Leo |
| T Cancel Approved · Cancel Maya’s lesson? | Confirm cancellation → T Cancelled<br>Keep lesson → T Approved |
| T Cancel Pending · Cancel Maya’s request? | Confirm cancellation → T Cancelled<br>Keep request → T Request |
| T Cancelled · Maya’s booking cancelled | Workspace → T Home<br>See student’s cancelled state → S Cancelled |
| T Cancelled Leo · Leo’s lesson cancelled | Workspace → T Home |
| T Homework · Share homework | Share assignment → T Shared<br>Preview file error → T File Error<br>Workspace → T Home |
| T File Error · File could not be attached | Back to assignment → T Homework |
| T Shared · Homework shared | See student’s assignment → S Assignment<br>Workspace → T Home |
| S Home · Your workspace | My teachers → S Teachers<br>Accept invitation → S Invite<br>Lesson calendar → S Calendar<br>Assignments → S Homework |
| S Teachers · My teachers | View Elif’s availability → S Slots<br>Accept invitation → S Invite<br>Workspace → S Home |
| S Invite · Accept an invitation | Accept invitation → S Connected<br>Preview expired code → S Invite Error<br>Workspace → S Home |
| S Connected · Invitation accepted | Return to Maya’s demo → S Home |
| S Invite Error · Invitation expired | Try another code → S Invite |
| S Slots · Elif’s availability | Choose Thursday at 15:00 → S Confirm<br>Choose Friday at 16:00 → S Confirm Fri<br>Preview empty availability → S Empty<br>Back to teachers → S Teachers |
| S Empty · No open times | Back to availability → S Slots |
| S Confirm · Request a lesson | Send request → S Pending<br>Preview slot conflict → S Conflict<br>Choose another time → S Slots |
| S Confirm Fri · Request Friday’s lesson | Send request → S Pending Fri<br>Choose another time → S Slots |
| S Pending · Request sent | Open lesson calendar → S Calendar<br>Cancel request → S Cancel |
| S Pending Fri · Friday request sent | Cancel request → S Cancel Fri<br>Back to workspace → S Home |
| S Conflict · Request could not be sent | Refresh availability → S Slots |
| S Calendar · Lesson calendar | Open Thursday request → S Pending<br>Workspace → S Home |
| S Approved · Lesson with Elif | Cancel lesson → S Cancel Approved<br>Workspace → S Home |
| S Rejected · Request declined | View available times → S Slots<br>Workspace → S Home |
| S Cancel · Cancel your request? | Confirm cancellation → S Cancelled<br>Keep request → S Pending |
| S Cancel Approved · Cancel your lesson? | Confirm cancellation → S Cancelled<br>Keep lesson → S Approved |
| S Cancel Fri · Cancel your Friday request? | Confirm cancellation → S Cancelled Fri<br>Keep request → S Pending Fri |
| S Cancelled · Booking cancelled | View available times → S Slots<br>Workspace → S Home |
| S Cancelled Fri · Friday request cancelled | View available times → S Slots<br>Workspace → S Home |
| S Homework · Assignments | Open Linear equations → S Assignment<br>Workspace → S Home |
| S Assignment · Linear equations | Preview download outcome → S Download<br>Back to assignments → S Homework |
| S Download · Download preview | Back to assignment → S Assignment |

## Follow-up review

The original transition table remains the inventory of wired Figma screens. The [Figma construction instructions](Figma-Completion.md) define the pending frames, labels, buttons and destinations. The [handoff](../UI-UX.md#pending-figma-states-and-entry-flows) lists the pending authentication, calendar, loading and access-recovery transitions. Use the [invitation](invitation-flow.svg), [lesson](lesson-flow.svg), and [homework](homework-flow.svg) diagrams to review the SRS decision paths.
