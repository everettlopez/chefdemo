from sqlmodel import SQLModel, create_engine

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.SQL_ECHO,
    pool_pre_ping=True,
)


def initialize_database() -> None:
    from app import models  # noqa: F401

    SQLModel.metadata.create_all(engine)
