from app import app
from dbconnection import connection
from flask import render_template
@app.route('/')
@app.route('/<name>')
def index(name = None):
    return render_template('splash.html', name=name)
@app.route('/register', methods =["GET", "POST"])
def register_page():
    try:
        cursor, db  = connection()
        x = cursor.execute("SELECT *  FROM users")
        #result = cursor.fetchone()
        #result = cursor.fetchone()
        result = cursor.fetchall()
        if result:
            string  = ''
            for z in result:
                string  += '<p>'+str(z[1]) + str(z[4]) + ' ' +'</p>'
        return string
        if result:
            resultSet = []
            for y in result:
                resultSet+= y
        return resultSet 
    except Exception as e:
        return (str(e))

