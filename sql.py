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
        return  self.cursor.lastrowid

    def get_user(self):
        sql_query = "SELECT * FROM  {} WHERE userId={}"
        raw_query = sql_query.format(USER_TABLE, self.id)
        print(raw_query)
        self.cursor.execute(raw_query)

        return self.cursor.fetchone()

    def get_all_records(self):
        sql_query = "SELECT * FROM {}"
        raw_query = sql_query.format(USER_TABLE)
        self.cursor.execute(raw_query)
        all_data = []
        for record in self.cursor.fetchall():
            all_data.append({"id":record[0], "name":record[1]})
        return all_data



class TripTable(object):
    """
    Mapping trip table with python class
    """
    def __init__(self, id=None, name=None):
        self.trip_id, self.trip_name = id, name
        self.con = Connection()
        self.cursor = self.con.get_cursor()

    def insert(self):
        sql_query = "INSERT INTO {}({}) VALUES (%s)"
        raw_query = sql_query.format(TRIP_TABLE, 'tripName')
        self.cursor.execute(raw_query, (self.trip_name,))
        self.con.commit()
        return self.cursor.lastrowid

    def get_trip(self):
        sql_query = "SELECT * FROM {} WHERE tripId={}"
        raw_query = sql_query.format(TRIP_TABLE, self.trip_id)
        self.cursor.execute(raw_query)
        return self.cursor.fetchone()

    def get_all_records(self):
        sql_query = "SELECT * FROM {}"
        raw_query = sql_query.format(TRIP_TABLE)
        self.cursor.execute(raw_query)
        all_data = []
        for record in self.cursor.fetchall():
            all_data.append({"id": record[0], "name":record[1]})
        return all_data


class UserBalanceTable(object):
    """
    Mapping SQL table user balance with python class
    """
    def __init__(self, ub_id=None, user_id=None, trip_id=None, balance=None):
        self.ub_id = ub_id
        self.user_id = user_id
        self.trip_id = trip_id
        self.balance = balance
        self.con = Connection()
        self.cursor = self.con.get_cursor()

    def insert(self):
        if self.if_exists():
            self.update_user_balance(balance, user_id, trip_id)
        else:
            sql_query = "INSERT INTO {}({},{},{}) VALUES(%s, %s, %s)"
            raw_query = sql_query.format(USER_BAL_TABLE, 'balance','userId','tripId')
            self.cursor.execute(raw_query, (self.balance, self.user_id, self.trip_id,))
            self.con.commit()

    def if_exists(self, user_id, trip_id):
        sql_query = "SELECT * FROM {} WHERE userId={} AND tripId={}"
        raw_query = sql_query.format(USER_BAL_TABLE, user_id, trip_id)
        self.cursor.execute(raw_query)
        return True if self.cursor.fetchall() else False

    def update_user_balance(self, balance, user_id, trip_id):
        balance = self.get_user_balance(user_id, trip_id)[0] + balance
        print("Balance +++++++++++++++++++++++++++     {}".format(balance))
        sql_query = "UPDATE {} SET balance={} WHERE userId={} AND tripId={}"
        raw_query = sql_query.format(USER_BAL_TABLE, balance, user_id, trip_id)
        self.cursor.execute(raw_query)
        self.con.commit()

    def get_user_balance(self, user_id, trip_id):
        sql_query = "SELECT balance from {} WHERE userId={} AND tripId={}"
        raw_query = sql_query.format(USER_BAL_TABLE, user_id, trip_id)
        self.cursor.execute(raw_query)
        return self.cursor.fetchone()


    def get_all_trip_users(self, trip_id):
        trip_sql = "SELECT userId, balance from {} WHERE tripId={}"
        raw_trip_sql = trip_sql.format(USER_BAL_TABLE, trip_id)
        self.cursor.execute(raw_trip_sql)
        all_balance = []
        for bal in self.cursor.fetchall():
            user_obj = UserTable(user_id=bal[0])
            all_balance.append({"name": user_obj.get_user()[1], "balance": bal[1]})
        return all_balance


if __name__ == "__main__":
    pass
