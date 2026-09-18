from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings read from environment variables and an optional local .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="VERIRAG_",
        extra="ignore",
    )

    app_name: str = "VeriRAG"
    environment: str = "development"
    log_level: str = "INFO"
    sec_user_agent: str | None = None


@lru_cache
def get_settings() -> Settings:
    """Return one immutable settings instance per process."""

    return Settings()