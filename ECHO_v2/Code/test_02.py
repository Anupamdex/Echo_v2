import tkinter as tk
from PIL import ImageTk,Image
import os
import tkinterhtml as html
from tkinter import ttk
import webbrowser


    
class WebPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


class WebFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #self.geometry(str(screen_width)+"x"+str(screen_height))
        self.configure(bg="black")
        self.geometry("65x65")

        # create a notebook widget 
        self.notebook = ttk.Notebook(self)
        self.mainpage = WebPage(self)

        self.fsub = tk.Frame(self, height= 65, width= 65, bg= "black")
        self.fsub.place(x=0, y=0)

        self.button = tk.Button(self.fsub, text = "go to", command= self.open_webpage)
        self.button.place(x=0, y=0)
        

    def open_webpage(self):

        self.notebook.add(self.mainpage, state= "hidden",)
        self.notebook.place(x=0, y=0)
        webbrowser.open("www.x.com")


if __name__ == "__main__":
 
    app = WebFrame()
    app.mainloop()