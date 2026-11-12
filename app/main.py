from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import settings
from app.model.fake import FakeModel
from .routers import generate, health

@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings().model == "fake":
        model = FakeModel()
    else:
        model = FakeModel() # Stand-in
    app.state.model = model
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(generate.router)
app.include_router(health.router)
