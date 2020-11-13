import requests
import json
import config
from pprint import pprint

# 現在の天気を取得する: 神戸
url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=units=metric'
url = url.format(city='Kobe,JP', key=config.api_key)

jsondata = requests.get(url).json()
pprint(jsondata)

