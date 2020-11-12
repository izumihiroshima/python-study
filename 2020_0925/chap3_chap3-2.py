import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 表データの情報を表示
print('データの件数 = ',len(df))
print('項目名　　　=',df.columns.values)
print('インデックス=',df.index.values)


