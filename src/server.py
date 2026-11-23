import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import uuid
from datetime import datetime, timedelta, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "tutorbridge.db"
EMAIL_LOCAL_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+$")
EMAIL_DOMAIN_PATTERN = re.compile(r"^[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$")


def connect_database():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():
    with connect_database() as database:
        database.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL CHECK (role IN ('teacher', 'student')),
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS auth_tokens (
                token TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_auth_tokens_user
                ON auth_tokens(user_id);
            """
        )


def hash_password(password):
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("ascii"), 200_000
    )
    return f"pbkdf2_sha256${salt}${digest.hex()}"


def verify_password(password, stored_hash):
    try:
        algorithm, salt, expected = stored_hash.split("$", 2)
        if algorithm != "pbkdf2_sha256":
            return False
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("ascii"), 200_000
        )
        return hmac.compare_digest(actual.hex(), expected)
    except (TypeError, ValueError):
        return False


def utc_now():
    return datetime.now(timezone.utc)


class TutorBridgeHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if urlparse(self.path).path == "/api/v1/users/me":
            self.get_current_user()
            return
        super().do_GET()

    def send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()

    def get_current_user(self):
        scheme, separator, token = self.headers.get("Authorization", "").partition(" ")
        if scheme.lower() != "bearer" or not separator or not token:
            self.send_json(401, {"code": "unauthorized", "message": "Giriş yapmanız gerekiyor."})
            return

        with connect_database() as database:
            user = database.execute(
                """
                SELECT users.id, users.name, users.email, users.role
                FROM auth_tokens
                JOIN users ON users.id = auth_tokens.user_id
                WHERE auth_tokens.token = ? AND auth_tokens.expires_at > ?
                """,
                (token, utc_now().isoformat()),
            ).fetchone()

        if user is None:
            self.send_json(401, {"code": "unauthorized", "message": "Oturum süreniz dolmuş. Yeniden giriş yapın."})
            return

        self.send_json(
            200,
            {"id": user["id"], "name": user["name"], "email": user["email"], "role": user["role"]},
        )

    def read_json(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length <= 0:
            return None
        try:
            raw_body = self.rfile.read(content_length)
            return json.loads(raw_body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/v1/auth/register":
            self.register_user()
        elif path == "/api/v1/auth/login":
            self.login_user()
        else:
            self.send_json(404, {"code": "not_found", "message": "Endpoint bulunamadı."})

    def register_user(self):
        data = self.read_json()
        if not isinstance(data, dict):
            self.send_json(400, {"code": "invalid_input", "message": "Geçersiz istek."})
            return

        unknown_fields = set(data) - {"name", "email", "password", "role"}
        if unknown_fields:
            self.send_json(400, {"code": "invalid_input", "message": "Desteklenmeyen istek alanı."})
            return

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        if not isinstance(name, str):
            self.send_json(400, {"code": "invalid_input", "message": "Ad ve soyadı metin olarak girin."})
            return
        name = name.strip()
        if not 1 <= len(name) <= 100:
            self.send_json(400, {"code": "invalid_input", "message": "Ad ve soyadı girin."})
            return
        if not isinstance(email, str):
            self.send_json(400, {"code": "invalid_input", "message": "Geçerli bir e-posta girin."})
            return
        email = email.strip().lower()
        if not 3 <= len(email) <= 254 or email.count("@") != 1:
            self.send_json(400, {"code": "invalid_input", "message": "Geçerli bir e-posta girin."})
            return
        local_part, domain = email.rsplit("@", 1)
        if (not 1 <= len(local_part) <= 64
                or local_part.startswith(".")
                or local_part.endswith(".")
                or ".." in local_part
                or not EMAIL_LOCAL_PATTERN.fullmatch(local_part)
                or not EMAIL_DOMAIN_PATTERN.fullmatch(domain)):
            self.send_json(400, {"code": "invalid_input", "message": "Geçerli bir e-posta girin."})
            return
        domain_labels = domain.split(".")
        if any(not label or len(label) > 63 or label.startswith("-") or label.endswith("-") for label in domain_labels):
            self.send_json(400, {"code": "invalid_input", "message": "Geçerli bir e-posta girin."})
            return
        if not isinstance(password, str):
            self.send_json(400, {"code": "invalid_input", "message": "Şifre metin olarak girilmelidir."})
            return
        if not 12 <= len(password) <= 128:
            self.send_json(400, {"code": "invalid_input", "message": "Şifre 12 ile 128 karakter arasında olmalıdır."})
            return
        if not isinstance(role, str):
            self.send_json(400, {"code": "invalid_input", "message": "Geçerli bir hesap türü seçin."})
            return
        if role not in ("teacher", "student"):
            self.send_json(400, {"code": "invalid_input", "message": "Geçerli bir hesap türü seçin."})
            return

        user_id = str(uuid.uuid4())
        created_at = utc_now().isoformat()

        try:
            with connect_database() as database:
                database.execute(
                    """
                    INSERT INTO users (id, name, email, password_hash, role, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (user_id, name, email, hash_password(password), role, created_at),
                )
        except sqlite3.IntegrityError:
            self.send_json(409, {"code": "conflict", "message": "Bu e-posta zaten kayıtlı."})
            return

        self.send_json(
            201,
            {"id": user_id, "name": name, "email": email, "role": role},
        )

    def login_user(self):
        data = self.read_json()
        if not isinstance(data, dict):
            self.send_json(400, {"code": "invalid_input", "message": "Geçersiz istek."})
            return

        unknown_fields = set(data) - {"email", "password"}
        if unknown_fields:
            self.send_json(400, {"code": "invalid_input", "message": "Desteklenmeyen istek alanı."})
            return

        email = data.get("email")
        password = data.get("password")
        if not isinstance(email, str) or not isinstance(password, str):
            self.send_json(400, {"code": "invalid_input", "message": "Geçersiz giriş bilgileri."})
            return
        email = email.strip().lower()

        with connect_database() as database:
            user = database.execute(
                "SELECT id, name, email, password_hash, role FROM users WHERE email = ?",
                (email,),
            ).fetchone()

            if user is None or not verify_password(password, user["password_hash"]):
                self.send_json(
                    401,
                    {"code": "unauthorized", "message": "E-posta veya şifre hatalı."},
                )
                return

            database.execute(
                "DELETE FROM auth_tokens WHERE user_id = ? OR expires_at <= ?",
                (user["id"], utc_now().isoformat()),
            )
            access_token = secrets.token_urlsafe(32)
            expires_at = utc_now() + timedelta(hours=1)
            database.execute(
                "INSERT INTO auth_tokens (token, user_id, expires_at) VALUES (?, ?, ?)",
                (access_token, user["id"], expires_at.isoformat()),
            )

        self.send_json(
            200,
            {
                "accessToken": access_token,
                "tokenType": "Bearer",
                "expiresIn": 3600,
            },
        )


if __name__ == "__main__":
    initialize_database()
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 8000), TutorBridgeHandler)
    print("TutorBridge http://127.0.0.1:8000", flush=True)
    print(f"Veritabanı: {DATABASE_PATH}", flush=True)
    server.serve_forever()
