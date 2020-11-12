import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む(名前の列をインデックスで）
df = pd.read_csv('test.csv', index_col=0)

# 棒グラフを作る
colorlist = ['skyblue','steelblue','tomato','cadetblue','orange','sienna']
df.T.plot.bar(color = colorlist)
plt.legend(loc='lower right')
plt.show()


