import MySQLdb

def connection():
    try:
        db = MySQLdb.connect(host='localhost',
                user='root',
                passwd='abc123',
                db='vetlist')
        cursor = db.cursor()
        return cursor, db

    except Exception as e:
        print(str(e))
