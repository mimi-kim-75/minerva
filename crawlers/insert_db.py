import MySQLdb
from config import db_config


# Connector 클래스
class Connector:
    def __init__(self):
        self.db = MySQLdb.connect(host = db_config.HOST,
                                  user = db_config.USER,
                                  passwd = db_config.PASS,
                                  db = db_config.MYDB)
        self.cur = self.db.cursor()

    def cur_insert(self,
                   channel,
                   brand,
                   product_name,
                   real_price,
                   product_size,
                   product_material,
                   product_shape,
                   product_pattern,
                   pick,
                   purchase,
                   review,
                   sellers_number,
                   sales_date):

        mysql_insert_query = f"""
            INSERT INTO shopFryingpan (
            channel, 
            brand, 
            product_name, 
            real_price, 
            product_size, 
            product_material,
            product_shape,
            product_pattern, 
            pick, 
            purchase, 
            review, 
            sellers_number, 
            sales_date
            ) VALUES (
            {channel}, 
            {brand}, 
            {product_name}, 
            {real_price}, 
            {product_size}, 
            {product_material}, 
            {product_shape},
            {product_pattern}, 
            {pick}, 
            {purchase}, 
            {review}, 
            {sellers_number}, 
            {sales_date}
            )"""

        self.cur.execute(mysql_insert_query)
        self.db.commit()

        print("Record inserted successfully into shopFryingpan table")

        self.db.close()
        print("MySQL connection is closed")
