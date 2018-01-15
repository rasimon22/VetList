from dbconnection import connection


class User:
    def __init__(self, username, f_name, l_name, branch,
                 password, uid=None, discharge_status=None):
        self.uID = uid
        self.username = username
        self.f_name = f_name
        self.l_name = l_name
        self.branch = branch
        self.discharge_status = discharge_status
        self.password = password

    def create_user(self):
        try:
            cursor, db = connection()
            cursor.execute("INSERT INTO `vetlist`.`users` (`username`, `first_name`, "
                           "`last_name`, `branch`, `password`) "
                           "VALUES ('{}', '{}', '{}', '{}', '{}');".format(self.username,
                                                                           self.f_name,
                                                                           self.l_name,
                                                                           self.branch,
                                                                           self.password))
            db.commit()
            db.close()
        except Exception as e:
            print(str(e))

    @classmethod
    def get_user(cls, username):
        try:
            cursor, db = connection()
            cursor.execute("SELECT * from `vetlist`.`users` WHERE "
                           "`users`.`username` = '{}';".format(username))
            result = cursor.fetchone()
            db.close()
            return cls(result[1], result[2], result[3], result[4], result[6],
                       result[0], result[5])
        except Exception as e:
            print(str(e))

    @classmethod
    def user_exists(cls, username):
        try:
            cursor, db = connection()
            cursor.execute("SELECT * FROM `vetlist`.`users` WHERE "
                           "`users`.`username` = '{}'".format(username))
            result = cursor.fetchone()
            db.close()
            return len(result) > 0
        except Exception as e:
            print(str(e))


class Posting:
    def __init__(self, l_id, e_id, zip_code, openings, description, company_name):
        self.l_id = l_id
        self.e_id = e_id
        self.zip_code = zip_code
        self.openings = openings
        self.description = description
        self.company_name = company_name

    def create_post(self):
        try:
            cursor, db = connection()
            cursor.execute("INSERT INTO `vetlist`.`users`"
                           "(`employer_id`, `zip_code`, `openings``description`)"
                           " VALUES ('{}','{}','{}','{}');".format(self.e_id,
                                                                   self.zip_code,
                                                                   self.openings,
                                                                   self.description))
            db.commit()
            db.close()
        except Exception as e:
            return str(e)

    @classmethod
    def get_posts(cls):
        try:
            cursor, db = connection()
            cursor.execute("SELECT * FROM listings, employer "
                           "WHERE listings.employer_id = employer.employer_id;")
            results = cursor.fetchall()
            db.close()
            postings = []
            for result in results:
                obj = cls(result[0], result[1], result[2], result[3], result[4], result[6])
                postings.append(obj)
            return postings
        except Exception as e:
            return str(e)

    @classmethod
    def get_post(cls, lid):
        try:
            cursor, db = connection()
            cursor.execute("SELECT * FROM listings,employer "
                           "WHERE listings.listing_id = {} "
                           "AND listings.employer_id = employer.employer_id;".format(lid))
            result = cursor.fetchone()
            print(result)
            db.close()
            obj = cls(result[0], result[1], result[2], result[3], result[4], result[6])
            return obj
        except Exception as e:
            return str(e)


class Skill:
    def __init__(self, skill, pro, uid):
        self.skill = skill
        self.pro = pro
        self.uid = uid

    @classmethod
    def get_skills_for_user(cls, user):
        try:
            cursor, db = connection()
            cursor.execute("SELECT * FROM skills WHERE user_id = {}".format(user))
            result = cursor.fetchall()
            db.close()
            resultSet = []
            for line in result:
                resultSet.append(cls(line[2], line[3]))
            return resultSet
        except Exception as e:
            return str(e)

    def create_skill(self):
        try:
            cursor, db = connection()
            cursor.execute("INSERT INTO `vetlist`.`skills` (`user_id`, `skill`, `proficiency`) VALUES "
                           "({}, {}, {})".format(self.uid, self.skill, self.pro))
        except Exception as e:
            return str(e)

