import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# グラフを作って表示する
df.plot()
plt.show()

