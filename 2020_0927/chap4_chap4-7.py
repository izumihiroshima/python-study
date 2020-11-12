import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df = pd.read_csv('FEH_00200524_200927163843.csv', index_col='全国・都道府県', encoding='shift_jis')

# 2019年の列データで棒グラフを作って表示する
df = df.drop('全国', axis=0)
df['2019年'] = pd.to_numeric(df['2019年'].str.replace(',',''))
df['2019年'].plot.bar(figsize=(10, 6))
plt.show()



