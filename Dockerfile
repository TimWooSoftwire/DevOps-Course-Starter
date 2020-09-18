FROM python:3.9.0rc2-buster as base

RUN pip install poetry
RUN pip install gunicorn

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /app

EXPOSE 5000

FROM base as production
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]

FROM base as development
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
