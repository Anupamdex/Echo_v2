
from tkinter import *
from threading import *
import time

global key

def main():

    # main program of servo motor
    print("is printing really happening ? ")
    pass

def verify():
    if key == 0:
        main()

def edit_servo():

    root = Tk()
    root.geometry("580x400")
    root.title("config window",)
    root.resizable(False, False)



    def call_adv_settings():
        pass

    bg = Frame(root, height=400, width=580, border=1)
    bg.place(x=0, y=0)
    Label(root, text="Servo Setings", font=("Calibri, 18")).place(x=20, y=40)
    Label(root, text="Left Hand Shoulder :",  fg="green", font=("Helvetica, 13",)).place(x=20, y=110)
    Label(root, text="Left Middle joint :",  fg="green", font=("Helvetica, 13",)).place(x=20, y=160)
    Label(root, text="Left Hand palm :",  fg="green", font=("Helvetica, 13",)).place(x=20, y=210)
    Label(root, text="Right Hand Shoulder :",  fg="green", font=("Helvetica, 13",)).place(x=280, y=110)
    Label(root, text="Right Middle joint :",  fg="green", font=("Helvetica, 13",)).place(x=280, y=160)
    Label(root, text="Right Hand palm :",  fg="green", font=("Helvetica, 13",)).place(x=280, y=210)
    Label(root, text="Head Motion :",  fg="green", font=("Helvetica, 13",)).place(x=20, y=260)

    def set_default():
        click_1.set("Servo 1")
        click_2.set("Servo 2")
        click_3.set("Servo 3")
        click_4.set("Servo 4")
        click_5.set("Servo 5")
        click_6.set("Servo 6")
        click_7.set("Servo 7")

    Button(root, text="Apply", command= root.destroy).place(x=100, y=320)
    Button(root, text="Reset to default", command= set_default).place(x=300, y=320)


    options = ["Servo 1","Servo 2","Servo 3","Servo 4","Servo 5","Servo 6","Servo 7"]
    click_1 = StringVar()
    click_2 = StringVar()
    click_3 = StringVar()
    click_4 = StringVar()
    click_5 = StringVar()
    click_6 = StringVar()
    click_7 = StringVar()

    OptionMenu(bg, click_1, *options).place(x=180, y=105)
    OptionMenu(bg, click_2, *options).place(x=180, y=155)
    OptionMenu(bg, click_3, *options).place(x=180, y=205)
    OptionMenu(bg, click_4, *options).place(x=450, y=105)
    OptionMenu(bg, click_5, *options).place(x=450, y=155)
    OptionMenu(bg, click_6, *options).place(x=450, y=205)
    OptionMenu(bg, click_7, *options).place(x=180, y=255)



    root.mainloop()


def edit():
    key = 1
    edit_servo()

def run_servo():
    key = 0


##
#edit()
