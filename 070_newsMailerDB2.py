import sqlite3

class DBase:

    connection = None
    def __init__(self):
        print("database creation")
        self.connection = sqlite3.connect("./files/db/newsMailer.db")
        self.create_tables()

    def __del__(self):
        print("connection closed")
        self.connection.close()

    def create_tables(self):
        db = self.connection.cursor()
        print("keyword table create")
        sql = "CREATE TABLE keyword " \
              "(idx INTEGER PRIMARY KEY AUTOINCREMENT, " \
              "keyword TEXT, send INTEGER)"
        db.execute(sql)

        print("email table create")
        sql = "CREATE TABLE email (idx INTEGER PRIMARY KEY AUTOINCREMENT, " \
              "kidx INTEGER, name TEXT, email TEXT, memo TEXT)"
        db.execute(sql)

        print("stime table create")
        sql = "CREATE TABLE stime (idx INTEGER PRIMARY KEY AUTOINCREMENT, " \
              "stime TEXT)"
        db.execute(sql)

if __name__ == "__main__":
    db = DBase()
