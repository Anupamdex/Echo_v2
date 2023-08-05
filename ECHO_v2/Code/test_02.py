from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from functools import partial
import time
from threading import *


w_value = 800
h_value = 500

i = 0

sr_bg = "new_files/speech/speech_reco.png"

def call_sr():
    #sr.start_up()
    pass

def bg_resizer(img, w_value, h_value):        
    raw = Image.open(img)
    #OPEN and RESIZE image
    resized = raw.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final

##
def filler():

    global S3

    SR1 = Thread(target= call_sr)            # 
    SR1.start() 

    def start_PA():
        typing(dynamic_label, "I'm Listening . . .")
        root.after(100)
        one()
        print("one is completeed")
        root.after(2000)
        #two()

    root = Tk()
    root.geometry("800x500")
    F1 = Frame(root, bg= "yellow", width= 800, height= 500)
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

    def one():
        for i in range(0,8,1):
            print(i)
            ab.set("I'm Listening ")
            typing(dynamic_label, " . . .")

            
    def two():
        ab.set("")
        typing(dynamic_label, "What's your name ? ")
        print("say your name please")

    S3 = Thread(target= start_PA)
    S3.start()

    
    def stop():
        root.quit()
    Button(sr_label, text= "continue", command= Thread(target= stop )).place(x=400, y=400)         ##
    
    root.mainloop()

##
#filler()


# on testing #