import importlib.util
import json
import tempfile
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path


SERVER_PATH = Path(__file__).resolve().parents[1] / "src" / "server.py"
SPEC = importlib.util.spec_from_file_location("tutorbridge_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(server)


class AuthApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        server.DATABASE_PATH = Path(cls.temp_directory.name) / "tutorbridge.db"
        server.initialize_database()
        cls.http_server = ThreadingHTTPServer(("127.0.0.1", 0), server.TutorBridgeHandler)
        cls.thread = threading.Thread(target=cls.http_server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.http_server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.http_server.shutdown()
        cls.thread.join()
        cls.http_server.server_close()
        cls.temp_directory.cleanup()

    def request(self, method, path, payload=None):
        connection = HTTPConnection("127.0.0.1", self.port, timeout=5)
        body = None
        headers = {}
        if payload is not None:
            body = json.dumps(payload)
            headers["Content-Type"] = "application/json"
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        response_body = json.loads(response.read().decode("utf-8"))
        connection.close()
        return response.status, response_body

    def test_register_rejects_null_name(self):
        status, body = self.request("POST", "/api/v1/auth/register", {
            "name": None,
            "email": "null-name@example.test",
            "password": "Example-only-123",
            "role": "student",
        })
        self.assertEqual(status, 400)
        self.assertEqual(body["code"], "invalid_input")

    def test_register_rejects_malformed_email(self):
        for email in ("invalid@", "bad@@example.com", ".bad@example.com", "bad..name@example.com"):
            with self.subTest(email=email):
                status, body = self.request("POST", "/api/v1/auth/register", {
                    "name": "Valid Name",
                    "email": email,
                    "password": "Example-only-123",
                    "role": "student",
                })
                self.assertEqual(status, 400)
                self.assertEqual(body["code"], "invalid_input")

    def test_register_rejects_wrong_json_types(self):
        cases = [
            {"name": ["Name"], "email": "type@example.test", "password": "Example-only-123", "role": "student"},
            {"name": "Valid Name", "email": 123, "password": "Example-only-123", "role": "student"},
            {"name": "Valid Name", "email": "type@example.test", "password": ["password"], "role": "student"},
            {"name": "Valid Name", "email": "type@example.test", "password": "Example-only-123", "role": 1},
        ]
        for payload in cases:
            with self.subTest(payload=payload):
                status, body = self.request("POST", "/api/v1/auth/register", payload)
                self.assertEqual(status, 400)
                self.assertEqual(body["code"], "invalid_input")

    def test_register_rejects_unknown_fields(self):
        status, body = self.request("POST", "/api/v1/auth/register", {
            "name": "Valid Name",
            "email": "unknown@example.test",
            "password": "Example-only-123",
            "role": "student",
            "isAdmin": True,
        })
        self.assertEqual(status, 400)
        self.assertEqual(body["code"], "invalid_input")

    def test_valid_registration_and_login(self):
        status, body = self.request("POST", "/api/v1/auth/register", {
            "name": "Valid Name",
            "email": "valid@example.test",
            "password": "Example-only-123",
            "role": "teacher",
        })
        self.assertEqual(status, 201)
        self.assertEqual(set(body), {"id", "name", "email", "role"})

        status, body = self.request("POST", "/api/v1/auth/login", {
            "email": "VALID@example.test",
            "password": "Example-only-123",
        })
        self.assertEqual(status, 200)
        self.assertEqual(body["tokenType"], "Bearer")
        self.assertEqual(body["expiresIn"], 3600)
        self.assertTrue(body["accessToken"])


if __name__ == "__main__":
    unittest.main()
