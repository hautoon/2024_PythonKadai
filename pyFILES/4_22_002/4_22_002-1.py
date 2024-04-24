import pandas as pd

# ファイルを読み込む
df = pd.read_csv("../../titanic3.csv")

# 'name' 列のデータを小文字に変換
df['name'] = df['name'].str.lower()

# 変換後の 'name' 列を表示
print(df['name'])