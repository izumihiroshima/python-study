import pandas as pd
import openpyxl

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# ソート（国語の点数が高いもの順)
kokugo = df.sort_values('国語',ascending=False)

# 1つのExcelファイルに複数のシートで出力する
with pd.ExcelWriter('csv_to_excel3.xlsx') as writer:
    df.to_excel(writer, index=False, sheet_name='元のデータ')
    kokugo.to_excel(writer, index=False, sheet_name='国語でそーと')

    




