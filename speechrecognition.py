import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print(0)
    r.adjust_for_ambient_noise(source)
    print(1)
    audio = r.listen(source)
    print(2)

print(r.recognize_google(audio, language='zh-CN')) #language='zh-CN'识别成中文


