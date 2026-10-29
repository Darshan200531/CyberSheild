import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "cybershield.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def initialize_database():
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(
            f"Schema file not found: {SCHEMA_PATH}"
        )

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        connection.executescript(schema)

        print("CyberShield database initialized successfully.")
        print(f"Database location: {DB_PATH}")


if __name__ == "__main__":
    initialize_database()