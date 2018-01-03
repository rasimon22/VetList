from app import app
from dbconnection import connection
@app.route('/')
def index():
    return '<h1>This is the index</h1>'
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

