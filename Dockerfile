FROM python:3.9.0rc2-buster

RUN pip install poetry
RUN pip install gunicorn

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /app

EXPOSE 5000
#ENTRYPOINT ["flask", "run"]

#ENTRYPOINT ["gunicorn", "-c", "./gunicorn.conf.py", "wsgi:app"]
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]

