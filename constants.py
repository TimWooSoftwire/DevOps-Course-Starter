import os

TRELLO_KEY = os.environ.get('TRELLO_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')

BASE_API_URL = "https://api.trello.com/1"
DEFAULT_PAYLOAD = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN}
BOARD_ID = ""
TODO_LIST_ID = "1"
DONE_LIST_ID = "2"
DOING_LIST_ID = "3"
