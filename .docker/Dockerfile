FROM python:3.11-slim
ENV WORKDIR=/app
WORKDIR $WORKDIR

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --without dev --no-interaction --no-ansi && \
    rm -rf ~/.cache


ENV WORKDIR=/app \
    PYTHONPATH=/app

WORKDIR $WORKDIR

# COPY --from=deps /venv /venv


ENV PATH=/venv/bin:$PATH

# COPY --from=build /venv/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages
COPY ../src $WORKDIR/src
