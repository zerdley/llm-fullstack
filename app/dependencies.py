from typing import Callable
from fastapi import Request
from app.db.crud import log_generate_request
from app.model.base import Base
from app.schemas import Prompt

def get_model(request: Request) -> Base:
    return request.app.state.model

def get_generate_request_logger() -> Callable[[Prompt], None]:
    return log_generate_request