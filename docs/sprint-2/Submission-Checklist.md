# Sprint 2 Submission Checklist

Owner: Osman Berke Özdemir (@makucheez). Tracking: [#63](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/63). DevOps implementation: [PR #64](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/64), merged into `develop` at [`defcf75`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/defcf7549109c20a39eb7fa23ce986df5115076a).
Readiness: **not ready for final submission**. Review date: 23 November 2026. Repository evidence reflects the reviewed develop baseline in the [verification report](Verification-Report.md).

## Source and deadline

The team-supplied copy of the Teams assignment states 24 November 2026, 23:59 Türkiye time (UTC+03:00), weight 20%, and permits multiple submissions. It requires the four groups below plus team/repository, release/tag, owners and artifact links. The assignment copy does not specify ZIP. Live Teams instructions and attachment format have not been accessed in this session; the submitting member must verify them before upload. Do not carry forward the old Sprint 1 ZIP rule automatically.

The supplied BM321 semester rubric places first working MVP and 50% unit-test coverage CI in Sprint 3, and one-command Docker operation in the final submission. Current smoke verification does not establish 50% coverage or full MVP acceptance. Document names below are team proposals, not instructor-mandated names or quotas.

## Four required delivery groups

| Group | Owner / dependency | Current evidence and remaining gate |
|---|---|---|
| Detailed SRS and refined backlog | Toprak | [SRS](SRS.md) and [backlog](../Initial-Product-Backlog.md) merged in [PR #62](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/62) at [`ece4918`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/ece4918dbed158904ca31ce6bae0645549255633). Reconcile historical auth notes and close or explicitly defer the open SRS decisions. |
| NFR and quality-measure specification | Berat | [NFRs](NFR-and-Quality-Measures.md), [review and test plan](Review-and-Test-Plan.md), auth QA suite and latency baseline script merged in [PR #73](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/73) at [`67e3ebf`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/67e3ebf67cbad5d3579907e5521328e9f137bb99). [PR #77](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/77) proposes follow-up documentation and review links and is still open at [`dedbfcb`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/dedbfcbc94a70dc24e83bb6e303e04a8c020ce3c). |
| Figma prototype and user flows | Kemal with Arda | [UI/UX handoff](UI-UX.md) includes the editable design and prototype links, local .fig backup, PNG exports, editable Mermaid flows and SVGs. Completion merged in [PR #69](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/69) at [`fe10e2a`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/fe10e2ad107a72453ae3a0a88cc8cbbc51031e82). Confirm evaluator access and review export findings in [#76](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/76). |
| C4/UML architecture | Mehmet with Osman's deployment support | [Architecture](Architecture.md) and editable Mermaid sources were introduced alongside the local auth prototype in [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58) at [`2bb7a4a`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/2bb7a4a5ee1cea2e73cc7a02f1acfbf42d797add), then updated in [PR #70](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/70) at [`ec696e3`](https://github.com/Sprint-1-Software-engineering/Sprint-1/commit/ec696e35de50affe53051a0f1aa45dab6160639c). C4 context/container, UML domain and auth/booking sequences are present. Stack and deployment choices still require a team decision. |

- [ ] Confirm Figma design and prototype access from an evaluator account. Review [#76](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/76) export findings and record their disposition. The handoff records representative prototype clicks by Toprak. The QA follow-up reports a partial export review and leaves the live Figma review pending.
- [ ] Review [PR #77](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/77) and resolve or explicitly defer open findings: [#71](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/71) expected auth failure, [#74](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/74) login password message, [#75](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/75) hardening/accessibility proposals and role routing in [#61](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61). Keep QA baselines, proposed thresholds and planned browser, accessibility, usability and domain tests distinct.
- [ ] Confirm the backend direction and local/hosted database choices, token lifecycle and logout/revocation, hosting/HTTPS, private file storage, monitoring, backup/recovery and migrations. Align the SRS, OpenAPI, architecture and runbook with recorded decisions. The integrated local baseline uses Python/SQLite and opaque bearer tokens at port 8000.
- [ ] Record the disposition of remaining SRS decisions, including role entry, stakeholder validation, cross-teacher booking conflicts and pagination. Keep planned invitation, booking and assignment behavior distinct from the implemented auth slice.

## Team, contributions and review

Repository: [Sprint-1-Software-engineering/Sprint-1](https://github.com/Sprint-1-Software-engineering/Sprint-1).

| Member / GitHub | Sprint 2 responsibility |
|---|---|
| Toprak Daldal / toprakdaldal | Product, SRS and backlog |
| Mehmet Ali Demircioğlu / mehmetalidmrcgl-hue | Architecture, schema, API/code decisions |
| Berat Erdem Yalçın / SunsetEva | Quality, NFR and tests |
| Osman Berke Özdemir / makucheez | Local environment, CI, deployment and delivery |
| Kemal Efe Bilgisiçok / kbilgisicok | Figma and UI/UX |
| Arda Demir / ardmr26 | Process, user flows and traceability |

Student IDs and RACI are in [the team record](../Team-Members-and-RACI.md). Actual authored work/reviews belong in [contributions](../../CONTRIBUTIONS.md).

- [ ] Each member records their own real Issue, commit, PR and review links; assignment alone is not completed-work evidence.
- [ ] Every release-bound PR has another person's review of its latest changes; no self-approval or bypass merge.
- [ ] Mehmet and Berat independently reproduce/check the [local procedure](Local-Development-and-Delivery.md); no teammate run is recorded yet.
- [ ] Complete or locate the team/process record and cross-artifact traceability from FR/NFR to Issues, Figma, API, architecture and verification. The readiness tool currently reports `Team-and-Process.md` and `Traceability.md` missing. If equivalent evidence uses different team-agreed paths, link it and align the tooling before release.

## Access and CI gates

23 November branch summaries using makucheez: both branches report protected; their branch summaries retain required context `Sprint 1 checks`, enforcement `everyone`. Confirm the full approval and conversation rules with a repository administrator.

The 19 November collaborator listing contained `mhmttemin` with Read; `goksuyldrm` and `nedima68` were absent at that check. Reconfirm their current access before submission. The existing README asks for all three. An administrator must resolve the stated evaluator-access requirement and verify acceptance. No permissions were modified.

- [ ] Preserve required `Sprint 1 checks`, PR/review/conversation requirements and administrator enforcement.
- [ ] Review successful CI logs on the exact integrated/release SHA, not an old feature or reference SHA.
- [ ] Re-run integrated checks on the release candidate. The 23 November develop run discovered 42 tests (41 passed, one expected failure for #71) and passed the separate 15-check integrated smoke. See the [CI evidence](Verification-Report.md#23-november-2026--integrated-develop-verification).
- [ ] Run `python3 scripts/check_sprint2.py --release-ready`; adapt proposed file paths if the team agrees different names. This only checks structural integration, not full release approval.
- [ ] Independently inspect Figma and remote document/diagram access; local-link validation is not permission verification.
- [ ] Ensure no real secrets, student records, SQLite databases, uploads or backups are tracked or packaged.

## Release and package procedure

The 23 November develop baseline includes merged Sprint 2 work. Complete the outstanding evidence and decisions before preparing the develop-to-main release. Refresh the [draft description](Release-PR-Draft.md) using the reviewed release candidate.

- [ ] Integrate team artifacts via independently reviewed feature PRs into develop.
- [ ] Refresh refs and open a **draft** develop -> main release PR with the prepared description and actual evidence. Fill in real Issue/PR/review, Figma and CI links.
- [ ] Run/check the full release candidate; resolve failures and obtain independent latest-push review before merge.
- [ ] Merge through the protected workflow only after all gates; do not push directly to main.
- [ ] Fetch main, identify the final reviewed SHA and choose an unused Sprint 2 tag, proposed `v0.2.0-sprint2`. This tag has not been created.
- [ ] Create a new tag at that final main commit after approval; never move Sprint 1 or existing tags.
- [ ] Run `python3 scripts/build_delivery.py --ref v0.2.0-sprint2 --output-dir /tmp/tutorbridge-delivery` after `git fetch origin main --tags`. The tool requires the tag to equal origin/main and all structural team paths to exist in the tagged tree; manual gates still apply.
- [ ] Open and inspect the resulting ZIP, manifest SHA and file hash; verify its source commit matches the actual assessed tag. A ZIP is a convenient local package, not proof Teams requires it.
- [ ] One member submits through Teams before the deadline, including team/roles, repository, actual tag and real artifact links; verify upload completion.

A preview package is explicitly marked DRAFT and is not a release or completed team submission. Deliver packages through chat/local files. Do not upload ZIPs as public GitHub release assets unless the user separately requests it.
