from pykakasi import kakasi
kks = kakasi()
word =input("日本語を入力してください")
result = kks.convert(word)
for converted_word in result:
    print(f"{converted_word['hepburn']}", end ="")