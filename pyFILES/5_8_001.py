from janome.tokenizer import Tokenizer
from collections import Counter

# 日本語テキスト
text = """
山路を登りながら、こう考えた。智に働けば角が立つ。情に棹させば流される。意地を通せば窮屈だ。とかくに人の世は住みにくい。住みにくさが高じると、安い所へ引き越したくなる。どこへ越しても住みにくいと悟った時、詩が生れて、画が出来る。人の世を作ったものは神でもなければ鬼でもない。やはり向う三軒両隣りにちらちらするただの人である。ただの人が作った人の世が住みにくいからとて、越す国はあるまい。あれば人でなしの国へ行くばかりだ。人でなしの国は人の世よりもなお住みにくかろう。越す事のならぬ世が住みにくければ、住みにくい所をどれほどか、寛容て、束の間の命を、束の間でも住みよくせねばならぬ。ここに詩人という天職が出来て、ここに画家という使命が降る。あらゆる芸術の士は人の世を長閑にし、人の心を豊かにするが故に尊い。
"""

# 形態素解析器を用意
tokenizer = Tokenizer()

# 単語のカウント
word_count = Counter()

# テキストを形態素解析
tokens = tokenizer.tokenize(text)
for token in tokens:
    part_of_speech = token.part_of_speech.split(',')[0]
    # 名詞、動詞、形容詞のみをカウント
    if part_of_speech in ['名詞', '動詞', '形容詞']:
        word_count[token.base_form] += 1

# 最も頻出する単語トップ2を取り出す
most_common_words = word_count.most_common(2)

# 結果の表示
print("最も頻出する単語トップ2:")
for word, count in most_common_words:
    print(f"{word}: {count}回")
