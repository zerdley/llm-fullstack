from typing import Annotated, AsyncIterable
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.dependencies import get_model
from app.model.base import Base
from app.schemas import Prompt

router = APIRouter(
    prefix="/generate",
)

@router.post("", response_class=StreamingResponse)
async def stream_generation(prompt: Prompt, model: Annotated[Base, Depends(get_model)]) -> AsyncIterable[str]:
    async for token in model.generate(prompt):
        yield token