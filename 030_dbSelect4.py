import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

id = 1
cur.execute("SELECT a.id, c.name, a.cellNo, a.addr " \
   "FROM AddressBook as a, CustomerCode as c " \
   "WHERE a.id = ? and c.id = ?;", (id, id))

results = cur.fetchall()
for result in results:
    print(result)

cur.close()
con.close()
