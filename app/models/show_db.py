# business logic 을 작성
# 1. python과　mysql 연결: minerva db에 쌓여 있는 sql을 python파일로 내려받는 코드

import MySQLdb
import app.models.config as config
import json


# Connector 클래스: ubuntu서버의 SQL파일을 json으로 dump -> 현재는 클래스가 하나 / 향후에 여러 클래스를 add 가능
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
            json_string = f'{{"id": {id}, "datetime" : "{datetime}", "product_name" : "{product_name}", "brand_name" : "{brand_name}",' \
                          f'"price" : {price}, "amount" : {amount}}}'

            result.append(json_string)
        result = json.dumps(result)

        return result

    def cur_close(self):
        self.db.close()




