# business logic 을 작성
# 1. python과　mysql 연결: minerva db에 쌓여 있는 sql을 python파일로 내려받는 코드

import MySQLdb
# python path에 넣었으나 찾지 못해서 path 따로 지정
import app.models.config as config

db = MySQLdb.connect(host = config.HOST,
                     user = config.USER,
                     passwd = config.PASS,
                     db = config.MYDB)
cur = db.cursor()

# to apply SQL
cur.execute('SELECT * FROM coupang_sales_data')

for row in cur.fetchall():
    print(row)

db.close()



