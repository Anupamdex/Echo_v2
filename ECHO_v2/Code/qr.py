from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import ImageTk, Image

def bg_resizer(raw, w_value, h_value):
    global final     
    file = ImageTk.getimage(raw)
    resized = file.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final

def create(link, base, size):
    global photo
    QR = pyqrcode.create(link)
    QR.png("qr_code.png", scale=8)
    photo = bg_resizer(PhotoImage(file = f"qr_code.png"), size, size)
    base.config(image = photo)


#1 Resize the Qr code as provided dimensions
#2 Generate QR code from Link
"""
How to use this qr.py ?
a = "https://www.instagram.com/" #example
qr.create(a, l1)
"""


