import requests
import json
import config
from datetime import datetime, timedelta, timezone

# 5日間（3時間ごと）の天気を取得する: 東京
url = 'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=jp&units=metric'
url = url.format(city='Tokyo,JP', key=config.api_key)

jsondata = requests.get(url).json()
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata['list']:
    jst = str(datetime.fromtimestamp(dat['dt'], tz))[:-9]
    weather = dat['weather'][0]['description']
    temp = dat['main']['temp']
    print('日時:{jst}, 天気:{w}, 気温:{t}度'.format(jst=jst,
                                             w=weather, t=temp))

    
