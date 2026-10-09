from getpass import getpass
from pathlib import Path
from urllib.parse import quote_plus


BACKEND_ROOT = Path(__file__).resolve().parent
ENV_FILE = BACKEND_ROOT / ".env"


def prompt_value(label: str, default: str) -> str:
    value = input(f"{label} [{default}]: ").strip()
    return value or default


def main() -> None:
    print("Configure the local MySQL connection for this project.")
    host = prompt_value("MySQL host", "localhost")
    port = prompt_value("MySQL port", "3306")
    database = prompt_value("Database name", "chef_db")
    username = prompt_value("MySQL username", "root")
    password = getpass("MySQL password (input hidden): ")

    if not port.isdecimal():
        raise ValueError("MySQL port must be a number.")

    database_url = (
        f"mysql+pymysql://{quote_plus(username)}:{quote_plus(password)}"
        f"@{host}:{port}/{quote_plus(database)}"
    )
    ENV_FILE.write_text(f"DATABASE_URL={database_url}\n", encoding="utf-8")
    print(f"Database connection saved locally to {ENV_FILE.name} (git-ignored).")
    print("You can now start the backend with: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()
