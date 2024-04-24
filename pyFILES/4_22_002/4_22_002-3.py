import pandas as pd

# ファイルを読み込む
df = pd.read_csv("../../titanic3.csv")

# 'fare' 列の値を丸める（小数点以下0桁で丸め）
df['fare'] = df['fare'].round(0)

# 丸め後の 'fare' 列を表示
print(df['fare'])