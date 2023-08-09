import sqlite3

class DBase:

    connection = None
    def __init__(self):
        print("database creation")
        self.connection = sqlite3.connect("./files/db/newsMailer.db")

    def __del__(self):
        print("connection closed")
        self.connection.close()

if __name__ == "__main__":
    db = DBase()
