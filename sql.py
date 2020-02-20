import mysql.connector as con
from constants   import *


class Connection(object):
        """
        Connection to MySQL Database, and gives you access to the cursor object
        """
        def __init__(self):
            self.con = con.connect(host=HOST, database=DB_NAME, user=DB_USER, passwd=DB_PASS)

        def get_cursor(self):
            return self.con.cursor()

        def commit(self):
            self.con.commit()


class UserTable(object):
    """
    Maps user table on MyySQL db
    """
    def __init__(self, user_id=None, name=None,  email=None, ph_no=None):
        self.id = user_id
        self.name, self.email, self.ph_no = name, email, ph_no
        self.con =  Connection()
        self.cursor = self.con.get_cursor()


    def insert(self):
        sql_query="INSERT INTO {}({},{},{}) VALUES(%s, %s, %s)"
        raw_sql= sql_query.format(USER_TABLE, "Name","Email","Phone", self.name, self.email, self.ph_no)
        self.cursor.execute(raw_sql, (self.name, self.email, self.ph_no))
        self.con.commit()



if __name__ == "__main__":
    pass
