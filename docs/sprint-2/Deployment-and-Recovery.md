# Deployment, Data and Recovery Handoff

Owner: Osman Berke Özdemir. Architecture handoff for Mehmet; proposed decisions awaiting team review. Tracking: [#63](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/63).

## Current environment versus target

The only verified environment is the pinned local PR #58 Python/SQLite auth reference, started with `python3 src/server.py`, bound to `127.0.0.1:8000`. Python serves static files from `src`; account/session data is in `data/tutorbridge.db` outside that directory. It has no container, reverse proxy, public TLS endpoint, hosting service, migration framework or implemented assignment storage. [Verification](Verification-Report.md) covers local operation only.

Proposed demonstration target: one host, one application instance and persistent local SQLite storage. Keep SQLite on the application's local persistent disk; do not assume a shared network filesystem or multi-replica deployment is supported. Hosting provider, OS, domain, budget, capacity and retention remain open decisions (OD-04 in the requirements draft). No production deployment has been carried out.

If the team later selects a public deployment, replace the development HTTP server with a supported serving arrangement, provide HTTPS and deliberate origin/bind configuration, and review the frontend's fixed local API URL. Do not expose the current prototype by merely binding it to all interfaces. Mehmet owns the application changes and contract agreement; Osman owns the environment/runbook integration. The full product's one-command Docker operation is a final-course deliverable; Sprint 2 documents its intended direction without claiming implementation.

## Proposed resource and file boundaries

| Resource | Current / planned handling |
|---|---|
| Application source | Reviewed Git commit, read-only to the running service where practical |
| SQLite | Current `data/tutorbridge.db`; persistent outside public static paths and build artifacts; private OS permissions |
| Sessions | Current `auth_tokens` contains bearer values; treat entire DB and backups as confidential; one-hour expiry is implemented |
| Assignment files | Not implemented; propose private persistent `uploads/`, server-authorized download, content/size checks and sanitized filenames |
| Configuration | Current prototype reads no env file; future variable names only in `.env.example`, real values outside Git |
| Logs | Operational events without passwords, authorization headers, invitation codes, student content or raw request bodies |
| Backups | Private storage outside Git and web roots; restricted operator access; encryption and retention to be selected before real data |

A Docker volume, if adopted, must preserve SQLite and future protected uploads across container replacement. It is not enough to preserve the image. Do not add fabricated Docker variables that this server does not consume. Provide a non-root container and a health/readiness approach when container implementation is scheduled.

## Backup and restore approach

Proposed starting policy for team approval: take a consistent backup before deployments and before schema changes; consider daily backups only once real usage requires them. Proposed recovery goals are at most 24 hours of data loss and restoration within one hour, unmeasured and unapproved. These are discussion targets, not achieved NFRs. Berat should reconcile any accepted values with the NFR specification.

For a local SQLite snapshot, stop the demo server for the simplest quiescent procedure, or use Python's SQLite backup API rather than copying an active database file. Supply a private destination outside the checkout:

```sh
python3 - <<'PY'
import sqlite3
from pathlib import Path
if not Path('data/tutorbridge.db').is_file():
    raise SystemExit('Source database does not exist; stop and verify the checkout.')
backup = Path.home() / 'TutorBridge-private-backups' / 'before-deploy.db'
backup.parent.mkdir(parents=True, exist_ok=True)
if backup.exists():
    raise SystemExit('Choose a new backup name; existing backup is preserved.')
with sqlite3.connect('data/tutorbridge.db') as source:
    with sqlite3.connect(backup) as destination:
        source.backup(destination)
        assert destination.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
print('Private backup created and integrity checked; protect it as confidential data.')
PY
```

This command is a proposed operator procedure. Its successful use with user data has not been claimed. Only a synthetic backup/restore rehearsal is reported separately. Future assignment files and metadata must be backed up as a consistent set; a database-only backup cannot recover missing uploads.

Restore: stop the application; preserve the current private data as a separate recovery copy; integrity-check the chosen backup; restore it at the documented data path; run a compatible reviewed code revision; verify login/profile using an authorized test account; then resume service. Restrict file access after restore. Decide explicitly whether restored sessions must be invalidated; current code has no operator revocation command. Do not alter real session tables without an approved procedure.

## Deployment rollback

Record the exact release SHA, data backup identity and any schema changes before deploying. To roll back, stop the service and select the previous compatible reviewed release. Current initialization only creates tables/indexes: it is not a reversible migration system. Do not assume old code can safely read a future schema. Restore the matching data/files only after assessing lost writes and obtaining the operator's data-recovery decision. Never move old tags or rewrite Git history.

## Architecture review decisions still required

- Mehmet/Toprak: Python versus Express, opaque session versus JWT, logout/revocation and correct API base URL.
- Mehmet/Osman: host, supported Python version, server process, persistent paths, permissions and deployment health checks.
- Berat/Osman: measurable recovery targets, approved retention and a future authorized restore exercise.
- Mehmet: include these boundaries and accepted decisions in Architecture.md/C4 deployment view; this handoff is not a replacement for his complete C4/UML architecture set.
