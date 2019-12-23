from insert_db import Connector
# parse following data - navershopping
# """write crawler here"""
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/tables')

try:
    driver.find_element_by_css_selector('.closeBtn').click()
except:
    print("no layer")

eplranking_selector = driver.find_element_by_css_selector('#mainContent')
items = eplranking_selector.find_elements_by_css_selector('.tableBodyContainer tr:not(.expandable)')

df = pd.DataFrame(columns=["Position", "club", "played", "won", "drawn", "lost", "GF", "GA", "GD", "points"])

for i in range(20):
    Position = items[i].find_elements_by_css_selector('tr>#Tooltip')[0].text
    club = items[i].find_elements_by_css_selector('td>a')[0].text
    played = items[i].find_elements_by_css_selector('td')[3].text
    won = items[i].find_elements_by_css_selector('td')[4].text
    drawn = items[i].find_elements_by_css_selector('td')[5].text
    lost = items[i].find_elements_by_css_selector('td')[6].text
    GF = items[i].find_elements_by_css_selector('td')[7].text
    GA = items[i].find_elements_by_css_selector('td')[8].text
    GD = items[i].find_elements_by_css_selector('td')[9].text
    points = items[i].find_elements_by_css_selector('td')[10].text

    data = {"Position": Position,
            "club": club,
            "played": played,
            "won": won,
            "drawn": drawn,
            "lost": lost,
            "GF": GF,
            "GA": GA,
            "GD": GD,
            "points": points}

    # df.loc[len(df)] = data

    driver.close
#
Posigtion = Position
club = club
played = played
won = won
drawn = drawn
lost = lost
GF = GF
GA = GA
GD = GD
points = points
# insert DB
connector = Connector()
connector.cur_insert(
    Position,
    club,
    played,
    won,
    drawn,
    lost,
    GF,
    GA,
    GD,
    points,
)
