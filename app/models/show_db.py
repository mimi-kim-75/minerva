# business logic 을 작성
# 1. python과　mysql 연결: minerva db에 쌓여 있는 sql을 python파일로 내려받는 코드

import MySQLdb
# python path에 넣었으나 찾지 못해서 path 따로 지정
import app.models.config as config
import json

class Connector:
    def __init__(self):
        self.db = MySQLdb.connect(host = config.HOST,
                             user = config.USER,
                             passwd = config.PASS,
                             db = config.MYDB)
        self.cur = self.db.cursor()

    def cur_execute(self):
        # to apply SQL
        self.cur.execute('SELECT * FROM coupang_sales_data')
        result = []
        for row in self.cur.fetchall():
            id = row[0]
            datetime = str(row[1])
            product_name = row[2]
            brand_name = row[3]
            price = row[4]
            amount = row[5]
            json_string = f"{{'id': {id}, 'datetime' : {datetime}, 'product_name' : {product_name}, 'brand_name' : {brand_name}," \
                          f"'price' : {price}, 'amount' : {amount}}}"

            result.append(json_string)
        result = json.dumps(result)
        self.db.close()
        return result




