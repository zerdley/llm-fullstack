from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str
    max_tokens: int