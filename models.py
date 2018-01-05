from dbconnection import connection
import hashlib
class User:
    def __init__(self, username, f_name, l_name, branch,  password, uID = None, uso_status=None):
        m = hashlib.md5()
        self.uID=uID
        self.username = username
        self.f_name = f_name
        self.l_name = l_name
        self.branch = branch
        self.uso_status = uso_status
        self.password = password
    def create_user(self):
        try: 
            cursor, db = connection()
            y = cursor.execute("INSERT INTO `vetlist`.`users` (`username`, `first_name`, `last_name`, `branch`, `password`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(self.username,
                self.f_name, self.l_name, self.branch, self.password))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            db.close()
            return str(e)
