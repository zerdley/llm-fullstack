from functools import lru_cache
from sqlmodel import create_engine

from app.config import settings

@lru_cache
def get_engine():
    return create_engine(settings().db_url)