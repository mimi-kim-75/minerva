# business logic 을 작성
# 1. python과　mysql 연결: minerva db에 쌓여 있는 sql을 python파일로 내려받는 코드

import json
import MySQLdb
from config import db_config


# Connector 클래스: ubuntu서버의 SQL파일을 json으로 dump -> 현재는 클래스가 하나 / 향후에 여러 클래스를 add 가능
class Connector:
    def __init__(self):
        self.db = MySQLdb.connect(host = db_config.HOST,
                                  user = db_config.USER,
                                  passwd = db_config.PASS,
                                  db = db_config.MYDB)
        self.cur = self.db.cursor()

    def cur_execute(self):
        # to apply SQL
        self.cur.execute('SELECT * FROM shopFryingpan')
        result = []
        for row in self.cur.fetchall():
            unique_id = row[0]
            channel = row[1]
            brand = row[2]
            product_name = row[3]
            real_price = row[4]
            product_size = row[5]
            product_material = row[6]
            product_shape = row[7]
            product_pattern = row[8]
            pick = row[9]
            purchase = row[10]
            review = row[11]
            seller_number = row[12]
            sales_date = row[13]

            json_string = f"""{{
            "id": {unique_id}, 
            "channel": "{channel}", 
            "brand": "{brand}", 
            "product_name": "{product_name}", 
            "real_price" : {real_price}, 
            "product_size" : {product_size}, 
            "product_material" : "{product_material}",
            "product_shape" : "{product_shape}",
            "product_pattern" : "{product_pattern}",
            "pick" : {pick},
            "purchase" : {purchase},
            "review" : {review},
            "seller_number" : {seller_number},
            "sales_date" : "{sales_date}"
            }}"""

            result.append(json_string)
        result = json.dumps(result)
        self.db.close()

        return result
