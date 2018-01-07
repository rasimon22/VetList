from app import app
from flask import render_template, request, redirect, url_for
from dbconnection import connection
from models import User, Posting
@app.route('/dynamic')
def dynamic_route():
    return "Hello World"
