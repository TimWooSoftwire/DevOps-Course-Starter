import os
import pytest
import requests
import app
import constants as c
from threading import Thread

from selenium import webdriver

# Below driver is for running locally

# @pytest.fixture(scope="module")
# def driver():
#     with webdriver.Firefox() as driver:
#         yield driver

# For running in Docker
@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
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

    # Create a new todo
    test_todo_item_name = "My new Todo"
    new_todo_input_box = driver.find_element_by_id('title')
    new_todo_input_box.send_keys(test_todo_item_name)
    new_todo_submit_button = driver.find_element_by_css_selector("input.btn-primary")
    new_todo_submit_button.click()

    assert "My new Todo" in driver.page_source
    assert "Start" in driver.page_source

    # Move to doing
    move_to_doing_button = driver.find_element_by_css_selector("input.btn-warning")
    move_to_doing_button.click()

    assert "My new Todo" in driver.page_source
    assert "Done!" in driver.page_source

    # Move to done
    move_to_done_button = driver.find_element_by_css_selector("input.btn-success")
    move_to_done_button.click()

    assert "My new Todo" in driver.page_source
    assert "Delete" in driver.page_source

    # Delete
    delete_todo_button = driver.find_element_by_css_selector("input.btn-danger")
    delete_todo_button.click()

    assert "My new Todo" not in driver.page_source
