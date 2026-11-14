from sqlmodel import Session

from app.db.db import get_engine
from app.db.tables import GenerateRequest
from app.schemas import Prompt


def log_generate_request(
    prompt: Prompt, ttft: float | None, total_gen_time: float, output_token_count: int
) -> None:
    with Session(get_engine()) as session:
        session.add(
            GenerateRequest(
                prompt=prompt.prompt,
                max_tokens=prompt.max_tokens,
                time_to_first_token=ttft,
                total_generation_time=total_gen_time,
                output_token_count=output_token_count,
            )
        )
        session.commit()
