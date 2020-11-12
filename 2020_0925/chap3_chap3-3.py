import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 1列のデータを表示
print('国語の列データ\n',df['国語'])

# 複数列のデータを表示
print('国語と数学の列データ\n',df[['国語','数学']])


