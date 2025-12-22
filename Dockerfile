# STAGE 1: Build the application
FROM debian:bookworm-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# https://github.com/astral-sh/uv-docker-example/blob/main/standalone.Dockerfile
# compile bytecode: pre-compile .py to .pyc for faster startup (no runtime compilation)
# no default groups: don't install groups marked as default in [tool.uv] (you'll specify explicitly with --group)
# frozen: sync without updating uv.lock (fail if lock is out of date, ensures reproducible builds)
# link mode: copy files instead of hardlinks (safer for containers, avoids issues with layered filesystems)
# install dir: where uv installs its managed python (keeps it in a predictable location for COPY --from)
# python preference: only use uv-managed python, never system python (ensures consistency)
ENV UV_COMPILE_BYTECODE=true
ENV UV_NO_DEFAULT_GROUPS=true
ENV UV_FROZEN=true
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_INSTALL_DIR=/python
ENV UV_PYTHON_PREFERENCE=only-managed

# immediately flush python output (for logging)
ENV PYTHONUNBUFFERED=1

# Copy python version and install
COPY .python-version .
RUN uv python install

# Copy project files needed by all builds
WORKDIR /app
COPY pyproject.toml uv.lock README.md ./

# sync dependency group 
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project