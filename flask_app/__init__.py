from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__,
            static_url_path='',
            static_folder='static/')


from flask_app import routes

app.config['SECRET_KEY']='averynicekey'
app.jinja_env.auto_reload=True
app.config['TEMPLATES_AUTO_RELOAD']=True
app.run(debug=True)
bootstrap = Bootstrap(app)


if __name__ == '__main__':
    app.run()
