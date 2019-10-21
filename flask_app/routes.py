from flask import render_template, request
from flask_app.forms import LoginForm
from flask_app import app
import pickle
static = '/home/shubham/projs/shubham/microblog/flask_app/static/'

stack_vec = pickle.load(open(static+'pickles/stack/vectorizer.pkl', 'rb'))
stack_model = pickle.load(open(static+'pickles/stack/model.pkl', 'rb'))

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
	if request.method=='POST':
		text = request.values.get('text')
	if text:
			return render_template('proj_quora.html', title='Quora Similarity', results=text)
	else:
		return render_template('proj_quora.html', title='Quora Similarity')

@app.route('/proj_stackoverflow', methods=['GET', 'POST'])
def proj_stackoverflow():
		if request.method=='POST':
			text = request.values.get('text')
		if text:
			vector = stack_vec.transform([text])
			result = stack_model.predict(vector)
			prob = stack_model.predict_proba(vector)
			return render_template('proj_stackoverflow.html', title = 'Tag Prediction', results= result, probability=prob*100)
		else:
			return render_template('proj_stackoverflow.html', title = 'Tag Prediction')
