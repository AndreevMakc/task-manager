from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI PostgreSQL Project"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    PG_HOST: str = os.getenv("PG_HOST", "localhost")
    PG_USER: str = os.getenv("PG_USER", "postgres")
    PG_PASS: str = os.getenv("PG_PASS", "postgres")
    PG_DB: str = os.getenv("PG_DB", "app")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @property
    def get_database_url(self) -> str:
        if self.SQLALCHEMY_DATABASE_URI:
            return self.SQLALCHEMY_DATABASE_URI
        return f"postgresql://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DB}"


settings = Settings()
