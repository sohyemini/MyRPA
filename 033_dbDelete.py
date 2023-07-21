import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

name = '삼순이'
cur.execute("DELETE FROM CustomerCode WHERE name = ?;", (name, ))
con.commit()

cur.execute("SELECT count(*) FROM CustomerCode WHERE name = ?;", (name, ))
results = cur.fetchall()
for result in results:
    print(result)

cur.close()
con.close()
