from fastapi import Request
from app.model.base import Base

def get_model(request: Request) -> Base:
    return request.app.state.model