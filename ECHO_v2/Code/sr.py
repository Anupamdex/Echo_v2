from tkinter import *
from functools import partial
import speech_recognition as sr 
import pyttsx3
from threading import *

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def write_it(index, content):
            f = open("data.txt", "r")
            data = f.readlines()
            name = content.capitalize()
            data[int(index)] = name+"\n"
            f =  open("data.txt", "w")
            f.writelines(data)

def main_program_call(obj):
    import application
    write_it(4, obj)
    print("hello "+ obj +", it's nice to meet you.")
    
    engine.say("hello "+ obj +", it's nice to meet you.")
    engine.runAndWait()

    application.main_frame()
        

def error_call():
    engine.say("sorry, i can't hear you !")
    engine.runAndWait()
    engine.say("say once more..")
    engine.runAndWait()


def start_up():
    global ans, m
    m = 1
    while True:
        if m == 1:
            r = sr.Recognizer()
            words = ""
            r.pause_threshold = 1.0
            r.phrase_threshold = 1.0
            r.non_speaking_duration = 1.0

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("listening...")

                write_it(4, " ")

                audio = r.listen(source)
                print("Recognizing...")
                try:
                    words = r.recognize_google(audio)
                    w = words.lower()
                    print("You have said : " + w )

                    keys = w.split(" ")
                    k = keys
                    print (k)
                    
                    for i in k :

                        if words == "":
                            print("Nothing heard")
                            m = 1

                        elif (i == "name") : # verifying name content
                            s = keys.index("is")
                            ans = keys[s+1]
                            print(ans)        # printing name
                            m = 0
                            main_program_call(ans)
                            
                        
                        elif (i == "am"):
                            s = keys.index("am")
                            ans = keys[s+1]
                            print(ans)        # printing name
                            m = 0
                            main_program_call(ans)
                            

                except Exception as e:
                    print(e)
                    if m == 1:
                        error_call()
                        pass
        else:
            break

#start_up()

