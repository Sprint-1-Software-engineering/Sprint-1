"""Repeatable QA checks for the local TutorBridge auth API (Sprint 2, Issue #72).

Scope: registration, login and the current-user profile of src/server.py. The
cases and their IDs match docs/sprint-2/Review-and-Test-Plan.md. Expected
values come from docs/sprint-2/SRS.md and docs/Openapi.yaml.

Each run uses a temporary SQLite database and a random localhost port. Only
synthetic accounts are used and no token, password or hash is printed. This is
an API check against the Python handler, not a browser or end-to-end test.
"""
import importlib.util
import json
import socket
import sqlite3
import sys
import tempfile
import threading
import time
import unittest
from datetime import datetime, timedelta, timezone
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

SERVER_PATH = Path(__file__).resolve().parents[1] / "src" / "server.py"
SPEC = importlib.util.spec_from_file_location("tutorbridge_server_quality", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(server)

PASSWORD = "Example-only-123"  # synthetic value, not a credential
PUBLIC_USER_KEYS = ["email", "id", "name", "role"]


class QuietHandler(server.TutorBridgeHandler):
    def log_message(self, *args):
        pass


class QuietServer(ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address):
        pass  # unhandled handler exceptions are asserted through responses, not stderr noise


class AuthQualityTests(unittest.TestCase):
    counter = 0
    counter_lock = threading.Lock()

    @classmethod
    def setUpClass(cls):
        cls.temp_directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        server.DATABASE_PATH = Path(cls.temp_directory.name) / "data" / "tutorbridge.db"
        server.initialize_database()
        cls.http_server = QuietServer(("127.0.0.1", 0), QuietHandler)
        cls.thread = threading.Thread(target=cls.http_server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.http_server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.http_server.shutdown()
        cls.thread.join()
        cls.http_server.server_close()
        cls.temp_directory.cleanup()

    # ------------------------------------------------------------ helpers
    @classmethod
    def email(cls, prefix="qa"):
        with cls.counter_lock:
            AuthQualityTests.counter += 1
            return f"{prefix}{AuthQualityTests.counter}@example.test"

    def request(self, method, path, payload=None, headers=None, raw=None):
        send_headers = dict(headers or {})
        body = raw
        if payload is not None:
            body = json.dumps(payload)
            send_headers["Content-Type"] = "application/json"
        elif raw is not None:
            send_headers["Content-Type"] = "application/json"
        connection = HTTPConnection("127.0.0.1", self.port, timeout=10)
        try:
            connection.request(method, path, body=body, headers=send_headers)
            response = connection.getresponse()
            data = response.read().decode("utf-8")
            try:
                parsed = json.loads(data)
            except ValueError:
                parsed = None
            return response.status, parsed
        finally:
            connection.close()

    def register(self, **overrides):
        payload = {"name": "QA User", "email": self.email(), "password": PASSWORD, "role": "student"}
        payload.update(overrides)
        payload = {key: value for key, value in payload.items() if value is not Ellipsis}
        return self.request("POST", "/api/v1/auth/register", payload)

    def login(self, email, password=PASSWORD):
        return self.request("POST", "/api/v1/auth/login", {"email": email, "password": password})

    def profile(self, token=None, header=None):
        headers = {}
        if header is not None:
            headers["Authorization"] = header
        elif token is not None:
            headers["Authorization"] = "Bearer " + token
        return self.request("GET", "/api/v1/users/me", headers=headers)

    def new_session(self, role="student"):
        email = self.email()
        status, body = self.register(email=email, role=role)
        self.assertEqual(status, 201)
        status, body = self.login(email)
        self.assertEqual(status, 200)
        return email, body["accessToken"]

    def database(self):
        return sqlite3.connect(server.DATABASE_PATH)

    # ------------------------------------------------------------ registration (FR-01)
    def test_r01_r02_valid_registration_returns_public_fields_only(self):
        for case_id, role in (("R-01", "teacher"), ("R-02", "student")):
            with self.subTest(case=case_id):
                status, body = self.register(role=role)
                self.assertEqual(status, 201)
                self.assertEqual(sorted(body), PUBLIC_USER_KEYS)
                self.assertEqual(body["role"], role)

    def test_r03_r04_duplicate_email_is_rejected_without_second_account(self):
        email = self.email()
        self.assertEqual(self.register(email=email)[0], 201)
        for case_id, variant in (("R-03", email), ("R-04", "  " + email.upper() + "  ")):
            with self.subTest(case=case_id):
                self.assertEqual(self.register(email=variant)[0], 409)
        count = self.database().execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,)).fetchone()[0]
        self.assertEqual(count, 1)

    def test_r05_r08_password_length_boundaries(self):
        for case_id, length, expected in (("R-05", 11, 400), ("R-06", 12, 201), ("R-07", 128, 201), ("R-08", 129, 400)):
            with self.subTest(case=case_id, length=length):
                self.assertEqual(self.register(password="p" * length)[0], expected)

    def test_r09_r25_role_must_be_teacher_or_student(self):
        for case_id, role in (("R-09", "admin"), ("R-25", 1)):
            with self.subTest(case=case_id):
                self.assertEqual(self.register(role=role)[0], 400)

    def test_r10_extra_malformed_emails(self):
        for case_id, email in (("R-10b", "no-at-sign.example.com"), ("R-10c", "@example.com"),
                               ("R-10d", "bad@example"), ("R-10e", "bad name@example.com")):
            with self.subTest(case=case_id, email=email):
                self.assertEqual(self.register(email=email)[0], 400)

    def test_r13_r16_name_boundaries_and_turkish_characters(self):
        for case_id, name, expected in (("R-13", "     ", 400), ("R-14", "n" * 100, 201), ("R-15", "n" * 101, 400),
                                        ("R-12", 123, 400)):
            with self.subTest(case=case_id):
                self.assertEqual(self.register(name=name)[0], expected)
        with self.subTest(case="R-16"):
            status, body = self.register(name="Berat Erdem Yalçın")
            self.assertEqual(status, 201)
            self.assertEqual(body["name"], "Berat Erdem Yalçın")

    def test_r17_r18_email_length_boundaries(self):
        local = "a" * 64
        valid_254 = f"{local}@{'x' * 63}.{'y' * 63}.{'z' * 61}"
        too_long_255 = f"{local}@{'x' * 63}.{'y' * 63}.{'z' * 62}"
        self.assertEqual(len(valid_254), 254)
        self.assertEqual(len(too_long_255), 255)
        with self.subTest(case="R-17"):
            self.assertEqual(self.register(email=valid_254)[0], 201)
        with self.subTest(case="R-18"):
            self.assertEqual(self.register(email=too_long_255)[0], 400)

    def test_r19_each_required_field_is_required(self):
        for case_id, field in (("R-19a", "name"), ("R-19b", "email"), ("R-19c", "password"), ("R-19d", "role")):
            with self.subTest(case=case_id, missing=field):
                self.assertEqual(self.register(**{field: Ellipsis})[0], 400)

    def test_r21_r23_request_body_shapes(self):
        for case_id, raw in (("R-21", ""), ("R-22", "{not json"), ("R-23", "[1, 2]")):
            with self.subTest(case=case_id):
                self.assertEqual(self.request("POST", "/api/v1/auth/register", raw=raw)[0], 400)

    def test_r24_password_null_is_rejected(self):
        self.assertEqual(self.register(password=None)[0], 400)

    # ------------------------------------------------------------ login (FR-02)
    def test_l01_valid_login_response_shape(self):
        email = self.email()
        self.assertEqual(self.register(email=email)[0], 201)
        status, body = self.login(email)
        self.assertEqual(status, 200)
        self.assertEqual(sorted(body), ["accessToken", "expiresIn", "tokenType"])
        self.assertEqual((body["tokenType"], body["expiresIn"]), ("Bearer", 3600))
        self.assertTrue(body["accessToken"])

    def test_l02_login_email_is_case_insensitive(self):
        email = self.email()
        self.assertEqual(self.register(email=email)[0], 201)
        self.assertEqual(self.login(email.upper())[0], 200)

    def test_l03_l04_failed_logins_are_generic_and_identical(self):
        email = self.email()
        self.assertEqual(self.register(email=email)[0], 201)
        wrong_status, wrong_body = self.login(email, "wrong-password-123")
        unknown_status, unknown_body = self.login("nobody-here@example.test")
        self.assertEqual((wrong_status, unknown_status), (401, 401))
        self.assertEqual(wrong_body, unknown_body)

    def test_l05_l08_login_input_validation(self):
        email = self.email()
        self.assertEqual(self.register(email=email)[0], 201)
        cases = (("L-05", {"email": email}), ("L-06", {"email": None, "password": PASSWORD}),
                 ("L-07", {"email": email, "password": PASSWORD, "extra": 1}))
        for case_id, payload in cases:
            with self.subTest(case=case_id):
                self.assertEqual(self.request("POST", "/api/v1/auth/login", payload)[0], 400)
        with self.subTest(case="L-08"):
            self.assertEqual(self.request("POST", "/api/v1/auth/login", raw="")[0], 400)

    # ------------------------------------------------------------ token and profile (FR-02, FR-15)
    def test_t01_valid_token_returns_own_profile_only(self):
        email, token = self.new_session("teacher")
        status, body = self.profile(token)
        self.assertEqual(status, 200)
        self.assertEqual(sorted(body), PUBLIC_USER_KEYS)
        self.assertEqual((body["email"], body["role"]), (email, "teacher"))

    def test_t02_t04_missing_malformed_and_unknown_credentials_get_401(self):
        cases = (("T-02", {}), ("T-03a", {"header": "Bearer"}), ("T-03b", {"header": "Bearer "}),
                 ("T-03c", {"header": "Token abc"}), ("T-03d", {"header": "abc"}),
                 ("T-03e", {"header": "Basic dXNlcjpwYXNz"}), ("T-04", {"token": "unknown-" + "x" * 40}))
        for case_id, kwargs in cases:
            with self.subTest(case=case_id):
                status, body = self.profile(**kwargs)
                self.assertEqual(status, 401)
                self.assertEqual(sorted(body), ["code", "message"])

    def test_t05_expired_token_gets_401(self):
        _, token = self.new_session()
        past = (datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat()
        with self.database() as database:
            database.execute("UPDATE auth_tokens SET expires_at = ? WHERE token = ?", (past, token))
        self.assertEqual(self.profile(token)[0], 401)

    def test_t06_session_lifetime_is_one_hour(self):
        _, token = self.new_session()
        with self.database() as database:
            expires_at = database.execute("SELECT expires_at FROM auth_tokens WHERE token = ?", (token,)).fetchone()[0]
        remaining = (datetime.fromisoformat(expires_at) - datetime.now(timezone.utc)).total_seconds()
        self.assertTrue(3590 <= remaining <= 3600, f"remaining lifetime {remaining:.0f} s")

    def test_t07_token_works_before_expiry_and_fails_after(self):
        _, token = self.new_session()
        soon = (datetime.now(timezone.utc) + timedelta(seconds=3)).isoformat()
        with self.database() as database:
            database.execute("UPDATE auth_tokens SET expires_at = ? WHERE token = ?", (soon, token))
        before = self.profile(token)[0]
        time.sleep(3.3)
        after = self.profile(token)[0]
        self.assertEqual((before, after), (200, 401))

    def test_t08_profiles_follow_their_own_account_and_role(self):
        teacher_email, teacher_token = self.new_session("teacher")
        student_email, student_token = self.new_session("student")
        self.assertEqual(self.profile(teacher_token)[1]["role"], "teacher")
        self.assertEqual(self.profile(student_token)[1]["role"], "student")
        self.assertNotEqual(self.profile(teacher_token)[1]["email"], self.profile(student_token)[1]["email"])

    # ------------------------------------------------------------ storage and integrity
    def test_o07_password_is_stored_as_salted_hash(self):
        email = self.email()
        self.assertEqual(self.register(email=email)[0], 201)
        stored = self.database().execute("SELECT password_hash FROM users WHERE email = ?", (email,)).fetchone()[0]
        self.assertTrue(stored.startswith("pbkdf2_sha256$"))
        self.assertNotIn(PASSWORD, stored)

    def test_p03_simultaneous_duplicate_registrations_create_one_account(self):
        email = self.email("race")
        statuses = []
        lock = threading.Lock()

        def attempt():
            status, _ = self.register(email=email)
            with lock:
                statuses.append(status)

        threads = [threading.Thread(target=attempt) for _ in range(8)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(sorted(statuses), [201] + [409] * 7)
        count = self.database().execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,)).fetchone()[0]
        self.assertEqual(count, 1)

    # ------------------------------------------------------------ known defect
    @unittest.expectedFailure
    def test_p01_non_numeric_content_length_returns_400(self):
        """Known defect, Issue #71: the server closes the connection without a response.

        Remove the expectedFailure marker when #71 is fixed; an unexpected success
        will then remind the team to do so.
        """
        raw = ("POST /api/v1/auth/register HTTP/1.1\r\nHost: x\r\nContent-Type: application/json\r\n"
               "Content-Length: abc\r\nConnection: close\r\n\r\n{}")
        connection = socket.create_connection(("127.0.0.1", self.port), timeout=5)
        try:
            connection.sendall(raw.encode("ascii"))
            received = b""
            try:
                while True:
                    part = connection.recv(4096)
                    if not part:
                        break
                    received += part
            except socket.timeout:
                pass
        finally:
            connection.close()
        status_line = received.split(b"\r\n", 1)[0].decode("ascii", "replace")
        self.assertIn(" 400 ", status_line)


if __name__ == "__main__":
    unittest.main()
