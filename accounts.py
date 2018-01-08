from app import app, login_manager
from flask import render_template, request, redirect, url_for
from dbconnection import connection
from models import User, Posting
from loginForm import SigninForm
from werkzeug.security import check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user
@app.route('/login', methods=["GET"])
def login_page():
    return render_template('login.html', form=SigninForm())

@app.route('/login', methods =["POST"])
def login_post():
    data = request.form
    form = SigninForm(data)
    if form.validate():
        user = User.get_user(form.username.data)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('listings_page'))
        else:
            return "Password Incorrect"
    else:
        return render_template('login.html', form=form)

