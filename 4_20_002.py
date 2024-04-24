import whisper
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
model = whisper.load_model("small") #モデル指定
result = model.transcribe("sample.wav", verbose=True, fp16=False, language="en") #ファイル指定
print(result['text'])

f = open('transcription.txt', 'w', encoding='UTF-8')
f.write(json.dumps(result['text'], sort_keys=True, indent=4, ensure_ascii=False))
f.close()