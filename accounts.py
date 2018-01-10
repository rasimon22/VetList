from app import app
from flask import render_template, request, redirect, url_for, session
from models import User
from loginForm import SigninForm
from werkzeug.security import check_password_hash


@app.route('/login', methods=["GET"])
def login_page():
    return render_template('login.html', form=SigninForm())


@app.route('/login', methods=["POST"])
def login_post():
    if 'uid' in session:
        return redirect(url_for('index'))
    data = request.form
    form = SigninForm(data)
    if form.validate():
        user = User.get_user(form.username.data)
        if user:
            if check_password_hash(user.password, form.password.data):
                session['uid'] = user.uID
                session['username'] = user.username
                session['f_name'] = user.f_name
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login_page', form=form))
        else:
            return redirect(url_for('login_page', form=form))
    else:
        return render_template('login.html', form=form)


@app.route('/logout', methods=["GET"])
def logout():
    if 'uid' not in session:
        return redirect('index')
    session.clear()
    return redirect(url_for('index'))
