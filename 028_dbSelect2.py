import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

cur.execute("SELECT addr, id FROM AddressBook WHERE id = 3;")
results = cur.fetchall()
for result in results:
    print(result[0], result[1])
    # print(result)

cur.close()
con.close()
