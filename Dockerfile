FROM python:3.13.7-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.9.4 /uv /uvx /bin/

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --compile-bytecode

COPY /src .

CMD ["uv", "run", "main.py"]
