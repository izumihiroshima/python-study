import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む(名前の列をインデックスで）
df = pd.read_csv('2020_tenkara.csv', index_col=0)

# 棒グラフを作る
df.T.plot.bar()
plt.legend(loc='lower right')
plt.show()

