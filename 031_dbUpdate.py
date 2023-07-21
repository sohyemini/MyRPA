import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

id = 1
name = '김삼순'
cur.execute("UPDATE CustomerCode SET name = ? WHERE id = ?;", (name, id))
con.commit()

cur.execute("SELECT * FROM CustomerCode WHERE id = ?;", (id, ))
results = cur.fetchall()
for result in results:
    print(result)

cur.close()
con.close()
