import MySQLdb
import sys
# sys.path.append("..")  # 시스템 path에 상위 폴더 추

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
                   Position,
                   club,
                   played,
                   won,
                   drawn,
                   lost,
                   GF,
                   GA,
                   GD,
                   points):
        Position = Position
        club = club
        played = played
        won = won
        drawn = drawn
        lost = lost
        GF = GF
        GA = GA
        GD = GD
        points = points

        mysql_insert_query = f"""
            INSERT INTO shopFryingpan (
            `id`,
            `Position`, 
            `club`, 
            `won`, 
            `drawn`, 
            `lost`, 
            `GF`,
            `GA`,
            `GD`, 
            `points`, 
            ) VALUES (
            NULL,
            '{Position}', 
            '{club}', 
            '{played}', 
            {won}, 
            {drawn}, 
            '{lost}', 
            '{GF}',
            '{GA}', 
            {GD}, 
            {points}, 
           
            )"""

        self.cur.execute(mysql_insert_query)
        self.db.commit()

        print("Record inserted successfully into shopFryingpan table")

        self.db.close()
        print("MySQL connection is closed")
