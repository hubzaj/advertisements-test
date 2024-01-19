FROM python:3.11.3-slim

RUN pip install -U poetry

WORKDIR /home/app

COPY poetry.lock pyproject.toml /home/app/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /home/app

ENTRYPOINT ["poetry", "run"]
