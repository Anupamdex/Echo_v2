# controlling speech recognition & tts source code
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def ask_name():
    speak("Please tell me your name.")
    name = listen_for_audio()
    return name

def listen_for_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Error during speech recognition: {0}".format(e))
        return ""

def greet_with_name(name):
    if name:
        speak("Hello, " + name)
        return "Hello, " + name
    else:
        return "Name not recognized. Please try again."