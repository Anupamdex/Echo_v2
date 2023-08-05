from tkinter import *
import time

#root = Tk()

def write_it(content):
    f = open("data.txt", "r")
    data = f.readlines()
    data[3] = content+"\n"
    f =  open("data.txt", "w")
    f.writelines(data)

class time_box:
    def __init__(self, master):
       
        self.time_label = Label(master, text= "", font=("ds-digital",16), fg="white", bg="black")
        self.time_label.pack()

        day_label = Label(master, text= "", font=("Calibri", 13), fg="white", bg="black")
        day_label.pack()

        def clock_on():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")

            day = time.strftime("%A")
            #month = time.strftime("%b")
            #year = time.strftime("%Y")

            self.time_label.config(text= hour + ":" + minute + ":" + second + " " + am_pm)
            day_label.config(text= day)  # + "  " + month + " - " + year)

            #self.time_label.after(1000, threading.Thread(target= clock_on).start())
            #day_label.after(1000, threading.Thread(target= clock_on).start())

            self.time_label.after(1000, clock_on)

            if (int(hour) < 12 and int(int(hour)) > 6 and am_pm == "AM"):
                write_it("Good Morning !")
            elif (int(hour) == 12 or int(hour) < 3 and am_pm == "PM"):
                write_it("Good Afternoon !")
            elif (int(hour) < 7 and int(hour) > 2 and am_pm == "PM"):
                write_it("Good Evening !")
            else:
                write_it("Nice to meet you")

        clock_on()

#e = time_box(root)
