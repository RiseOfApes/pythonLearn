import pymysql
from _sqlite3 import Cursor, Row
from distutils.util import execute
from select import select
conn = pymysql.Connect( 
              host = 'localhost',
              port = 3306,
              user = 'root',
              passwd = '123456',
              db = 'report',
              charset = 'utf8'
              )


cursor = conn.cursor()
sql = "select * from ch415 limit 100"

cursor.execute(sql)

print(cursor.rowcount)
# 
# rs = cursor.fetchone()
# print(rs)
# 
# rs = cursor.fetchmany(21)
# print(rs)

rs = cursor.fetchall()
for row in rs:
    print("one=%s ,two=%s ,three=%s" % row)
print(rs)
# print(conn)
# print(cursor)

cursor.close()
conn.close()