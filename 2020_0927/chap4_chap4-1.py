import pandas as pd

# データフレームを読み込む
df = pd.read_csv('13TOKYO.CSV', header=None, encoding='shift_jis')
print(len(df))
print(df.columns.values)



