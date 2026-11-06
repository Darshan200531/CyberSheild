import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-change-me")
    DATABASE_PATH = os.getenv(
        "DATABASE_PATH", str(BASE_DIR / "instance" / "cybershield.db")
    )
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH_MB", "5")) * 1024 * 1024
    JSON_SORT_KEYS = False
