from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='averynicekey'
from flask_app import routes



app.jinja_env.auto_reload=True
app.config['TEMPLATES_AUTO_RELOAD']=True

app.run(debug=True)
