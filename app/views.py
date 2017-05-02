from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/connectiontest')
def connectiontest():
    return render_template('connectiontest.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/blog0412201701')
def blog0412201701():
    return render_template('blog0412201701.html')

@app.route('/blog/blog0502201701')
def blog0502201701():
    return render_template('blog0502201701.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
