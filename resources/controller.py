# controlling speech recognition & tts source code
import speech_recognition as sr
import pyttsx3

import os
rel_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

def speak(text):
    engine = pyttsx3.init() #for raspberry pi, pass argument : driverName= 'espeak'
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def greet_with_name(name):
    if name:
        speak("Hello, " + name)
        return "Hello, " + name
    else:
        return "Name not recognized. Please try again."
    
def clear_prev_rec_name():
    with open(os.path.join(rel_path, "data.txt"), "r") as file:
        lines = file.readlines()
        lines[4] = " " +"\n"
    with open(os.path.join(rel_path, "data.txt"), "w") as file:
        file.writelines(lines)


def ask_name():
    listen_for_audio()
    #speak("Please tell me your name.")
    #name = listen_for_audio()
    #return name

def listen_for_audio():
    clear_prev_rec_name()
    global ans
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout = 5)
    try:
        words = recognizer.recognize_google(audio)
        #
        w = words.lower()
        print("You have said : " + w )

        keys = w.split(" ")
        #k = list(set(keys))
        k = keys
        print (k)

        def working(content):
            with open(os.path.join(rel_path, "data.txt"), "r") as file:
                lines = file.readlines()
                lines[4] = content +"\n"
            with open(os.path.join(rel_path, "data.txt"), "w") as file:
                file.writelines(lines)

            speak("if you want to know more, please access the application buttons")
                
        for i in k :
            if words == "":
                #print("Nothing heard")
                pass

            if (i == "name") : # verifying name content
                s = keys.index("is")
                print("i am finding your name.. its.. ")
                ans = keys[s+1]
                print(ans)        # printing name
                greet_with_name(ans)
                working(ans)

            elif (i == "am"):
                s = keys.index("am")
                print("i am finding your name.. its.. ")
                ans = keys[s+1]
                print(ans)        # printing name
                greet_with_name(ans)
                working(ans)
            
            else :
                #ans = i
                #print(ans)          # assuming it would be the name and printing name
                #greet_with_name(ans)
                #working()
                pass

        return  i


    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Could not recognize the name at the moment")
        return ""
    except sr.RequestError as e:
        print("Error during speech recognition: {0}".format(e))
        speak("please confirm your internet connectivity")
        return ""

#
