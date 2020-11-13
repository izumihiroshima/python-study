import requests
import json
import config
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# 5日間（3時間ごと）の天気を取得する: 東京
url = 'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=jp&units=metric'
url = url.format(city='Tokyo,JP', key=config.api_key)

jsondata = requests.get(url).json()
df =pd.DataFrame(columns=['気温'])
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata['list']:
    jst = str(datetime.fromtimestamp(dat['dt'], tz))[:-9]
    weather = dat['weather'][0]['description']
    temp = dat['main']['temp']
    df.loc[jst] =temp

df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()
