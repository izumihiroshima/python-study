import requests
import json
from pprint import pprint

# 現在の天気を取得する: 神戸
url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=units=metric'
url = url.format(city='Kobe,JP', key='d78e9f8fc401c30f8c284c36bb1b2a83')

jsondata = requests.get(url).json()
print('都市名　　= ', jsondata['name'])
print('気温　　　= ', jsondata['main']['temp'])
print('天気　　　= ', jsondata['weather'][0]['main'])
print('天気詳細　= ', jsondata['weather'][0]['description'])

