import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

cur.execute("INSERT INTO CustomerCode VALUES (1, '홍길동');")
cur.execute("INSERT INTO CustomerCode VALUES (?, ?);", (2, '김갑동'))
id = 3
name = '김순이'
cur.execute(f"INSERT INTO CustomerCode VALUES ({id}, '{name}');")
id2 = 4
name2 = '삼순이'
cur.execute("INSERT INTO CustomerCode VALUES (?, ?);", (id, name))

con.commit()

cur.close()
con.close()
