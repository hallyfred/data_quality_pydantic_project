import os

from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine


ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


def load_database() -> Engine:
    """Cria e devolve uma engine SQLAlchemy para o PostgreSQL."""
    load_dotenv(ENV_FILE)

    required_variables = ("POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB")
    missing_variables = [name for name in required_variables if not os.getenv(name)]
    if missing_variables:
        missing = ", ".join(missing_variables)
        raise RuntimeError(f"Defina as variáveis no arquivo .env: {missing}")

    database_url = URL.create(
        "postgresql+psycopg",
        username=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        database=os.environ["POSTGRES_DB"],
    )

    return create_engine(database_url, pool_pre_ping=True)


