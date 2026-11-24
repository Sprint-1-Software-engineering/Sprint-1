# Local development and delivery

Updated: 24 November 2026 under #83. Original DevOps owner: Osman Berke Ozdemir; integrated instructions refreshed by Toprak. Historical reference checks remain in [Verification-Report.md](Verification-Report.md).

## Current baseline

The reviewed develop branch includes the local Python standard-library HTTP server, SQLite, static HTML/CSS/JavaScript, opaque one-hour bearer sessions and `/api/v1/users/me`. Auth corrections are merged in PR #79; QA re-tests are merged in #80. There is no external database service, API key, npm runtime dependency or loaded `.env`. Python includes `sqlite3`; CI targets Python 3.12. Local checks have also used Python 3.14 on macOS and Python 3.12 on Windows. This is not a supported production-version matrix.

## Clean local start

Use a new folder; do not reset another contributor's checkout. Before release, the branch is a moving candidate:

```sh
git clone --branch develop https://github.com/Sprint-1-Software-engineering/Sprint-1.git TutorBridge-sprint2
cd TutorBridge-sprint2
python3 src/server.py
```

On Windows, use `py -3` if that is the installed launcher. After the release tag exists, checkout the actual submitted tag in this fresh clone to reproduce the final source. Do not use the old pinned PR #58 reference as the final product.

Open `http://127.0.0.1:8000/register.html`, then `login.html`. Use synthetic accounts. Registration enforces a 12-128-character password; login checks submitted credentials without stating a conflicting minimum. The fixed port is 8000; environment variables do not change it. Keep the terminal open; Ctrl+C stops the server. Do not stop an unknown process if the port is occupied.

## Storage and limitations

Startup creates `data/tutorbridge.db` outside the served `src` directory, with users and auth_tokens. Accounts persist across restart. A successful login replaces earlier tokens for that account; expiry is one hour. Logout removes the browser token only; server revocation is not implemented. Never commit the database, tokens, uploads or backups. For a disposable demo reset, stop the server and move its DB to private backup storage. Do not reset real data.

Implemented operations are registration, login and own profile. Connections, availability, bookings and assignments are planned. Both roles currently reach the same sample student dashboard (#61); Figma has separate designed role routes. The dashboard does not show live lesson or assignment data. Field error announcements, serving only frontend assets and login throttling are planned Sprint 3 work (#75). API source is currently accessible through `/server.py`; the source is also public in GitHub. No hosted-security or full-MVP acceptance is claimed.

## Repeatable checks

From the checkout, use a temporary environment for documentation dependencies:

```sh
python3 -m venv /tmp/tutorbridge-docs-venv
/tmp/tutorbridge-docs-venv/bin/python -m pip install -r requirements-docs.txt
/tmp/tutorbridge-docs-venv/bin/python scripts/check_submission.py
python3 scripts/check_sprint2.py --release-ready
python3 -m unittest discover -s tests -v
python3 scripts/check_auth_environment.py --validation-probes --report /tmp/tutorbridge-auth-validation.json
```

Use a suitable temporary path on Windows. Documentation checking needs the packages in requirements-docs.txt; application code itself has only standard-library dependencies. Git must be on PATH for delivery-tool tests. The auth runner copies source into temporary storage and uses synthetic accounts; port 8000 must be free. It does not use the real checkout's database. Current QA records 42 passing automated tests without expected failures; that is separate from the 15-check startup/storage/restart smoke and extra validation probes. Run checks again for the actual release commit and preserve the report.

## Final handoff

Use [Submission-Checklist.md](Submission-Checklist.md) and [Traceability.md](Traceability.md). Review a develop-to-main PR; after independent approval and merge, tag the final main commit with an unused Sprint 2 version. Build with `scripts/build_delivery.py` using that exact tag. Preview packages are labelled DRAFT. Keep ZIP delivery local/chat; no public asset upload. Verify live Teams attachment requirements and evaluator/Figma access before submission.
