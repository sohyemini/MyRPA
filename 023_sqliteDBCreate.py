import sqlite3

con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()
cur.execute("CREATE TABLE CustomerCode(id integer unique, name text);")
cur.execute("CREATE TABLE AddressBook(id integer, cellNo text, addr text);")
cur.close()
con.close()
