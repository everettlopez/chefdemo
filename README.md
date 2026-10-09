# Full-Stack React + FastAPI Starter

A modular starter for a React, TypeScript, and Vite frontend backed by FastAPI, SQLModel, Alembic, and MySQL.

## Requirements

- Python 3.12 or newer
- Node.js 20 or newer and npm
- MySQL 8 or a compatible MySQL server

## Backend

```bash
cd backend
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux/macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure the MySQL server is running, then create the database once before starting the backend. For the `chef_db` database used during setup, run this in MySQL Workbench or another MySQL client:

```sql
CREATE DATABASE chef_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

You can choose a different database name, but it must already exist and you must enter that exact name during configuration. Creating the database is separate from creating a MySQL user: use the username and password of a MySQL account that has permission to access that database.

Configure the database connection once:

```bash
python setup_database.py
```

Enter the connection details when prompted. For the local MySQL setup, use:

```text
MySQL host:     localhost
MySQL port:     3306
Database name:  chef_db
MySQL username: root
MySQL password: (your MySQL password; input is hidden)
```

Press Enter to accept the displayed defaults for host, port, database, and username, or type the values you use. Type your MySQL password at the hidden password prompt. This setup writes the connection URL to a local `backend/.env` file. It is excluded by `.gitignore`, so it will not be pushed to the repository. Keep it private and never remove its ignore rule or commit it.

After that one-time setup, start the backend directly with Uvicorn whenever you work on the project:

```bash
uvicorn app.main:app --reload
```

Run that command from the `backend` directory with its virtual environment activated. The backend reads the saved local connection settings and serves on <http://localhost:8000>.

If startup reports `Unknown database`, create the database first and confirm that the entered database name matches it exactly. If MySQL reports `Access denied`, check the username/password and that the account has permission to connect to the selected database.

The backend is available at <http://localhost:8000>. Interactive API documentation is at <http://localhost:8000/docs>. Check <http://localhost:8000/health> and <http://localhost:8000/api/test>.

For convenience, install Taskipy (`pip install taskipy`) and run `task run`, `task migrate`, or `task makemigrations` from the backend directory. `makemigrations` creates a migration named `update`. Alembic migrations are the recommended way to manage schema changes. The app also calls `SQLModel.metadata.create_all()` on startup to make a fresh development database usable without a migration; this does not replace migrations or alter existing tables.

## Frontend

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend is available at <http://localhost:5173>. It calls `GET /api/test` on startup and displays the response.

## Project layout

```text
frontend/       React application and Vite configuration
backend/app/    API routes, SQLModel models/schemas, services, and database setup
backend/alembic/Database migration environment and revisions
tasks.md        Starter ideas for extending the project
```

## Extending the starter

- Add SQLModel table definitions under `backend/app/models/` and import them in `backend/app/models/__init__.py`.
- Add request/response models under `backend/app/schemas/`.
- Put database/business operations in `backend/app/services/` and expose them through route modules.
- Register new route modules in `backend/app/api/router.py`.
- Generate and apply schema changes with `alembic revision --autogenerate -m "describe the change"` and `alembic upgrade head`. These commands use the local connection settings created by `python setup_database.py`.

The sample `Item` API includes `GET /api/items` and `POST /api/items`.
