import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

newName = '삼순이'
name = '김삼순'
cur.execute("UPDATE CustomerCode SET name = ? WHERE name = ?;", (newName, name))
con.commit()

id = 1
cur.execute("SELECT * FROM CustomerCode WHERE id = ?;", (id, ))
results = cur.fetchall()
for result in results:
    print(result)

cur.close()
con.close()
