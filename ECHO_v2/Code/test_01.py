import tkinter as tk
import os
from application import *

rel_path = os.getcwd()

class Basewindow(tk.Tk):
    def __init__(self, width, height):
        super().__init__()

        print("Testing window for Application Dummy ")

        self.geometry(f"{width}x{height}")
        self.configure(bg="black")
        self.title("ECHO - The Smart Office Assistant")
        self.resizable(False, False)

        self.o_image = tk.PhotoImage(file=rel_path + "/files/echo_logo.png")
        self.o_label = tk.Label(self, image=self.o_image, bg="black", highlightthickness=0, borderwidth=0)
        self.o_label.place(relx=0.5, rely=0.5, anchor="center")

        self.after(1500, self.load_app)


    def load_app(self):
            # remove all existing contents from the current window
        for widget in self.winfo_children():
            widget.destroy()

        # Load the application_page to base window
        set_screen_size(screen_width, screen_height)
        self.application_page = Application(self, screen_width, screen_height)
        self.application_page.pack(expand=True, fill=tk.BOTH)
            

def get_screensize():
    root = tk.Tk()
    x_width = 800
    x_height = 500
    root.destroy()
    return x_width, x_height


if __name__ == "__main__":
    screen_width, screen_height = get_screensize()
    app = Basewindow(screen_width, screen_height)
    app.mainloop()