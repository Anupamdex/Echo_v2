from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from functools import partial
from threading import *
import speech_recognition as sr 
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def voice_pi(obj):
    
        mytext = "hello "+ obj +", it's nice to meet you."
        engine.say(mytext)
        engine.runAndWait()

w_value = 800
h_value = 500

i = 0

sr_bg = "files/speech/speech_reco.png"

def bg_resizer(img, w_value, h_value):        
    raw = Image.open(img)
    #OPEN and RESIZE image
    resized = raw.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final

def start_up():

    c = 0
    while True:
        r = sr.Recognizer()
        words = ""
        r.pause_threshold = 1.0
        r.phrase_threshold = 1.0
        r.non_speaking_duration = 1.0

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            engine.say("welcome to  NTTF")
            engine.say("Hello, I'm ECHO - The smart Robiot Assistant")

            engine.say("I'm Listening.. ?")
            engine.say("whats your name ?")
            engine.runAndWait()
            print("listening...")

            audio = r.listen(source)
            print("Recognizing...")
            try:
                words = r.recognize_google(audio)
                w = words.lower()
                print("You have said : " + w )

                keys = w.split(" ")
                #k = list(set(keys))
                k = keys
                print (k)

                def working():
                    engine.say("if you want to know more, please access the buttons")
                
                for i in k :
                    if words == "":
                        #print("Nothing heard"
                        pass

                    if (i == "name") : # verifying name content
                        s = keys.index("is")
                        print("you are saying something about your name ?")
                        ans = keys[s+1]
                        print(ans)        # printing name
                        voice_pi(ans)
                        working()

                    elif (i == "am"):
                        s = keys.index("am")
                        print("you are saying something about your name ?")
                        print(ans)        # printing name
                        voice_pi(ans)
                        working()

            except Exception as e:
                print(e)
                
                if c < 2 :
                    engine.say("sorry, i can't hear you !")
                    engine.say("say once more..")
                else:
                    engine.say("i'm experiencing poor connectivity. please check the internet")
                    working()
            c = c+1
                    
def sr_window():

    '''def start_PA():
        typing(dynamic_label, "I'm Listening . . .")
        root.after(100)
        one()
        print("one is completeed")
        root.after(2000)
        #two()'''

    root = Tk()
    root.geometry("800x500")
    F1 = Frame(root, bg= "black", width= 800, height= 500)
    F1.place(x=0, y=0)

    re_sr_bg = bg_resizer(sr_bg, w_value, h_value)
    sr_label = Label(F1, image= re_sr_bg, border=0, highlightthickness=0).place(x=0, y=0)

    ab = StringVar()
    dynamic_label = Label(sr_label, textvariable= ab, font= ("comic sans ms", 18 ), fg="black", bg="#E7E7E7")
    dynamic_label.place(relx=0.28, rely=0.58)

    def typing(base, content):
        for i in content:
            base = ab.get()
            ab.set(base+i)
            root.after(50)
            root.update()

    root.mainloop()

    '''def one():
        for i in range(0,8,1):
            print(i)
            ab.set("I'm Listening ")
            typing(dynamic_label, " . . .")

            
    def two():
        ab.set("")
        typing(dynamic_label, "What's your name ? ")
        print("say your name please")'''

    '''S3 = Thread(target= start_PA)
    S3.start()'''

    
    '''  def stop():
        root.quit()
    Button(sr_label, text= "continue", command= Thread(target= stop )).place(x=400, y=400)         ##
    '''




'''def onebyone():
    t1 = Thread(target= start_up)
    t1.start()
'''


# needed func
#sr_window()

# not neccessary
#start_up()

