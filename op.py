import speech_recognition as sr
import os
import win32com.client as win


# 初始化识别器
recognizer = sr.Recognizer()
# 初始化语音发声器
speak = win.Dispatch("SAPI.SpVoice")
# 录制声音
with sr.Microphone() as source:
    print("请说话...")
    audio = recognizer.listen(source)

try:
    # 使用Google Web Speech API进行语音识别
    text = recognizer.recognize_google(audio, language="zh-CN")
    # print("你说了:", text)

    # 如果识别到"原神"，回复"启动"
    if "元神" in text:
        print("原神")
        speak.Speak("启动")
        print("启动")
except sr.UnknownValueError:
    print("无法识别音频")
except sr.RequestError as e:
    print("无法连接到Google Web Speech API: {0}".format(e))