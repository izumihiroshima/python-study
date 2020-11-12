import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# ソートをして表示
kokugo = df.sort_values('国語',ascending=False)
print('国語の点数が高いもの順でソート\n',kokugo)



