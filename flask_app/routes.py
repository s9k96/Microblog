from flask_app import app
from flask import render_template
from flask_app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username':'thomas the tank engine!!!'
    }

    return render_template('index.html', title='Home', user=user)


@app.route('/login')
def login():
    form=LoginForm()

    return render_template('login.html', title='sign in', form=form)

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')