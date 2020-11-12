import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む(名前の列をインデックスで）
df = pd.read_csv('test.csv', index_col=0)

# 棒グラフを作って表示
df.plot.bar()
plt.legend(loc='lower right')
plt.show()

# 棒グラフ（水平）を作って表示
df.plot.barh()
plt.legend(loc='lower left')
plt.show()

# 積み上げ棒グラフ
df.plot.bar(stacked=True)
plt.legend(loc='lower right')
plt.show()

# 箱ひげグラフ
df.plot.box()
plt.show()

# 面グラフ
df.plot.area()
plt.legend(loc='lower right')
plt.show()




