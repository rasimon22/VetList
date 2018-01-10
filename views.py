from app import app  
from dbconnection import connection
from flask import render_template, request, redirect, url_for, session
from registerForm import SignupForm
from models import User, Posting
from werkzeug.security import generate_password_hash


@app.route('/index')
def index():
    try:
        cursor, db = connection()
        cursor.execute("Select employer.name, listings.description from listings, employer "
                       "WHERE listings.employer_id = employer.employer_id;")
        result = cursor.fetchall()
        if result:
            return render_template('splash.html', listings=result)
        else:
            return "Error"
    except Exception as e: 
        return str(e)


@app.route('/register/', methods=["GET"])
def register_page(): 
    return render_template('register.html', form=SignupForm())


@app.route('/register/', methods=["POST"])
def register_post():
    data = request.form
    form = SignupForm(data)
    if form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(form.username.data, form.firstName.data, form.lastName.data,
                    form.branch.data, hashed_password)
        user.create_user()
        return redirect(url_for('index'))
    else:
        return render_template('register.html', form=form)


@app.route('/listing/', methods=['GET'])
def listings_page():
    posts = Posting.get_posts()
    return render_template('listings.html', posts=posts)


@app.route('/listing/<int:lid>')
def listing_detail(lid):
    if 'uid' in session:
        post = Posting.get_post(lid)
        return render_template("detail.html", post=post)
    else:
        return redirect(url_for('login_page'))


# this route must remain last
@app.route('/')
def root():
    return redirect(url_for('index'))
