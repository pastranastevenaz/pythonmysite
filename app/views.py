from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# from app import app
# from .forms import LoginForm
#
# @app.route('/')
# @app.route('/index')
# def index():
#
#     return render_template('index.html',
#                            title='Home',
#                            user=user,
#                            posts= posts,
#                            hobbies = hobbies)
#
#
#
# @app.route('/posts')
# def posts():
#     return "Hello from posts"
