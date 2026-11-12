from typing import Annotated, AsyncIterable, Callable
from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import StreamingResponse

from app.dependencies import get_generate_request_logger, get_model
from app.model.base import Base
from app.schemas import Prompt

router = APIRouter(
    prefix="/generate",
)

@router.post("", response_class=StreamingResponse)
async def stream_generation(prompt: Prompt, model: Annotated[Base, Depends(get_model)], background_tasks: BackgroundTasks, generate_request_logger: Annotated[Callable[[Prompt], None], Depends(get_generate_request_logger)]) -> AsyncIterable[str]:
    background_tasks.add_task(generate_request_logger, prompt)
    async for token in model.generate(prompt):
        yield token