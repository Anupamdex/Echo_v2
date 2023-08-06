import tkinter as tk
from PIL import ImageTk,Image
import os
from sliding_images import SlidingImages
import qr

rel_path = os.getcwd()

class testing(tk.Tk):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        
        self.geometry(str(screen_width)+"x"+str(screen_height))
        self.configure(bg="black")

        self.content_sub_label = tk.Canvas(self, width=800, height=500, bd=0,)
        self.content_sub_label.place(relx=0.5, rely=0.5, anchor="center")

        self.show_qr("www.nothing.com", "home" )


    def show_qr(self, link, gallery):
        qr_label = tk.Label(self.content_sub_label, image= "")
        qr_label.place(relx=0.5, anchor= "n")

        qr.create(link, qr_label, 160)
                    
                    # create image sliding
        global sliding_images_page
        sliding_images_page = SlidingImages(self)
        #sliding_images_page.pack(expand=True, fill=tk.BOTH)

                    # add images
        images_path = [
            rel_path + "/new_files/"+gallery+"/a1.png",
            rel_path + "/new_files/"+gallery+"/a2.png",
            rel_path + "/new_files/"+gallery+"/a3.png",
            ]
        
        sliding_images_page.set_images(images_path)

        pic_label = tk.Label(self.content_sub_label, image = sliding_images_page, highlightthickness=0, bd=0, width= 600, height= 400)
        pic_label.place(relx= 0.35, rely= 0.45, anchor= "center")



if __name__ == "__main__":
    app = testing(800, 500)
    app.mainloop()