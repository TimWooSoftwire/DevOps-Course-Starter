import sys
import pytest
del sys.path[0]
sys.path.insert(0, 'C:/Users/TimWoo/Work/Training/DevOpsApprenticeship/ProjectExercise/DevOps-Course-Starter')
from view_model import ViewModel
from TodoItem import TodoItem
import constants

@pytest.fixture
def example_board():
    todo_item = TodoItem(1, constants.TODO_LIST_ID, "Item not started")
    doing_item = TodoItem(2, constants.DOING_LIST_ID, "Item in progress")
    done_item = TodoItem(3, constants.DONE_LIST_ID, "Completed Item!")
    return ViewModel([todo_item, doing_item, done_item])

def test_items_in_done(example_board):
    assert "Completed Item!" == example_board.items_in_done[0].name
    

def test_items_in_doing(example_board):
    assert "Item in progress" ==  example_board.items_in_doing[0].name

def test_items_in_todo(example_board):
    assert "Item not started" ==  example_board.items_in_todo[0].name

