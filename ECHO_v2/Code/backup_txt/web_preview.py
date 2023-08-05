import tkinterweb
from tkinter import *

root = Tk()
root.geometry("800x500")

parent = Frame(root, height=300, width= 600)


frame = tkinterweb.HtmlFrame(parent)

n = "https://erp.nttftrg.com/"
s = "https://sites.google.com/view/echo-robot"

a = "sites.google.com/view/clickinghub/home"

frame.load_website(a)

frame.place(x=0, y=0)

parent.pack(fill= BOTH, expand= True)

root.mainloop()