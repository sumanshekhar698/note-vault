from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "NoteVault"
    debug: bool = False
    database_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()

# @lru_cache on get_settings() caches the returned Settings instance for the lifetime of the process (unless you call get_settings.cache_clear()).
settings = get_settings()