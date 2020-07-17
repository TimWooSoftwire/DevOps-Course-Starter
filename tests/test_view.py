import sys
import pytest
from datetime import datetime, timedelta

del sys.path[0]
sys.path.insert(0, 'C:/Users/TimWoo/Work/Training/DevOpsApprenticeship/ProjectExercise/DevOps-Course-Starter')
from view_model import ViewModel
from TodoItem import TodoItem
import constants

@pytest.fixture
def example_board():
    todo_item = TodoItem(1, constants.TODO_LIST_ID, "Item not started", datetime.now())
    doing_item = TodoItem(2, constants.DOING_LIST_ID, "Item in progress", datetime.now())
    done_item = TodoItem(3, constants.DONE_LIST_ID, "Completed Item!", datetime.now())
    return ViewModel([todo_item, doing_item, done_item])

@pytest.fixture
def example_board_with_different_dates():
    old_item = TodoItem(3, constants.DONE_LIST_ID, "I did this ages ago", datetime.now() - timedelta(days=1))
    fresh_item = TodoItem(3, constants.DONE_LIST_ID, "I just finished this", datetime.now())
    return ViewModel([old_item, fresh_item])

def test_items_in_done(example_board):
    assert "Completed Item!" == example_board.items_in_done[0].name

def test_items_in_doing(example_board):
    assert "Item in progress" ==  example_board.items_in_doing[0].name

def test_items_in_todo(example_board):
    assert "Item not started" ==  example_board.items_in_todo[0].name

def test_show_all_done_items_true_if_fewer_than_5_items(example_board):
    assert example_board.show_all_done_items == True

def test_show_all_done_items_false_if_more_than_5_items():
    item = TodoItem(3, constants.DONE_LIST_ID, "Completed Item!", datetime.now())
    model = ViewModel([item] * 6)
    assert model.show_all_done_items == False

def test_recently_done_items(example_board_with_different_dates):
    assert "I just finished this" == example_board_with_different_dates.recent_done_items[0].name

def test_older_done_items(example_board_with_different_dates):
    assert "I did this ages ago" == example_board_with_different_dates.older_done_items[0].name



