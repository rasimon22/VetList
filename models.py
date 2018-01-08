from dbconnection import connection
import hashlib
from flask_login import UserMixin
class User(UserMixin):
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
    @classmethod
    def get_user(cls_obj, username):
        try:
            cursor, db = connection()
            y = cursor.execute("SELECT * from `vetlist`.`users` WHERE `users`.`username` = '{}';".format(username))
            result = cursor.fetchone()
            db.close()
            return cls_obj(result[1],result[2],result[3],result[4],result[6],result[0], result[5]) 
        except Exception as e:
            db.close()
            return "db error"
class Posting:
    def __init__ (self, l_id, e_id, zip_code, openings, description, company_name):
        self.l_id = l_id
        self.e_id = e_id
        self.zip_code = zip_code
        self.openings = openings
        self.description = description
        self.company_name = company_name
    def create_post(self):
        try:
            cursor, db = connection()
            y = cursor.execute("INSERT INTO `vetlist`.`users`(`employer_id`, `zip_code`, `openings``description`) VALUES ('{}','{}','{}','{}');".format(self.e_id,self.zip_code,self.openings,
                    self.description))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            db.close()
            return str(e)
    @classmethod
    def get_posts(cls_obj):
        try:
            cursor,db = connection()
            x=cursor.execute("SELECT * FROM listings, employer WHERE listings.employer_id = employer.employer_id;")
            results = cursor.fetchall()
            db.close
            postings = [] 
            for result in results:
                obj = cls_obj(result[0],result[1],result[2],result[3],result[4],result[6])
                postings.append(obj)
            return postings
        except Exception as e:
            db.close()
            return str(e)
    @classmethod
    def get_post(cls_obj, lid):
        try:
            cursor,db = connection()
            x=cursor.execute("SELECT * FROM listings,employer WHERE listings.listing_id = {} AND listings.employer_id = employer.employer_id;".format(lid))
            result = cursor.fetchone()
            print (result)
            db.close
            obj = cls_obj(result[0],result[1],result[2],result[3],result[4],result[6])
            return obj
        except Exception as e:
            db.close()
            return str(e)





