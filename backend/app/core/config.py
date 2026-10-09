import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

BACKEND_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(BACKEND_ROOT / ".env")


class Settings:
    DATABASE_URL: str
    SQL_ECHO: bool
    FRONTEND_ORIGINS: list[str]

    def __init__(self) -> None:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise RuntimeError(
                "DATABASE_URL is not set. Run 'python setup_database.py' once from "
                "the backend directory to save your local MySQL connection settings."
            )
        self.DATABASE_URL = database_url
        self.SQL_ECHO = os.getenv("SQL_ECHO", "false").strip().lower() in {
            "1",
            "true",
            "yes",
        }
        origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:5173")
        self.FRONTEND_ORIGINS = [origin.strip() for origin in origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
