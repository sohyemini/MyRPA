import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

cur.execute("SELECT * FROM AddressBook;")
results = cur.fetchall()
for result in results:
    print(result[0], result[1], result[2])
    # print(result)
print(type(results))
# con.commit()
cur.close()
con.close()
