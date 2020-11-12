import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 集計（最大値、最小値、平均値、中央値、合計など）をして表示
print('数学の最高点 =', df['数学'].max())
print('数学の最低点 =', df['数学'].min())
print('数学の平均点 =', df['数学'].mean())
print('数学の中央値 =', df['数学'].median())
print('数学の合計 =', df['数学'].sum())

