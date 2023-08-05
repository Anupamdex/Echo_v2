import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.say("welcome to  NTTF")
engine.runAndWait()
engine.say("Hello, I'm ECHO - The smart Robiot Assistant")
engine.runAndWait()


