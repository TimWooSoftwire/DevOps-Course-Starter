# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
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

## Secrets

Secrets (a trello API key and Token) are stored in a secrets.py file, and not checked in to git.  These look like 
```bash
TRELLO_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TRELLO_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Constants and environment variables
`constants.py` has some constants in - these all get set automatically. When running for the first time, you will need to create a new trello board, and set the environemnt variable "TRELLO_BOARD_ID" to the id of the new board. 
The environment variable "DONT_CHECK_FOR_TRELLO_LIST_IDS" is for testing, and should be set to false when running the app.

## Testing

Unit, integration and end-to-end tests using pytest are available - run then in your favourite IDE. 
End to end tests will require:
 * internet connectivity
