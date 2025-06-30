ARG AIRFLOW_VERSION=3.0.2
ARG PYTHON_VERSION=3.12

FROM docker.io/apache/airflow:slim-${AIRFLOW_VERSION}-python${PYTHON_VERSION}

ENV AIRFLOW_USE_UV=true

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --active
