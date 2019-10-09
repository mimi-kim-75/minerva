from insert_db import Connector
# parse following data - navershopping
# 크롤러 구현해야 함

channel = "naver"
brand = "brand"
product_name = "name"
real_price = 10000
product_size = 10
product_material = "metal"
product_shape = "round"
product_pattern = "flower"
pick = 10000
purchase = 8000  # naver only
review = 4000  # naver only
sellers_number = 50  # naver only
sales_date = "2018.04"  # naver only

# insert DB
connector = Connector()
connector.cur_insert(
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
)
