import pandas as pd

# ファイルを読み込む
df = pd.read_csv("../../titanic3.csv")

# 'age' 列の欠損値を含む行を削除
df = df.dropna(subset=['age'])

# 結果を表示
print(df['age'])