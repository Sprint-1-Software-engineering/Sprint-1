# TutorBridge

A web platform for private tutors and their existing students. The first release covers connections, lesson scheduling and assignment sharing.

## Documents

- [Project Proposal and System Vision](docs/Project-Proposal-and-System-Vision.md)
- [System Boundary](docs/diagrams/system-boundary.svg)
- [Roles and RACI](docs/Team-Members-and-RACI.md)
- [OpenAPI Draft](docs/Openapi.yaml)
- [Sprint 2 Architecture and diagrams](docs/sprint-2/Architecture.md)
- [Git-Flow Workflow](docs/Git-Flow-Workflow.md)
- [Initial Product Backlog](docs/Initial-Product-Backlog.md)
- [Individual Contributions](CONTRIBUTIONS.md)
- [MIT License](LICENSE.md)

The Sprint 1 documents originated from the team's three original drafts. Historical snapshot: [v0.1.0-sprint1](https://github.com/Sprint-1-Software-engineering/Sprint-1/tree/v0.1.0-sprint1). Current Sprint 2 work remains subject to its own review and release gates.

Validation tools stay in the repository. PR #58's local Python/SQLite authentication prototype is merged into `develop`; the complete MVP backend is not implemented. Dashboard and announcement content are sample data and are not connected to the database. PR #69 completed and merged the Sprint 2 Figma/UI-UX handoff. AI and parent features are deferred.

## Yerel giriş ve kayıt sunucusu

Geliştirme ortamında geçici HTTP sunucusunu proje kökünde çalıştırın:

```powershell
python src/server.py
```

Ardından `http://127.0.0.1:8000/register.html` veya `http://127.0.0.1:8000/login.html` adresini açın. Hesaplar `data/tutorbridge.db` dosyasındaki `users` tablosuna, oturumlar geçici olarak `auth_tokens` tablosuna kaydedilir. Oturum değeri veritabanında tutulan rastgele bearer token'dır; JWT seçimi yapılmamıştır. Kayıt ve giriş minimum 12 karakterlik şifreyi doğrular.

The current local auth smoke checks cover registration and login. They do not verify the complete booking, invitation or assignment workflows.

## Sprint 2 requirements and delivery candidate

- [Sprint 2 submission overview](docs/sprint-2/Submission-Overview.md)
- [Detailed SRS](docs/sprint-2/SRS.md)
- [Refined product backlog](docs/Initial-Product-Backlog.md)
- [Stakeholder validation guide](docs/sprint-2/Stakeholder-Validation-Guide.md)
- [NFR and quality measures](docs/sprint-2/NFR-and-Quality-Measures.md)
- [Review and test plan](docs/sprint-2/Review-and-Test-Plan.md)
- [UI/UX handoff](docs/sprint-2/UI-UX.md)
- [Team and process](docs/sprint-2/Team-and-Process.md)
- [Cross-artifact traceability](docs/sprint-2/Traceability.md)

These requirements are prepared for peer review under [Issue #59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59). PR #58 is merged and provides the local auth implementation input. The profile addition and unresolved technology decisions are identified in the SRS. The architecture proposal and editable diagrams were merged in [PR #70](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/70), not presented as a fully implemented or production-approved system. The Figma/UI-UX work is complete via merged [PR #69](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/69); NFR and test records are integrated through PR #73/#77/#80. Final decisions and release checks remain open.

## Sprint 2 environment and delivery

- [Local Development and Delivery](docs/sprint-2/Local-Development-and-Delivery.md): exact reference setup, storage, commands and known gaps.
- [Deployment and Recovery Handoff](docs/sprint-2/Deployment-and-Recovery.md): current local behavior and proposed deployment/data decisions.
- [Verification Report](docs/sprint-2/Verification-Report.md): actual checks and their limits, including the remaining input and browser validation scope.
- [Submission Checklist](docs/sprint-2/Submission-Checklist.md): required groups, owners, access, reviews and release gates.

The existing Sprint 1 checks validates documents/contracts. Sprint 2 structural validation and local auth smoke have separate scopes; an absent backend is not reported as tested. The supplied Sprint 2 Teams text does not mandate ZIP; confirm live instructions before submission.

## Sprint 1 Teams submission (historical)

One team member submits one ZIP containing all Sprint 1 documents and includes the repository URL in the Teams description. Proposal and Vision share one file; the diagram, contribution records and license are included. Check that the ZIP opens and matches the reviewed release tag.

Keep `mhmttemin` and `goksuyldrm` access, and add `nedima68` as required by the extra announcement. All three need at least Read access to this organization repository. Confirm that invitations are accepted, even though the repository is public.

The Proposal includes the team's 3 November 2026 conversation with one mathematics/software tutor. It records the current process, reported problem and response to the proposed system. Frequency and time cost are unmeasured; no broader validation or usability result is claimed.

Before submission, finish the missing individual work links and review this revision. At the latest access check, `mhmttemin` had Read; `goksuyldrm` and `nedima68` were not listed. No access changes are made by this document update. Open tasks: [Issue #5](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/5).
