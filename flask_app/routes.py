from flask_app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username':'thomas the tank engine!!!'
    }

    return render_template('index.html', title='Home', user=user)