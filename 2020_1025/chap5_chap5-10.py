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
    jst = str(datetime.fromtimestamp(dat['dt'], tz))[:9]
    print('UST={ust}, JST={jst}'.format(ust=dat['dt_txt'],jst=jst))

    
