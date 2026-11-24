# Sprint 2 traceability

Updated: 24 November 2026. Author: Toprak Daldal. Tracking: [#81](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/81). Source baseline: develop `1897f24`. This matrix connects existing artifacts; it does not create new requirements or mark product stories complete.

## Sources and status

- [SRS](SRS.md): FR-01 to FR-15 and their AC/BR rules.
- [Backlog](../Initial-Product-Backlog.md): epics, features, story/task owners, priority, estimates and dependencies. Each row below links the existing story and task; no Issue IDs or implementation assignments are replaced.
- [API contract](../Openapi.yaml): paths below are relative to `/api/v1`. One shared contract covers the complete planned MVP; only three auth/profile operations are implemented.
- [Figma design](https://www.figma.com/design/sUCAuJ5j1WEXdGBJKSc8QJ), [prototype](https://www.figma.com/proto/sUCAuJ5j1WEXdGBJKSc8QJ?page-id=0%3A1&node-id=1-3&starting-point-node-id=1%3A3&scaling=contain), [UI/UX handoff](UI-UX.md) and [named-frame transition index](ui-ux/Screen-Flows.md).
- [Architecture](Architecture.md): C4 boundary/container views and UML domain/auth/booking models. The [context](../diagrams/TutorBridge-context.mmd) and [container](../diagrams/TutorBridge-container.mmd) views apply across all rows.
- [Review/test plan](Review-and-Test-Plan.md), [NFR](NFR-and-Quality-Measures.md) and [dated verification report](Verification-Report.md): executed results, observations and plans are distinct.

A Figma frame name identifies the design scenario, not working server behavior. API tests cover registration, login and profile only; connections, lessons and assignment tests remain planned. A mapped test is not a passing test. PR approval is not acceptance of all proposed quality thresholds.

## Functional requirements

All frame names below resolve through the linked transition index. Test IDs refer to the review/test plan; AC details remain in the SRS.

| SRS | Story / task | Contract method and path | Figma frames | Architecture | Test cases | Evidence boundary |
| --- | --- | --- | --- | --- | --- | --- |
| [FR-01](SRS.md) | [US-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/15) / [T-01](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/29) | `POST /auth/register` | Auth Create account / Registration error | [User, AuthToken](../diagrams/TutorBridge-auth-sequence.mmd) | [R-01 to R-27, UI-09](Review-and-Test-Plan.md) | API implemented and tested; UI has QA findings |
| [FR-02](SRS.md) | [US-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/16) / [T-02](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/30) | `POST /auth/login` | Auth Sign in / Signing in teacher / Signing in student | [User, AuthToken](../diagrams/TutorBridge-auth-sequence.mmd) | [L-01 to L-08, T-03 to T-10, UI-01/02/06](Review-and-Test-Plan.md) | API tested; runtime role entry fails (#61) |
| [FR-03](SRS.md) | [US-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/17) / [T-03](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/31) | `POST /invitations` | T Invite / T Code | [Invitation, Relationship](../diagrams/TutorBridge-domain.mmd) | [INV-01 to INV-05, ROL-01](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-04](SRS.md) | [US-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/18) / [T-04](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/32) | `POST /invitations/accept` | S Invite / S Connected / S Invite Error | [Invitation, Relationship](../diagrams/TutorBridge-domain.mmd) | [ACC-01 to ACC-07, ROL-02](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-05](SRS.md) | [US-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/19) / [T-05](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/33) | `GET /teachers/me/students; GET /students/me/teachers` | T Students / S Teachers | [User, Relationship](../diagrams/TutorBridge-domain.mmd) | [LST-01 to LST-03, ROL-03](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-06](SRS.md) | [US-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/20) / [T-06](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/34) | `POST /availability` | T Availability / T Slot / T Slot Conflict | [Availability](../diagrams/TutorBridge-domain.mmd) | [AVL-01 to AVL-04, ROL-04/09](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-07](SRS.md) | [US-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/21) / [T-07](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/35) | `GET /availability` | S Slots / S Empty | [Availability, Booking](../diagrams/TutorBridge-domain.mmd) | [AVL-05 to AVL-09](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-08](SRS.md) | [US-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/22) / [T-08](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/36) | `DELETE /availability/{id}` | T Removed / T Slot Locked | [Availability, Booking](../diagrams/TutorBridge-domain.mmd) | [AVL-10 to AVL-12](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-09](SRS.md) | [US-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/23) / [T-09](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/37) | `POST /bookings` | S Confirm / S Pending / S Conflict | [Booking, Availability, Relationship](../diagrams/TutorBridge-booking-sequence.mmd) | [BKG-01 to BKG-05, ROL-05](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-10](SRS.md) | [US-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/24) / [T-10](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/38) | `PATCH /bookings/{id}/status` | T Request / T Approved / T Rejected / T Conflict | [Booking](../diagrams/TutorBridge-booking-sequence.mmd) | [BKG-06 to BKG-11, ROL-06](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-11](SRS.md) | [US-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/25) / [T-11](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/39) | `GET /bookings` | T Calendar / S Calendar; role-specific filters, results, empty and retry | [Booking](../diagrams/TutorBridge-domain.mmd) | [BKG-12 to BKG-14](Review-and-Test-Plan.md) | Figma paths reviewed; API tests planned |
| [FR-12](SRS.md) | [US-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/26) / [T-12](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/40) | `PATCH /bookings/{id}/status` | T/S Cancel, Cancel Approved, Cancelled | [Booking](../diagrams/TutorBridge-booking-sequence.mmd) | [BKG-15 to BKG-18](Review-and-Test-Plan.md) | Design and planned tests; no endpoint |
| [FR-13](SRS.md) | [US-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/27) / [T-13](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/41) | `POST /assignments` | T Homework / T File Error / T Shared | [Assignment, AssignmentFile, Relationship](../diagrams/TutorBridge-domain.mmd) | [ASG-01 to ASG-08, ROL-07](Review-and-Test-Plan.md) | Figma preview; API tests planned |
| [FR-14](SRS.md) | [US-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/28) / [T-14](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/42) | `GET /assignments; GET /assignments/{id}; GET /assignments/{id}/file` | S Homework / S Assignment / S Download / S Access denied | [Assignment, AssignmentFile](../diagrams/TutorBridge-domain.mmd) | [ASG-09 to ASG-12](Review-and-Test-Plan.md) | Figma preview; API access tests planned |
| [FR-15](SRS.md) | [US-15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/60) / [T-15](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61) | `GET /users/me` | Auth role routes / T Home / S Home | [User, AuthToken](../diagrams/TutorBridge-auth-sequence.mmd) | [T-01/02/04/05/08, UI-01](Review-and-Test-Plan.md) | Own-profile API tested; full runtime role entry not accepted |

## Quality requirements

Every ID from the NFR is included below. Numeric targets, owners, environments and detailed status remain in the NFR table; this index does not accept proposed targets.

| NFR | Related FR / artifact | Verification link and current boundary |
| --- | --- | --- |
| [SEC-01](NFR-and-Quality-Measures.md) | FR-02/15; AuthToken | [T-05 to T-07; shortened-expiry and stored-lifetime checks passed; real one-hour wait not run](Review-and-Test-Plan.md) |
| [SEC-02](NFR-and-Quality-Measures.md) | All protected APIs; FR-15 implemented | [T-02 to T-05; profile credential matrix passed; domain checks planned](Review-and-Test-Plan.md) |
| [SEC-03](NFR-and-Quality-Measures.md) | FR-03 to FR-14; relationship/ownership | [ROL cases; planned domain authorization](Review-and-Test-Plan.md) |
| [SEC-04](NFR-and-Quality-Measures.md) | FR-14; homework-flow and AssignmentFile | [ASG-10/11/12; metadata and file checks planned](Review-and-Test-Plan.md) |
| [SEC-05](NFR-and-Quality-Measures.md) | FR-01/02/15; User, AuthToken | [R-01/26, L-01, T-01; response/storage checks; logs not fully reviewed](Review-and-Test-Plan.md) |
| [SEC-06](NFR-and-Quality-Measures.md) | FR-01; OpenAPI Register | [R-05 to R-25; boundaries and wrong types tested](Review-and-Test-Plan.md) |
| [SEC-07](NFR-and-Quality-Measures.md) | FR-13; private files | [ASG-02 to ASG-08; size/type/path cases planned](Review-and-Test-Plan.md) |
| [SEC-08](NFR-and-Quality-Measures.md) | All APIs; Deployment-and-Recovery.md | [Hosted HTTPS verification planned; no hosted environment](Review-and-Test-Plan.md) |
| [SEC-09](NFR-and-Quality-Measures.md) | Static serving; proposed #75 | [O-06: source served; allowlist proposal pending](Review-and-Test-Plan.md) |
| [SEC-10](NFR-and-Quality-Measures.md) | FR-02; proposed #75 | [O-05: no throttling; policy decision pending](Review-and-Test-Plan.md) |
| [PERF-01](NFR-and-Quality-Measures.md) | FR-15 and future list/calendar APIs | [measure_auth_latency.py: profile baseline measured; lists planned](Review-and-Test-Plan.md) |
| [PERF-02](NFR-and-Quality-Measures.md) | FR-01/02 | [measure_auth_latency.py: local auth baseline; proposed target not accepted](Review-and-Test-Plan.md) |
| [PERF-03](NFR-and-Quality-Measures.md) | FR-09/10 | [Concurrent booking latency planned](Review-and-Test-Plan.md) |
| [PERF-04](NFR-and-Quality-Measures.md) | FR-13/14 | [Maximum-size transfer latency planned](Review-and-Test-Plan.md) |
| [USE-01](NFR-and-Quality-Measures.md) | FR-09; S Confirm to S Pending | [UI-08: real participant session planned; no usability result](Review-and-Test-Plan.md) |
| [USE-02](NFR-and-Quality-Measures.md) | FR-03 to FR-14; Figma flows | [UI-07: partial export review; Toprak prototype paths in UI-UX.md; not full live QA](Review-and-Test-Plan.md) |
| [USE-03](NFR-and-Quality-Measures.md) | FR-01/02; login/register forms | [UI-03/04/05: headless keyboard/labels checked; error announcements fail; #75 pending](Review-and-Test-Plan.md) |
| [USE-04](NFR-and-Quality-Measures.md) | FR-01/02; validation messages | [UI-02/09; #74 fixed and re-tested, closed](Review-and-Test-Plan.md) |
| [USE-05](NFR-and-Quality-Measures.md) | FR-02/15; runtime role entry | [UI-01: both roles enter sample student dashboard; #61 open](Review-and-Test-Plan.md) |
| [REL-01](NFR-and-Quality-Measures.md) | FR-10; booking-sequence | [BKG-10: atomic conflicting approval test planned](Review-and-Test-Plan.md) |
| [REL-02](NFR-and-Quality-Measures.md) | FR-01/04/13; transaction boundaries | [P-03: duplicate registration tested; invitation/upload faults planned](Review-and-Test-Plan.md) |
| [REL-03](NFR-and-Quality-Measures.md) | FR-01/02; invalid JSON/headers | [P-01: #71 fixed and closed; unknown API GET error format remains a recorded gap](Review-and-Test-Plan.md) |
| [REL-04](NFR-and-Quality-Measures.md) | Deployment-and-Recovery.md | [Synthetic recovery history in Verification-Report.md; QA timed target test planned](Review-and-Test-Plan.md) |
| [MNT-01](NFR-and-Quality-Measures.md) | Application tests and CI | [Coverage not measured; 50% course target belongs to Sprint 3](Review-and-Test-Plan.md) |
| [MNT-02](NFR-and-Quality-Measures.md) | FR-01 to FR-15; this matrix | [All FRs mapped; mapping does not accept implementation](Review-and-Test-Plan.md) |
| [MNT-03](NFR-and-Quality-Measures.md) | tests/ and sprint2-checks.yml | [42 automated tests pass at 7fccc47; linked CI in test plan](Review-and-Test-Plan.md) |
| [MNT-04](NFR-and-Quality-Measures.md) | SRS, API, code, diagrams | [Limits reviewed by QA; historical wording dated; open consistency notes below](Review-and-Test-Plan.md) |
| [MNT-05](NFR-and-Quality-Measures.md) | GitHub defect records | [Closed #71/#74, open #75/#76/#61; unknown-GET-format tracking still needed](Review-and-Test-Plan.md) |

## Integration evidence

| Artifact / result | GitHub record | Scope |
| --- | --- | --- |
| Requirements/backlog | [PR #62](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/62) / [#59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59) | Detailed requirements and planned implementation |
| Auth/profile implementation | [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58) and [PR #79](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/79) | Three implemented operations; role-specific UI remains open |
| UI/UX and flows | [PR #67](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/67) and [PR #69](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/69) / [#66](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/66) | Editable source, exports and representative prototype checks |
| Architecture | [PR #70](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/70) | C4/UML design and editable/readable diagrams |
| Quality and re-tests | [PR #73](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/73), [PR #77](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/77), [PR #80](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/80) / [#72](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/72) | Planned versus executed cases, all-pass auth regression results, headless findings |
| Environment/CI | [PR #64](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/64) and [PR #78](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/78) / [#63](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/63) | Integrated API/QA/tooling checks; not hosted acceptance |
| Process and cross-artifact matrix | [#81](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/81) | This new change requires independent review |

## Open consistency and decision notes

1. The architecture UML BookingStatus says `declined`, but SRS FR-10/11 and OpenAPI use `rejected`. Mehmet and Toprak should align the model and regenerate the readable export before final consistency sign-off. The contract remains the reference; this matrix does not silently introduce a new state.
2. QA identifies four unresolved expected behaviors: INV-05 repeated active invitation; BKG-05 requesting a past slot; BKG-11 approving after the start; ASG-04 empty-file rejection/status. Toprak and Mehmet must record decisions and update SRS/contract/tests together. No test result is invented for these cases.
3. Proposed NFR targets, session concurrency/revocation, hosting/recovery, cross-teacher student conflicts and pagination remain in the owners' decision registers. Open design questions are not implementation completion.
4. Role-specific auth routing remains a runtime gap (#61). Figma role routes do not close it. The shared loading exports intentionally show the same progress state with different outgoing destinations (#76 clarity suggestions).
5. Team roster and contribution history remain unchanged. Toprak authored this process/matrix handover; future implementation owners remain those in the backlog.

## Maintaining the matrix

When a requirement changes, update its AC, contract, backlog, affected model/frame and test expected value in the same reviewed change. When implementation changes, re-run the affected tests and record the exact commit, environment and limits. Update CONTRIBUTIONS.md with actual author/review links. At release, use the final tag and exact-commit CI evidence in the submission checklist; do not reuse this baseline as proof of final readiness.
