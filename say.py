import win32com.client as win

speak = win.Dispatch("SAPI.SpVoice")
speak.Speak("come on")
speak.Speak("你好")
