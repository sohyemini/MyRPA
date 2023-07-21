import sqlite3
con = sqlite3.connect(r".\files\db\myfirst.db")
cur = con.cursor()

cellNumber = ['010-1234-5678', '010-4456-2345', '010-5434-5345', '010-2407-6520']
address = ['인천시 연수동', '경기도 여주시', '서울 강서구', '부산 기장구']

for i in range(1, 5, 1):
    cur.execute("INSERT INTO AddressBook VALUES (?, ?, ?);",
                (i, cellNumber[i-1], address[i-1]))

con.commit()
cur.close()
con.close()
