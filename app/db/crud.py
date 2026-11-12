from sqlmodel import Session

from app.db.db import get_engine
from app.db.tables import GenerateRequest
from app.schemas import Prompt


def log_generate_request(prompt: Prompt) -> None:
    with Session(get_engine()) as session:
        session.add(GenerateRequest(prompt=prompt.prompt, max_tokens=prompt.max_tokens))
        session.commit()