from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

@lru_cache(maxsize=128)
def get_settings():
    return Settings()

class Settings(BaseSettings):
    model: str = "fake"
    model_config = SettingsConfigDict(env_file=".env")