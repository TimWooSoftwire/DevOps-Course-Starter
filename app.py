import os

from flask import Flask, render_template, request, redirect

import constants
from trello_helper import TrelloAPI as trello
from view_model import ViewModel


def create_app():
    app = Flask(__name__)

    constants.BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    dont_check_for_list_ids = os.environ.get('DONT_CHECK_FOR_TRELLO_LIST_IDS')

    if not dont_check_for_list_ids:
        list_ids = trello.get_list_ids(constants.BOARD_ID)
        constants.TODO_LIST_ID = list_ids[0]
        constants.DOING_LIST_ID = list_ids[1]
        constants.DONE_LIST_ID = list_ids[2]

    @app.route('/', methods=['GET'])
    def index():
        todos = trello.get_items()
        item_view_model = ViewModel(todos)
        return render_template('index.html', view_model = item_view_model)

    @app.route('/new', methods=['POST'])
    def new_todo():
        title = request.form.get('title')
        trello.add_item(title)
        return redirect('/')

    @app.route('/done/<id>', methods=['POST'])
    def mark_as_complete(id):
        trello.move_item_to_done(id)
        return redirect('/')

    @app.route('/doing/<id>', methods=['POST'])
    def mark_as_doing(id):
        trello.move_item_to_doing(id)
        return redirect('/')

    @app.route('/delete/<id>', methods=['POST'])
    def delete(id):
        trello.delete_item(id)
        return redirect('/')

    return app


if __name__ == '__main__':
    create_app().run()
