from pydantic import BaseModel, Field


class Prompt(BaseModel):
    prompt: str
    max_tokens: int = Field(ge=1)
