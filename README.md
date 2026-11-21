# TutorBridge: Sprint 1

A web platform for private tutors and their existing students. The first release covers connections, lesson scheduling and assignment sharing.

## Documents

- [Project Proposal and System Vision](docs/Project-Proposal-and-System-Vision.md)
- [System Boundary](docs/diagrams/system-boundary.svg)
- [Roles and RACI](docs/Team-Members-and-RACI.md)
- [OpenAPI Draft](docs/Openapi.yaml)
- [Architecture](docs/sprint-2/Architecture.md)
- [Git-Flow Workflow](docs/Git-Flow-Workflow.md)
- [Initial Product Backlog](docs/Initial-Product-Backlog.md)
- [Individual Contributions](CONTRIBUTIONS.md)
- [MIT License](LICENSE.md)

This revision is based on the team's three original drafts and awaits peer review. Previous snapshot: [v0.1.0-sprint1](https://github.com/Sprint-1-Software-engineering/Sprint-1/tree/v0.1.0-sprint1). This ZIP contains nine files in total; the combined Proposal/Vision counts as one file.

## Yerel giriş ve kayıt sunucusu

Frontend'i ve SQLite kullanıcı veritabanını çalıştırmak için proje kökünde:

```powershell
python src/server.py
```

Ardından `http://127.0.0.1:8000/register.html` veya `http://127.0.0.1:8000/login.html` adresini açın. Hesaplar `data/tutorbridge.db` dosyasındaki `users` tablosuna, oturumlar geçici olarak `auth_tokens` tablosuna kaydedilir. Oturum değeri veritabanında tutulan rastgele bearer token'dır; JWT seçimi yapılmamıştır. Kayıt ve giriş minimum 12 karakterlik şifreyi doğrular; giriş doğrulaması anlık HTTP API davranışıdır.

Validation tools stay in the repository. A local authentication backend, registration/login screens, and an example OBS-style student dashboard are implemented. Dashboard and announcement content is sample data and is not connected to the database. AI and parent features are deferred.

## Teams submission

One team member submits one ZIP containing all Sprint 1 documents and includes the repository URL in the Teams description. Proposal and Vision share one file; the diagram, contribution records and license are included. Check that the ZIP opens and matches the reviewed release tag.

Keep `mhmttemin` and `goksuyldrm` access, and add `nedima68` as required by the extra announcement. All three need at least Read access to this organization repository. Confirm that invitations are accepted, even though the repository is public.

The Proposal includes the team's 3 November 2026 conversation with one mathematics/software tutor. It records the current process, reported problem and response to the proposed system. Frequency and time cost are unmeasured; no broader validation or usability result is claimed.

Before submission, finish the missing individual work links and review this revision. At the latest access check, `mhmttemin` had Read; `goksuyldrm` and `nedima68` were not listed. No access changes are made by this document update. Open tasks: [Issue #5](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/5).
