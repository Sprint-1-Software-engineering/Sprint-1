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

Validation tools stay in the repository. PR #58's local Python/SQLite authentication prototype is present on this feature branch, while the complete MVP backend is not implemented. Dashboard and announcement content is sample data and is not connected to the database. AI and parent features are deferred.

## Yerel giriş ve kayıt sunucusu

Bu feature branch'teki geçici HTTP sunucusunu proje kökünde çalıştırın:

```powershell
python src/server.py
```

Ardından `http://127.0.0.1:8000/register.html` veya `http://127.0.0.1:8000/login.html` adresini açın. Hesaplar `data/tutorbridge.db` dosyasındaki `users` tablosuna, oturumlar geçici olarak `auth_tokens` tablosuna kaydedilir. Oturum değeri veritabanında tutulan rastgele bearer token'dır; JWT seçimi yapılmamıştır. Kayıt ve giriş minimum 12 karakterlik şifreyi doğrular.

The current local auth smoke checks cover registration and login. They do not verify the complete booking, invitation or assignment workflows.

## Sprint 2 requirements draft

- [Detailed SRS](docs/sprint-2/SRS.md)
- [Refined product backlog](docs/Initial-Product-Backlog.md)
- [Stakeholder validation guide](docs/sprint-2/Stakeholder-Validation-Guide.md)

These requirements are prepared for peer review under [Issue #59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59). PR #58 remains a separate, unmerged implementation input. The profile addition and unresolved architecture decisions are identified in the SRS; NFR, Figma and architecture deliverables are not marked complete here.

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
