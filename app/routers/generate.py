import time
from collections.abc import AsyncIterable, Callable
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import StreamingResponse

from app.dependencies import get_generate_request_logger, get_model
from app.model.base import Base
from app.schemas import Prompt

router = APIRouter(
    prefix="/generate",
)


@router.post("", response_class=StreamingResponse)
async def stream_generation(
    prompt: Prompt,
    model: Annotated[Base, Depends(get_model)],
    background_tasks: BackgroundTasks,
    generate_request_logger: Annotated[
        Callable[[Prompt, float | None, float, int], None],
        Depends(get_generate_request_logger),
    ],
) -> AsyncIterable[str]:
    time_start = time.perf_counter()
    token_count = 0
    ttft_end = None
    try:
        async for token in model.generate(prompt):
            if ttft_end is None:
                ttft_end = time.perf_counter()
            token_count += 1
            yield token
    finally:
        total_time_end = time.perf_counter()
        ttft = ttft_end - time_start if ttft_end is not None else None
        background_tasks.add_task(
            generate_request_logger,
            prompt,
            ttft,
            (total_time_end - time_start),
            token_count,
        )
