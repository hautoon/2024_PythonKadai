import pandas as pd
import matplotlib.pyplot as plt

# ファイルを読み込む
df = pd.read_csv("../../titanic3.csv")

# ヒストグラムを描画
plt.hist(df['age'].dropna(), bins=20)  # NaN値を除外してヒストグラムを描画
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()