import requests
import json
from pprint import pprint

# 5日間(3時間ごと）の天気を取得する: 東京
url = 'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=jp&units=metric'
url = url.format(city='Tokyo,JP', key='d78e9f8fc401c30f8c284c36bb1b2a83')

jsondata = requests.get(url).json()
pprint(jsondata)

