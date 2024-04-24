import pandas as pd

# ファイルを読み込む
df = pd.read_csv("../../titanic3.csv")

# 'age' 列を適切なデータタイプに変換し、不可能ならば NaN にする
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# 外れ値を識別する（100歳以上など）
outliers = df[df['age'] > 100]

# 異常値があれば表示する
if not outliers.empty:
    print("Identified outliers in 'age':")
    print(outliers)

# 異常値（100歳以上）を除外する
df = df[df['age'] <= 100]

# NaN を含む行を削除
df = df.dropna(subset=['age'])

# 結果を確認
print("Corrected 'age' data:")
print(df['age'])