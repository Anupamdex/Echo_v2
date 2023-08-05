import tkinter as tk
import threading
import time
from PIL import ImageTk,Image

class SlidingImages(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="black")
        self.images = []  # List to store the images
        self.current_image_index = 0

        # Create a label to display the sliding images
        self.image_label = tk.Label(self, bg="black", fg="white", text= "ECHO - The Smart Office Assistant",
                                    font=("calibri", 18), bd= 0, highlightthickness=0, background= "black" )
        self.image_label.pack(expand=True)

        # Start the background task to switch images
        self.start_sliding()

    def set_images(self, images_path):
        self.images = images_path

    def start_sliding(self):
        self.update_image()
        bg_thread = threading.Thread(target=self.sliding_task)
        bg_thread.daemon = True
        bg_thread.start()

    def sliding_task(self):
        while True:
            time.sleep(2)  # Change the delay time for the desired animation speed
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.update_image()

    def update_image(self):
        h_value = self.winfo_screenwidth()
        w_value = self.winfo_screenheight()

        if self.images:
            img = self.images[self.current_image_index]
            raw = Image.open(img)
            resized = raw.resize((h_value, w_value), Image.Resampling.LANCZOS)
            final_image = ImageTk.PhotoImage(resized)
            self.image_label.configure(image=final_image)
            self.image_label.image = final_image  # Keep a reference to prevent garbage collection




