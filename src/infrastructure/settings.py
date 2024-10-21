import os
from dataclasses import dataclass
from typing import Any


def get_env_var(key: str, to_cast: Any, default: Any | None = None) -> Any:
    """
    Converting environment variable types
    ### Args:
        key (str): environment variable
        to_cast (Any): type to convert
        default (Any, optional): default value
    ### Raises:
        RuntimeError: occurs if such a variable is not found in .env and default is not set
    ### Returns:
        Any: an environment variable with a converted type
    """
    value = os.getenv(key)

    if not value and not default:
        raise RuntimeError(f"{key} environment variable not set")
    if not value:
        return default
    return to_cast(value)


@dataclass(frozen=True)
class DatabaseSettings:

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DB_URL(self) -> str:
        return "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST,
            self.POSTGRES_PORT,
            self.POSTGRES_DB,
        )

    @staticmethod
    def load_from_env() -> "DatabaseSettings":
        return DatabaseSettings(
            POSTGRES_HOST=get_env_var("POSTGRES_HOST", to_cast=str, default="postgres"),
            POSTGRES_PORT=get_env_var("POSTGRES_PORT", to_cast=int, default=5432),
            POSTGRES_USER=get_env_var("POSTGRES_USER", to_cast=str),
            POSTGRES_PASSWORD=get_env_var("POSTGRES_PASSWORD", to_cast=str),
            POSTGRES_DB=get_env_var("POSTGRES_DB", to_cast=str),
        )


@dataclass(frozen=True)
class Settings:

    db: DatabaseSettings

    @staticmethod
    def load_from_env() -> "Settings":
        return Settings(
            db=DatabaseSettings.load_from_env(),
        )


settings = Settings.load_from_env()
