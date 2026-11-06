import sqlite3
from pathlib import Path

def get_connection(database_path):
    Path(database_path).parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def init_db(database_path):
    schema_path = Path(__file__).with_name("schema.sql")
    schema = schema_path.read_text(encoding="utf-8")
    with get_connection(database_path) as connection:
        connection.executescript(schema)
        connection.commit()

def fetch_one(database_path, query, params=()):
    with get_connection(database_path) as connection:
        row = connection.execute(query, params).fetchone()
        return dict(row) if row else None

def fetch_all(database_path, query, params=()):
    with get_connection(database_path) as connection:
        rows = connection.execute(query, params).fetchall()
        return [dict(row) for row in rows]
