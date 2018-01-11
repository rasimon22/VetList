import os
from app import app
from flask import render_template, request, redirect, url_for, session
from models import User
from loginForm import SigninForm
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from util import allowed_file


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
                session['l_name'] = user.l_name
                session['branch'] = user.branch
                session['discharge_status'] = user.discharge_status
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


@app.route('/account/', methods=["GET"])
def account_page():
    if 'uid' in session:
        return render_template('account.html',
                               uploaded=os.path.exists(os.path.join(app.config['RESUME_FOLDER'], session['username'] +
                                                                    ".pdf")))
    else:
        return redirect(url_for('login_page'))


@app.route('/upload/', methods=["POST"])
def post_resume():
    if 'file' not in request.files:
        return redirect(url_for('account_page'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('account_page'))
    if file and allowed_file(file.filename):
        # if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], session['username'])):
        #     os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], session['username']))
        file.save(os.path.join(app.config['RESUME_FOLDER'], session['username'] + "." +
                               file.filename.rsplit('.', 1)[1].lower()))
        return redirect(url_for('account_page', uploaded=True))
    else:
        return redirect(url_for('account_page', uploaded=False))


@app.route('/password/', methods=["GET", "POST"])
def change_password():
    return "CP"
