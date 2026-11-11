from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import get_settings
from app.model.fake import FakeModel
from .routers import generate, health

@asynccontextmanager
async def lifespan(app: FastAPI):
    if get_settings().model == "fake":
        model = FakeModel()
    else:
        model = FakeModel()
    app.state.model = model
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(generate.router)
app.include_router(health.router)
