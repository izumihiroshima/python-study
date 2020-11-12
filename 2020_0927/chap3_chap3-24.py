import pandas as pd
import openpyxl

# Excelファイルを読み込む
df = pd.read_excel('csv_to_excel3.xlsx')
print(df)
df = pd.read_excel('csv_to_excel3.xlsx', sheet_name='国語でそーと')
print(df)


