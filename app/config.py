from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache
def settings():
    return Settings()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    model: str = "fake"
    db_url: str = ""
    fake_sleep_time: float = 0.05
