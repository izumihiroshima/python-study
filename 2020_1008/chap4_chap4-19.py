import pandas as pd
import folium

# データフレームを読み込む
df = pd.read_csv('200.csv',encoding='shift-jis')

# 消火器のある地点（緯度、経度）をリスト化する
hydrant = df[['緯度','経度']].values

# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
for data in hydrant:
    folium.Marker([data[0], data[1]]).add_to(m)
m.save('hydrant.html')
