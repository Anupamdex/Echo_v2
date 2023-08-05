from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from functools import partial
import sr
import time
from threading import *
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

#w_value = 800
#h_value = 500

def bg_resizer(raw, w_value, h_value):
    global final     
    file = ImageTk.getimage(raw)
    resized = file.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final

def typing(root, ab, base, content):
    for i in content:
        base = ab.get()
        ab.set(base+i)
        root.after(50)
        root.update()

def sr_window(base, w_value, h_value):
    global ab

    sr_bg = PhotoImage(file = f"files/speech/speech_reco.png")

    re_sr_bg = bg_resizer(sr_bg, w_value, h_value)
    sr_label = Label(base, image= re_sr_bg, border=0, highlightthickness=0).place(x=0, y=0)

    ab = StringVar()
    dynamic_label = Label(sr_label, textvariable= ab, font= ("comic sans ms", 18 ), fg="black", bg="#E7E7E7")
    dynamic_label.place(relx=0.28, rely=0.58)
    
    def greet_tts():
        engine.say("welcome to  NTTF")
        engine.runAndWait()
        engine.say("Hello, I'm ECHO - The smart Robot Assistant")
        engine.runAndWait()
    tts1 = Thread(target= greet_tts)
    tts1.start()

    typing(dynamic_label, ab, base, "Welcome to  NTTF ")
    time.sleep(2)
    ab.set("")
    typing(dynamic_label, ab, base, "Hello, ")
    typing(dynamic_label, ab, base, "I'm Echo . . .")
    for i in range(0,5,1):
        time.sleep(0.25)
        ab.set("I'm Listening ")
        typing(dynamic_label, ab, base, " . . .")

    def pytts_1():
        engine.say("What's your Name ?")
        engine.runAndWait()
        ab.set("")
    pytts_1()

    def pytts_2():
        def t1():
            sr.start_up()
            # Running Speach Recognition program 
        def t2():
            for i in range(0,5,1):
                time.sleep(0.25)
                ab.set("What's your Name ?")
                typing(dynamic_label, ab, base, " . . .")

        Thread(target= t1).start()
        Thread(target= t2).start()

    tts3 = Thread(target= pytts_2)
    tts3.start()

    

    #root.mainloop()

# needed func
#sr_window()



