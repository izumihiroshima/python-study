import pandas as pd

# データフレームを読み込む
df = pd.read_csv('13TOKYO.CSV', header=None, encoding='shift_jis')
print(len(df))
print(df.columns.values)

# 「2」の列が「1600006」の住所を抽出して表示
results = df[df[2] == 1600006]
print(results[[2,6,7,8]])



