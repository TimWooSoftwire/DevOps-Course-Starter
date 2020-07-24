import os
import pytest
import requests
import app
import constants as c
from threading import Thread

from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox(r"C:\Users\TimWoo\Work\Training\DevOpsApprenticeship\ProjectExercise\DevOps-Course-Starter") as driver:
        yield driver


def create_trello_board(name):
    request_payload = {**c.DEFAULT_PAYLOAD, **{'name': name}}
    r = requests.post(f"{c.BASE_API_URL}/boards", params=request_payload)
    return r.json()['id']


def delete_trello_board(id):
    request_payload = c.DEFAULT_PAYLOAD
    requests.delete(f"{c.BASE_API_URL}/boards/{id}", params=request_payload)
    return "the board is dead"


@pytest.fixture(scope='module')
def test_app():
    board_id = create_trello_board("test_board")
    os.environ['TRELLO_BOARD_ID'] = board_id

    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)




def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'

