from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user
app = Flask(__name__)

app.config.from_pyfile('config.py')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  'login_page'
from accounts import *
from views import *
if __name__ == '__main__':
	app.run()
