import tkinter as tk
import threading
import time
import os
import ultrasonic
from tkinter import PhotoImage
from tkinter import StringVar
from PIL import ImageTk,Image
from sliding_images import SlidingImages
from functools import partial
import controller

import concurrent.futures
import pyttsx3

rel_path = os.getcwd()

class Basewindow(tk.Tk):
    def __init__(self, width, height):
        super().__init__()

        print("Base of Application is created")

        self.geometry(f"{width}x{height}")
        self.configure(bg="black")
        self.title("ECHO - The Smart Office Assistant")
        self.resizable(False, False)

        self.show_logo()

        self.distance_value = 0
        self.start_distance_measurement()

        self.opening_page = None  # Create the opening page instance

    def show_logo(self):
        self.logo_image = tk.PhotoImage(file=rel_path + "/files/echo_logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image, bg="black", highlightthickness=0, borderwidth=0)
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")

        self.after(1500, self.show_sliding_images)

    def show_sliding_images(self):
        # destroy the logo
        for widget in self.winfo_children():
            widget.destroy()

        # create image sliding
        global sliding_images_page
        sliding_images_page = SlidingImages(self)
        sliding_images_page.pack(expand=True, fill=tk.BOTH)

        # add images
        images_path = [
            rel_path + "/files/a1.png",
            rel_path + "/files/a2.png",
            rel_path + "/files/a3.png",
        ]
        sliding_images_page.set_images(images_path)

        global distance_label
        distance_label = tk.Label(self, text="Measured Distance is : cm")
        distance_label.place(relx=0.1, rely=0.9, anchor="center")

    def start_distance_measurement(self):
        # create background thread
        bg_thread = threading.Thread(target=self.background_task)
        bg_thread.daemon = True
        bg_thread.start()

    def background_task(self):
        # for distance measurement
        object_nearby = False
        while True:
            self.distance_value = ultrasonic.dummy()
            time.sleep(3)
            distance_label.config(text="Measured Distance : {:.2f} cm".format(self.distance_value))

            if self.distance_value < 100 and not object_nearby:
                object_nearby = True
                print("object nearby")
                # modify the base window to speech recognition & tts
                time.sleep(4)
                self.show_opening_page()

            elif self.distance_value >= 100 and object_nearby:
                object_nearby = False
                print("object is far away")
            time.sleep(1)


    def show_opening_page(self):
        # Forgetting sliding images
        sliding_images_page.pack_forget()
        # Create the OpeningPage instance
        self.opening_page = OpeningPage(self)
        self.opening_page.pack()


class OpeningPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")

        raw = Image.open(rel_path + "/files/speech/speech_reco.png")
        resized = raw.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
       
        self.opening_image = ImageTk.PhotoImage(resized)
        self.opening_label = tk.Label(self, image= self.opening_image)
        self.opening_label.pack(expand=True, fill=tk.BOTH)

        # Add the text label to display recognized text
        global ab
        ab = StringVar()
        self.dynamic_label = tk.Label(self, textvariable= ab, font= ("comic sans ms", 18 ), fg="black", bg="#E7E7E7")
        self.dynamic_label.place(relx=0.28, rely=0.58)

        self.after(300, self.update_content)
        
    def inst_typing(self, ab, content):
        self.typing( ab, content)

    def inst_speak(self, content):
        controller.speak(content)

    def required_threads(self, out_content):
        subThread_1 = threading.Thread(target= self.inst_typing, args=( ab, out_content))
        subThread_2 = threading.Thread(target= self.inst_speak, args=(out_content, ))

        subThread_1.start()
        subThread_2.start()

        
    def update_content(self):

        self.required_threads("Hello Friend, Welcome to NTTF ", )
        self.after(4000, ab.set , " ") 
        
        self.after(5300, self.required_threads, "Tell me your good Name please . . .", )


    def typing(self, ab, content):
        for i in content:
            base = ab.get()
            ab.set(base+i)
            self.after(50)
            self.update()



def get_screensize():
    root = tk.Tk()
    x_width = root.winfo_screenwidth()
    x_height = root.winfo_screenheight()
    root.destroy()
    return x_width, x_height


if __name__ == "__main__":
    screen_width, screen_height = get_screensize()
    app = Basewindow(screen_width, screen_height)
    app.mainloop()