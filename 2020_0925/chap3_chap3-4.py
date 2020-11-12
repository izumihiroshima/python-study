import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 1行のデータを表示
print('B介のデータ\n',df.loc[1])

# 複数の列のデータを表示
print('B介とC子のデータ\n',df.loc[[1,2]])

# 指定した行の指定した列のデータを表示
print('C子の国語データ\n',df.loc[2]['国語'])


