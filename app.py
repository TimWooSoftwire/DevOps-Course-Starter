from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['GET'])
def index():
    todos = session.get_items()
    return render_template('index.html', todos=todos)


@app.route('/new', methods=['POST'])
def newtodo():
    title = request.form.get('title')
    session.add_item(title)
    return redirect('/')

if __name__ == '__main__':
    app.run()
