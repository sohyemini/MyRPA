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

    def updateKeyword(self, idx, keyword, send):
        db = self.connection.cursor()
        db.execute("UPDATE keyword SET keyword = ?, send = ? WHERE idx = ?", (keyword, send, idx, ))
        self.connection.commit()
    def updateEmail(self, idx, kidx, name, email, memo):
        db = self.connection.cursor()
        db.execute("UPDATE email SET kidx = ?, "
                   "name = ?, email = ?, memo = ? "
                   "WHERE idx = ?"
                   , (kidx, name, email, memo, idx, ))
        self.connection.commit()
    def updateStime(self, stime):
        db = self.connection.cursor()
        db.execute("UPDATE stime SET stime = ? WHERE idx = 1", (stime,))
        self.connection.commit()
    def deleteKeyword(self, idx):
        db = self.connection.cursor()
        db.execute("DELETE FROM keyword WHERE idx = ?", (idx,))
        self.connection.commit()
    def deleteEmail(self, idx):
        db = self.connection.cursor()
        db.execute("DELETE FROM email WHERE idx = ?", (idx,))
        self.connection.commit()
    def deleteEmailAll(self, kidx):
        db = self.connection.cursor()
        db.execute("DELETE FROM email WHERE kidx = ?", (kidx,))
        self.connection.commit()

    def getAllData(self, tbl_name):
        db = self.connection.cursor()
        sql = f"SELECT * FROM {tbl_name}"
        conn = db.execute(sql)
        return conn.fetchall()

    def getSendingKeyword(self):
        db = self.connection.cursor()
        sql = f"SELECT * FROM keyword WHERE send = 1"
        conn = db.execute(sql)
        return conn.fetchall()

    # 이메일을 받을 사람만 추려기 위한 함수
    # kidx가 키워드 테이블의 idx이며, 이 정보가 email 테이블에 저장되어 있음
    def getEmailForSending(self,kidx):
        db = self.connection.cursor()
        sql = f"SELECT * FROM email WHERE kidx = {kidx}"
        conn = db.execute(sql)
        return conn.fetchall()

    def getOneData(self, tbl_name, idx):
        db = self.connection.cursor()
        sql = f"SELECT * FROM {tbl_name} WHERE idx = {idx}"
        conn = db.execute(sql)
        return conn.fetchall()

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

    db.updateKeyword(1, "internal bank interest ratio", 1)
    db.updateEmail(1, 1, "sohyemin", "sohyemini@gmail.com", "나")
    db.updateStime("18:24")

    # db.deleteKeyword(2)
    # db.deleteEmail(2)
    # db.deleteEmailAll(3)

    print("keyword data")
    rows = db.getAllData('keyword')
    for row in rows:
        print(row)

    print("keyword data for sending email")
    rows = db.getSendingKeyword()
    for i in range(len(rows)):
        idx, keyword, send = rows[i]
        print(idx, keyword, send)

    print("email receiver kidx == 1")
    rows = db.getEmailForSending(1)
    for row in rows:
        print(row)