from flask_app import app
from flask import render_template, request
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

@app.route('/proj_quora',  methods=['GET', 'POST'])
def proj_quora():
    text = 'yooooo'
    return render_template('proj_quora.html', title='Quora Similarity', results=text)

@app.route('/proj_stackoverflow', methods=['GET', 'POST'])
def proj_stackoverflow():
    if request.method=='POST':
        text = request.values.get('text')
        if text:
            return render_template('proj_stackoverflow.html', title = 'Tag Prediction', results= text)
    else:
        return render_template('proj_stackoverflow.html', title = 'Tag Prediction')