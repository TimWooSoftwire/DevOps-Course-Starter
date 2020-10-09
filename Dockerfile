FROM python:3.8.5-buster as base

RUN pip install poetry
RUN pip install gunicorn

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false


COPY . /app

EXPOSE 5000

FROM base as production
ENV FLASK_ENV=production
RUN poetry install --no-dev
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]

FROM base as development
RUN poetry install
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
