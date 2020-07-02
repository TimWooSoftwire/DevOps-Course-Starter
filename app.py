from flask import Flask, render_template, request, redirect, url_for
from trello_helper import TrelloAPI as trello

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    todos = trello.get_items()
    return render_template('index.html', todos=todos)

@app.route('/new', methods=['POST'])
def new_todo():
    title = request.form.get('title')
    trello.add_item(title)
    return redirect('/')

@app.route('/complete/<id>', methods=['POST'])
def mark_as_complete(id):
    trello.complete_item(id)
    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    trello.delete_item(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
