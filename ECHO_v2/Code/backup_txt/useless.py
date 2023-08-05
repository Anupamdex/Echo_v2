from tkinter import *
from PIL import ImageTk,Image


'''
ach_c3 = PhotoImage(f"files/achieve/ach_3.png")
print(ach_c3)
'''
img = "files/achieve/ach_3.png"
raw = Image.open(img)
print(raw)