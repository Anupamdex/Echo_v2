from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from functools import partial
import webview

w_value = 800
h_value = 500

root = Tk()
root.geometry(str(w_value)+"x"+str(h_value))

def bg_resizer(img, w_value, h_value):        
    #raw = Image.open(img)
    #OPEN and RESIZE image
    resized = img.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final


page = Image.open("files/page_bg.png")
exit_b = Image.open("files/exit_b0.png")
content_box = Image.open("files/content_box.png")

re_bg = bg_resizer(page, w_value, h_value)
e_b = bg_resizer(exit_b, int(w_value/8), int(h_value/8))

def exit_main_page():                   # change the commands
    pass
    print("exit from sub page content")

def call():                             # assign to another function call
    print("button pressed")
    pass


F1 = Frame(root, bg= "black", width= w_value, height= h_value)
F1.place(x=0, y=0)
page_label = Label(F1, image= re_bg, border=0, highlightthickness=0)
page_label.place(x=0, y=0)
re_content_box = bg_resizer(content_box, int(int(w_value)*(6/8)), int(int(h_value)*(4/5)))

content_label = Label(page_label, image= re_content_box, border=0, highlightthickness= 0)
content_label.place(relx= 0.5, rely= 0.5, anchor= CENTER)

def exit_sub_page():
    content_sub_label.place_forget()
    sub_footer_label.pack_forget()
    sub_exit.place_forget()

def container(sub_footer):
    global content_sub_label, sub_exit, sub_footer_label
    #Label(content_label, width= 800, height= 500).place(x=0, y=0)
    content_sub_label = Label(page_label, image= re_content_box, border=0, highlightthickness= 0)
    content_sub_label.place(relx= 0.5, rely= 0.5, anchor= CENTER)
    sub_exit = Button(page_label, image= e_b, border=0
                           , highlightthickness=0, activebackground="black", command= exit_sub_page)
    sub_exit.place(relx= 0.9, rely= 0.85, anchor= CENTER)
    sub_footer_label = Label(content_sub_label, text= sub_footer, font=("calibri", int(int(h_value)/35), "italic"), bg="black", fg="white")
    sub_footer_label.place(relx=0.14, rely=0.92, anchor= CENTER) 


'''    ###
    def web_open():

        subframe = Frame(F1, height=500, width= 500)
        subframe.place(x=0, y=0)

        webview.create_window(subframe, 'Geeks for Geeks', 'https://geeksforgeeks.org',x=100, y= 100, height= 400, width= 600, fullscreen= False, resizable= False)
        webview.start()

    web_open() 
     
    ###   '''


main_exit = Button(page_label, image= e_b, border=0, highlightthickness=0, command= exit_main_page)
main_exit.place(relx= 0.9, rely= 0.85, anchor= CENTER)

#Label(content_label, text= "text", fg="white", bg="black", font=("calibri", "14", "italic")).place(relx=0.1, rely=0.92, anchor= CENTER)

"comic sans ms"
root.mainloop()


# reserved for testing sub buttons and pages and exit functions
