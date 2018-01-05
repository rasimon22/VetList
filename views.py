from app import app
from dbconnection import connection
from flask import render_template, request, redirect, url_for
from registerForm import SignupForm
from models import User
@app.route('/')
@app.route('/<name>')
def index(name = None):
    try: 
        cursor, db = connection()
        x = cursor.execute("Select employer.name, listings.description from listings, employer WHERE listings.employer_id = employer.employer_id;")
        result = cursor.fetchall()
        if result:
            return render_template('splash.html', name=name, listings=result)
        else:
            return "Error"
    except Exception as e: 
        return "Database Error"
@app.route('/register', methods =["GET"])
def register_page(): 
    return render_template('register.html', form=SignupForm(csrf_enabled=False))
@app.route('/register', methods=["POST"])
def register_post():
    data=request.form
    form =SignupForm(request.form, csrf_enabled=False)
    if form.validate():
        user = User(form.username.data, form.firstName.data, form.lastName.data,
                form.branch.data, form.password.data)
        user.create_user()
        return redirect(url_for('index'))
    else:
        return render_template('register.html', form=form) 
