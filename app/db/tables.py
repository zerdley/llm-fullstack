from sqlmodel import SQLModel, Field

class GenerateRequest(SQLModel, table=True):
    __tablename__ = "generate_request" # pyright: ignore[reportAssignmentType]
    id: int | None = Field(default=None, primary_key=True)
    prompt: str
    max_tokens: int
    latency: float | None = None