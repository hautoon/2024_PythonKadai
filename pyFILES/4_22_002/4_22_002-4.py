import pandas as pd

# ファイルを読み込む
df = pd.read_csv("../../titanic3.csv")

# 'fare' 列の欠損値をその列の平均値で補完
fare_mean = df['fare'].mean()  # 'fare' 列の平均値を計算
df['fare'] = df['fare'].fillna(fare_mean)  # 欠損値を平均値で補完

# 補完後の 'fare' 列を表示
print(df['fare'])