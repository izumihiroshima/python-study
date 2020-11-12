import pandas as pd
import openpyxl

# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# Excelファイルを読み込む
df = pd.read_excel('csv_to_excel2.xlsx')
print(df)


