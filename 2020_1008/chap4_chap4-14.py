import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df1 = pd.read_csv('Sample_20201008140116.csv', index_col='時点')
df2 = pd.read_csv('Sample_20201008140330.csv', index_col='時点')
df3 = pd.read_csv('Sample_20201008140311.csv', index_col='時点')

# 3つのグラフを重ねて表示
df1['年平均気温【℃】'].plot()
df2["最高気温（日最高気温の月平均の最高値）【℃】"].plot()
df3["最低気温（日最低気温の月平均の最低値）【℃】"].plot()
plt.ylim(-10,40)
plt.legend(loc='lower right')
plt.show()








