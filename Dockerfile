FROM ghcr.io/astral-sh/uv:debian
WORKDIR /app
COPY . /app/
RUN uv sync --frozen
CMD ["uv", "run", "run.py"]
