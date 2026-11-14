from sqlmodel import Field, SQLModel


class GenerateRequest(SQLModel, table=True):
    __tablename__ = "generate_request"  # pyright: ignore[reportAssignmentType]
    id: int | None = Field(default=None, primary_key=True)
    prompt: str
    max_tokens: int
    time_to_first_token: float | None = None
    total_generation_time: float
    output_token_count: int
