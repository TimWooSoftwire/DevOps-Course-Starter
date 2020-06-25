from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import trello_helper as trello

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['GET'])
def index():
    todos = trello.get_items()
    return render_template('index.html', todos=todos)


@app.route('/new', methods=['POST'])
def newtodo():
    title = request.form.get('title')
    trello.add_item(title)
    return redirect('/')

@app.route('/complete/<id>', methods=['POST'])
def markascomplete(id):
    trello.complete_item(id)
    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    # todo = trello.get_item(id)
    trello.delete_item(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
