import pandas as pd
import requests

# URLからデータをダウンロード
url = "exams.csv"

# データをDataFrameに読み込む
data = pd.read_csv(url)

# 各行で'average'を計算し、新しいカラムとして追加
data['average'] = str(data.mean(axis=1))

# DataFrameをExcelファイルに保存
data.to_excel('output.xlsx', index=False)