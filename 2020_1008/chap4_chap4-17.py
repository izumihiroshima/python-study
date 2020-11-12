import folium

# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)

m.save('sabae.html')
