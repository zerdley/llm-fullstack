FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim AS base

WORKDIR /app

RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

ENV PYTHONUNBUFFERED=1

ENV UV_NO_DEV=1

ENV UV_COMPILE_BYTECODE=1

ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []


FROM base AS dev

ENV UV_NO_DEV=0

COPY --chown=nonroot . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

USER nonroot

CMD ["fastapi", "dev", "--host", "0.0.0.0"]


FROM base AS prod

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

USER nonroot

CMD ["fastapi", "run"]
