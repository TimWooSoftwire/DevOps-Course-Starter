# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

There is also a Vagrant option. With vagrant installed, and Windows Hyper-V disabled, run `vagrant up` from the root of this directory. It should do all of the above for you, and after a few minutes the app will be running on `http://localhost:5000/`.

There is also a docker option. With Docker Desktop running, use the following commands from the root of this directory to start the app running on port 5000 using gunicorn:
```bash
docker build --target production --tag todo-app:prod . 
docker run --env-file .env -p 5000:5000 todo-app:prod
```
Or these commands to start a development version using flask's development mode:
```bash
docker build --target production --tag todo-app:dev . 
docker run --env-file .env -p 5000:5000 -v ${pwd}:/app todo-app:dev
```
Note the volume mount (-v) flag - this means that changes to local files will be present on the container; no rebuild/rerun required. You'll need to add this root directory to the set of directories that docker is allowed to bind - see [this answer](https://stackoverflow.com/a/59984239) for details on how to do this.


## Secrets

Secrets (a trello API key and Token) are stored in .env files, and not checked into git. the .env files look like 
```{bash}
TRELLO_KEY=""
TRELLO_TOKEN=""
```

## Constants and environment variables
`constants.py` has some constants in - these all get set automatically. When running for the first time, you will need to create a new trello board, and set the environemnt variable "TRELLO_BOARD_ID" to the id of the new board. 

## Testing

Unit and integration and end-to-end tests using pytest are available - run then in your favourite IDE. 
For the end to end tests, a different webdriver is needed for running locally vs in Docker - use the correct one in test_e2e.py.


You can run all tests, including end to end tests, using Docker with 
```bash
docker build --target test --tag my-test-image .
docker run --env-file .env.e2e my-test-image tests
```

### Testing environment variables
The end to end tests want real trello credentials in a `.env.e2e` file - copy the trello credentials from your main `.env` file. The e2e tests will create their own board.
Note the comment about webdrivers above too!

## CI
`travis.yml` describes the automated code build that happens whenever a PR is raised. The two `secure` variable are encrypted forms of the trello API key and token. Note that the environment variables are explicitly passed through to Docker with the `-e` flag in the `docker run` command

## CD 
The travis file above will also automatically deploy the app to https://tims-todo-app.herokuapp.com/ when anything is pushed to master; this uses heroku.