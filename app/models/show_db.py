# business logic 을 작성
# 1. python과　mysql 연결: minerva db에 쌓여 있는 sql을 python파일로 내려받는 코드

import json
import MySQLdb
import sys
sys.path.append("..")  # 시스템 path에 상위 폴더 추
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
        self.cur.execute('SELECT * FROM EnglishPremierLeague')
        result = []
        for row in self.cur.fetchall():
            unique_id = row[0]
            Position = row[1]
            club = row[2]
            played = row[3]
            won = row[4]
            drawn = row[5]
            lost = row[6]
            GF = row[7]
            GA = row[8]
            GD = row[9]
            points = row[10]


            json_string = f"""{{
            "id": {unique_id}, 
            "Position": "{Position}", 
            "club": "{club}", 
            "played": "{played}", 
            "won" : {won}, 
            "drawn" : {drawn}, 
            "lost" : "{lost}",
            "GF" : "{GF}",
            "GA" : "{GA}",
            "GD" : {GD},
            "points" : {points},
            }}"""

            result.append(json_string)
        result = json.dumps(result)
        self.db.close()

        return result
