FROM python:3.8.5-buster as base

FROM base as production

RUN pip install poetry
RUN pip install gunicorn

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false


COPY . /app

EXPOSE 5000

ENV FLASK_ENV=production
RUN poetry install --no-dev
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]

FROM base as development

RUN pip install poetry
RUN pip install gunicorn

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false


COPY . /app

EXPOSE 5000

RUN poetry install
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]


FROM base as test

RUN pip install "poetry==1.0.10"
COPY . ./app
WORKDIR /app
RUN poetry install

# Install Chrome 
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb
RUN rm /var/lib/apt/lists/* -vf
RUN apt-get clean
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install ./chrome.deb -y
RUN rm ./chrome.deb

# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
 echo "Installing chromium webdriver version ${LATEST}" &&\
 curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
 apt-get install unzip -y &&\
 unzip ./chromedriver_linux64.zip
 
ENTRYPOINT [ "poetry", "run", "pytest" ]