from _sqlite3 import Cursor, Row
from distutils.util import execute
from select import select

import pymysql


conn = pymysql.Connect( 
              host = 'localhost',
              port = 3306,
              user = 'root',
              passwd = '123456',
              db = 'report',
              charset = 'utf8'
              )


cursor = conn.cursor()

try:
    sql_select = "select * from ch415 limit 10"
    cursor.execute(sql_select)
    for row in cursor.fetchall():
        print("partyId = %s ,realname = %s ,carPlantNumber = %s" % row)
    print(cursor.rowcount)
    
    sql_insert = "insert into ch415(partyId,realname,carPlateNumber) values (123456 ,'wangjian' ,'黑A123456') "
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    # 
    conn.commit()
    # rs = cursor.fetchone()
    # print(rs)
    # 
    # rs = cursor.fetchmany(21)
    # print(rs) 
    # print(conn)
    # print(cursor)
except Exception as e:
    print(e) 
    conn.rollback()
    
cursor.close()
conn.close()