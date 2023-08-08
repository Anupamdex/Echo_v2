from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import ImageTk, Image

root = Tk()

def bg_resizer(raw, w_value, h_value):
    global final     
    file = ImageTk.getimage(raw)
    resized = file.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final

def create(link, size):
    global photo
    QR = pyqrcode.create(link)
    QR.png("qr_code.png", scale=8)
    photo = bg_resizer(PhotoImage(file = f"qr_code.png"), size, size)

create("www.x.ai", 50)
