import sqlite3

conn = sqlite3.connect(r".\files\db\myfirst.db")       # 데이터베이스 연결
cursor = conn.cursor()                                 # 커서 생성
cursor.execute('SELECT * FROM AddressBook')            # 쿼리 실행
for row in cursor.fetchall():                          # 결과 처리
    print(row)
cursor.close()                                         # 커서 닫기
conn.close()                                           # 데이터베이스 연결 닫기
