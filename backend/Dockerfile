FROM python:3.12.1 AS venv

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_IN_PROJECT="true" \
    POETRY_NO_INTERACTION=1 \
    PATH="$PATH:/root/.local/bin"

RUN pip install pipx
RUN pipx install "poetry==$POETRY_VERSION"
RUN pipx ensurepath

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root --no-interaction --no-ansi

FROM python:3.12.1
WORKDIR /usr/src/app

# For watching files and because no-root is better
RUN useradd -ms /bin/sh -u 1001 app
USER app

COPY --from=venv --chown=app:app /.venv /usr/src/.venv
COPY --chown=app:app backend /usr/src/backend
COPY --chown=app:app entrypoint.sh /entrypoint.sh
WORKDIR /usr/src/backend
ENV PATH="/usr/src/.venv/bin:$PATH"

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "/usr/src/backend/manage.py", "runserver", "0.0.0.0:8000" ]
