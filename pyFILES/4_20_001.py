import pandas as pd

# CSVデータを読み込むための文字列。実際にはファイルパスを指定します。
data = data = """gender,race/ethnicity,parental level of education,lunch,test preparation course,math score,reading score,writing score
male,group E,associate's degree,standard,none,90,74,68
male,group B,some college,free/reduced,none,60,55,62
male,group B,associate's degree,free/reduced,none,47,52,51
male,group E,master's degree,standard,completed,89,73,73
female,group E,some college,standard,none,64,78,81
male,group D,some high school,standard,completed,60,70,62
female,group D,some college,free/reduced,completed,48,53,57
female,group B,high school,free/reduced,none,60,78,74
female,group D,master's degree,standard,completed,94,100,100
female,group E,some high school,standard,none,63,73,73
"""

# 文字列からデータフレームを作成
from io import StringIO
df = pd.read_csv(StringIO(data))
df.columns = [col.strip() for col in df.columns]
# "average" カラムを計算して追加
df['average'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Excelファイルに保存
df.to_excel('output.xlsx', index=False, engine='openpyxl')