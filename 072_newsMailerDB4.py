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

        if not self.is_table_exist('keyword'):
            print("keyword table create")
            sql = "CREATE TABLE keyword " \
                  "(idx INTEGER PRIMARY KEY AUTOINCREMENT, " \
                  "keyword TEXT, send INTEGER)"
            db.execute(sql)

        if not self.is_table_exist('email'):
            print("email table create")
            sql = "CREATE TABLE email (idx INTEGER PRIMARY KEY AUTOINCREMENT, " \
                  "kidx INTEGER, name TEXT, email TEXT, memo TEXT)"
            db.execute(sql)

        if not self.is_table_exist('stime'):
            print("stime table create")
            sql = "CREATE TABLE stime (idx INTEGER PRIMARY KEY AUTOINCREMENT, " \
                  "stime TEXT)"
            db.execute(sql)

    def is_table_exist(self, tbl_name):
        db = self.connection.cursor()
        cursor = db.execute("SELECT * FROM sqlite_master WHERE name = ?", (tbl_name,))

        if cursor.fetchone():
            print(f"{tbl_name} 테이블이 있어요")
            db.close()
            return True

        print(f"{tbl_name} 테이블이 없어요")
        db.close()
        return False

    def insertKeyword(self, keyword, send):
        db = self.connection.cursor()
        db.execute("INSERT INTO keyword (keyword, send) VALUES (?, ?)", (keyword, send,))
        self.connection.commit()

    def insertEmail(self, kidx, name, email, memo):
        db = self.connection.cursor()
        db.execute("INSERT INTO email "
                   "(kidx, name, email, memo) "
                   "VALUES (?, ?, ?, ?)"
                   , (kidx, name, email, memo,))
        self.connection.commit()

    def insertStime(self, stime):
        db = self.connection.cursor()
        db.execute("INSERT INTO stime (stime) VALUES (?)", (stime,))
        self.connection.commit()

if __name__ == "__main__":
    db = DBase()
    db.insertKeyword("internal bank interest", 1)
    db.insertKeyword("k-pop news", 0)
    db.insertKeyword("global EV sales", 1)

    db.insertEmail(1, "ricky", "ricky@gmail.com", "친구")
    db.insertEmail(1, "NICK", "nick@ktt.com", "동료")
    db.insertEmail(2, "ricky", "ricky@gmail.com", "친구")
    db.insertEmail(3, "ricky", "ricky@gmail.com", "친구")
    db.insertEmail(3, "BK", "bbk@hkmk.co.kr", "선배")
    db.insertEmail(3, "hun", "hun.kim@ltk.com", "팀장")

    db.insertStime("23:59")
