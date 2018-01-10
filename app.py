from flask import Flask
app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['TEMPLATE_AUTO_RELOAD'] = True
from accounts import *
from views import *
if __name__ == '__main__':
    app.run()
