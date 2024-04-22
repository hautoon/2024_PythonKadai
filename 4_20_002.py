import whisper
import json

model = whisper.load_model("small") #モデル指定
result = model.transcribe("sample.mp4", verbose=True, fp16=False, language="en") #ファイル指定
print(result['text'])

f = open('transcription.txt', 'w', encoding='UTF-8')
f.write(json.dumps(result['text'], sort_keys=True, indent=4, ensure_ascii=False))
f.close()