import requests
import json
from pprint import pprint

# 現在の天気を取得する: 神戸
url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=units=metric'
url = url.format(city='Kobe,JP', key='d78e9f8fc401c30f8c284c36bb1b2a83')

jsondata = requests.get(url).json()
pprint(jsondata)

