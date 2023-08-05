from tkinter import *
from webview import WebView, webview
import WebView

root = Tk()
root.title("website viewer")

f1 = Frame(root, bg = "black", width=500, height= 500)
f1.place(x=0, y=50)

web_view = WebView(f1)
web_view.place(x=0, y=0)

def open():
    web_view.load_url("https://www.instagram.com/")
    root.mainloop()

open()