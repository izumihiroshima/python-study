import pandas as pd

# データフレームを読み込む
df1 = pd.read_csv('Sample_20201008140116.csv', index_col='時点')
df2 = pd.read_csv('Sample_20201008140311.csv', index_col='時点')
df3 = pd.read_csv('Sample_20201008140330.csv', index_col='時点')

print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)







