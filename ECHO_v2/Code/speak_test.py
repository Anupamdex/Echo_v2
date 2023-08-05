import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

print("im speaking")
engine.say("welcome to  NTTF")
engine.runAndWait()

