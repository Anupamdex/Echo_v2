
import tkinter as tk
import os
from PIL import ImageTk,Image
import time
from sliding_images import SlidingImages
import threading
from tkinter import messagebox
from functools import partial
import edit_app_
import qr
import webbrowser
from tkinter import ttk


# updated code

rel_path = os.getcwd()

class Application(tk.Frame):
    def __init__(self, master, screen_width, screen_height):
        super().__init__(master)
        self.master = master
        self.configure(bg="black")

        print(" This snippet of code is running from application.py > working fine.")
        
        #Resources
        
        self.welcome_bg_image = self.image_resize(rel_path + "/files/background.png", adaptive_width, adaptive_height )
        self.main_b1_image = self.image_resize(rel_path + "/files/img0.png", bt_size, bt_size)
        self.main_b2_image = self.image_resize(rel_path + "/files/img1.png", bt_size, bt_size)
        self.main_b3_image = self.image_resize(rel_path + "/files/img2.png", bt_size, bt_size)
        self.main_b4_image = self.image_resize(rel_path + "/files/img3.png", bt_size, bt_size)
        self.main_b5_image = self.image_resize(rel_path + "/files/img4.png", bt_size, bt_size)
        self.main_b6_image = self.image_resize(rel_path + "/files/img5.png", bt_size, bt_size)
        self.exit_b_image = self.image_resize(rel_path + "/files/exit_b0.png", int(int(adaptive_width)/8), int(int(adaptive_height)/8))

        self.page_bg = self.image_resize(rel_path + "/files/page_bg.png", adaptive_width, adaptive_height )
        self.content_box = self.image_resize(rel_path + "/files/content_box.png", int(int(adaptive_width)*(4/5)), int(int(adaptive_height)*(4/5)))


        self.home_c1 = "files/home/home_c1.png"
        self.home_c2 = "files/home/home_c2.png"
        self.home_c3 = "files/home/home_c3.png"

        self.exp_c1 = "files/explore/exp_c1.png"
        self.exp_c2 = "files/explore/exp_c2.png"
        self.exp_c3 = "files/explore/exp_c3.png"

        self.ach_c1 = "files/achieve/ach_1.png"
        self.ach_c2 = "files/achieve/ach_2.png"
        self.ach_c3 = "files/achieve/ach_3.png"
        
        self.more_1 = "files/more/more_1.png"
        self.more_2 = "files/more/more_2.png"
        self.more_3 = "files/more/more_3.png"

        self.map_1 = "files/map/map_1.png"
        self.map_2 = "files/map/map_2.png"

        self.con_1 = "files/contact/con_1.png"
        self.con_2 = "files/contact/con_2.png"
        self.con_3 = "files/contact/con_3.png"
        self.con_4 = "files/contact/con_4.png"
        self.con_5 = "files/contact/con_5.png"


        self.app_bg = tk.Label(self, image=self.welcome_bg_image, bg="black", highlightthickness=0, borderwidth=0)
        self.app_bg.place(relx=0.5, rely=0.5, anchor="center")

        tk.Button(self, image=self.main_b1_image, bg="black", highlightthickness=0, borderwidth=0,
                  activebackground="#0B0B0B", command=  partial(self.call, "home")).place(relx= 0.2, rely=0.8)
        tk.Button(self, image=self.main_b2_image, bg="black", highlightthickness=0, borderwidth=0,
                  activebackground="#0B0B0B", command= partial(self.call, "explore" )).place(relx= 0.3, rely=0.8)
        tk.Button(self, image=self.main_b3_image, bg="black", highlightthickness=0, borderwidth=0,
                  activebackground="#0B0B0B", command= partial(self.call, "contact")).place(relx= 0.4, rely=0.8)
        tk.Button(self, image=self.main_b4_image, bg="black", highlightthickness=0, borderwidth=0,
                  activebackground="#0B0B0B", command= partial(self.call, "map" )).place(relx= 0.5, rely=0.8)
        tk.Button(self, image=self.main_b5_image, bg="black", highlightthickness=0, borderwidth=0,
                  activebackground="#0B0B0B", command= partial(self.call, "achieve" )).place(relx= 0.6, rely=0.8)
        tk.Button(self, image=self.main_b6_image, bg="black", highlightthickness=0, borderwidth=0,
                  activebackground="#0B0B0B", command= partial(self.call, "more" )).place(relx= 0.7, rely=0.8)
        
        # Text on Welcome screen
        g = open("data.txt", "r")
        content = g.readlines()
        title_text = content[1].strip()
        greeting_text = (content[2].strip()) +" " + ((content[4].strip()).capitalize())
        time_specifier = content[3].strip()
        print(title_text)
        print(greeting_text)
        print(time_specifier)

        L1 = tk.Label(self, text= title_text , font=("Times", int(screen_height/20)), bg="#0B0B0B", fg="white")
        L1.place(relx= 0.5, rely= 0.11, anchor= "center")

        L2 = tk.Label(self, text= greeting_text , font=("Calibri", int(screen_height/10)), bg="black", fg="white")
        L2.place(relx= 0.5, rely= 0.48, anchor= "center")

        L3 = tk.Label(self, text= time_specifier , font=("calibri", int(screen_height/20)), bg="black", fg="white")
        L3.place(relx= 0.5, rely= 0.6, anchor= "center")


        #clock
        clock_canvas = tk.Canvas(self, background="black", width=100, height=50, bd=0, borderwidth=0, highlightthickness=0)
        clock_canvas.place(x=55, y=45)

        def one23():
            time_box(clock_canvas)
        from clock_tk import time_box
        clock_thread = threading.Thread(target= one23)
        clock_thread.daemon = True
        clock_thread.start()

    
    def call(self, page):
 
        self.page_label = tk.Label(self, image= self.page_bg, border=0, highlightthickness= 0)
        self.page_label.place(x=0, y=0)

        self.content_label = tk.Label(self.page_label, image= self.content_box, border=0, highlightthickness= 0)
        self.content_label.place(relx= 0.5, rely= 0.525, anchor= "center")

        def exit_main_page():
            print("Returned to Main welocme page")
            self.page_label.place_forget()
            self.main_exit.place_forget()

        if page == "home":
            self.button_call(page, "Home", self.home_c1, self.home_c2, self.home_c3, 
                        "Centre", "Courses", "Refer & Earn", "4.4", "2.2", "0.2", "0.5", "0.8", "0.45", "0.45", "0.45")

        if page == "explore":
            self.webview_call(page, "Explore", self.exp_c1, self.exp_c2, self.exp_c3, 
                        "Student Login", "Documents", "Creators", "4.4", "2.2", "0.2", "0.5", "0.8", "0.45", "0.45", "0.45")
            
        if page == "contact":
            print("Redirected to : Contacts")
            self.re_con_1 = self.image_resize(self.con_1, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))
            self.re_con_2 = self.image_resize(self.con_2, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))
            self.re_con_3 = self.image_resize(self.con_3, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))
            self.re_con_4 = self.image_resize(self.con_4, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))
            self.re_con_5 = self.image_resize(self.con_5, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))

            self.show_con = tk.Label(self.content_label, image= self.re_con_1)
            self.show_con.place(relx= 0.5, rely= 0.45, anchor= "center")

            def set_page(cmd_1, cmd_2):
                self.show_con.place_forget()
                self.show_con.place(relx= 0.5, rely= 0.45, anchor= "center")
                tk.Button(self.content_label, text="⟫", command= cmd_1).place(relx= 0.9, rely= 0.45, anchor= "center")
                tk.Button(self.content_label, text="⟪", command= cmd_2).place(relx= 0.1, rely= 0.45, anchor= "center")
                footer = tk.Label(self.content_label, text= "Contacts", font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
                footer.place(relx=0.14, rely=0.92, anchor= "center")
                
            def show_con_2():
                self.show_con.config(image= self.re_con_2)
                set_page(show_con_3, show_con_1)
            def show_con_1():
                self.show_con.config(image= self.re_con_1)
                set_page(show_con_2, show_con_5)
            def show_con_3():
                self.show_con.config(image= self.re_con_3)
                set_page(show_con_4, show_con_2)
            def show_con_4():
                self.show_con.config(image= self.re_con_4)
                set_page(show_con_5, show_con_3)
            def show_con_5():
                self.show_con.config(image= self.re_con_5)
                set_page(show_con_1, show_con_4)

            set_page(show_con_2, show_con_3)

    
            
            self.main_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
            self.main_exit.place(relx= 0.9, rely= 0.9, anchor= "center")
            
        if page == "map":
            print("Redirected to : Maps")
            self.re_map_1 = self.image_resize(self.map_1, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))
            self.re_map_2 = self.image_resize(self.map_2, int(int(adaptive_width)/1.8), int(int(adaptive_height)/1.8))
            
            footer = tk.Label(self.content_label, text= "Maps", font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
            footer.place(relx=0.14, rely=0.92, anchor= "center")

            show_map = tk.Label(self.content_label, image= self.re_map_1)
            show_map.place(relx= 0.5, rely= 0.45, anchor= "center")

            def show_map_1():
                show_map.config(image= self.re_map_1)
                print("Maps - First Floor")
            def show_map_2():
                show_map.config(image= self.re_map_2)
                print("Maps - Second Floor")

            tk.Button(self.content_label, text="⟪", command= show_map_1).place(relx= 0.1, rely= 0.45, anchor= "center")
            tk.Button(self.content_label, text="⟫", command= show_map_2).place(relx= 0.9, rely= 0.45, anchor= "center")

            main_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
            main_exit.place(relx= 0.9, rely= 0.9, anchor= "center")
            
        if page == "achieve":
            self.button_call(page, "Achievements", self.ach_c1, self.ach_c2, self.ach_c3, 
                        "Roll of honour", "Placements", "Certificates", "4.4", "2.2", "0.2", "0.5", "0.8", "0.45", "0.45", "0.45")

        if page == "more":
            self.button_call(page, "More", self.more_1, self.more_2, self.more_3, 
                        "Servo Syncing", "Advanced  Settings", "Exit from Mainloop", "2", "6", "0.4", "0.4", "0.4", "0.2", "0.45", "0.7")

    
    ##
    def button_call(self, page, text, C1, C2, C3, FL_1, FL_2, FL_3, W, H, x1, x2, x3, y1, y2, y3):
        print("Redirected to : "+ text)
        footer = tk.Label(self.content_label, text= text, font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
        footer.place(relx=0.14, rely=0.92, anchor= "center")

        self.re_C1 = self.image_resize(C1, int(int(adaptive_width)/float(W)), int(int(adaptive_height)/float(H)))
        self.re_C2 = self.image_resize(C2, int(int(adaptive_width)/float(W)), int(int(adaptive_height)/float(H)))
        self.re_C3 = self.image_resize(C3, int(int(adaptive_width)/float(W)), int(int(adaptive_height)/float(H)))

        def exit_main_page():
            print("Returned to Main welocme page")
            self.page_label.place_forget()
            self.main_exit.place_forget()

        def exit_sub_page():
            content_sub_label.place_forget()
            sub_footer_label.pack_forget()
            sub_exit.place_forget()

        def container(footer_label, page_identifier):
            global content_sub_label, sub_exit, sub_footer_label
            content_sub_label = tk.Label(self.page_label, image= self.content_box, border=0, highlightthickness= 0)
            content_sub_label.place(relx= 0.5, rely= 0.53, anchor= "center")
            sub_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0
                                , highlightthickness=0, activebackground="black", command= exit_sub_page)
            sub_exit.place(relx= 0.9, rely= 0.9, anchor= "center")
            sub_footer_label = tk.Label(content_sub_label, text= footer_label, font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
            sub_footer_label.place(relx=0.14, rely=0.92, anchor= "center")

            def show_qr(link, gallery):
                qr_canvas = tk.Canvas(content_sub_label, bg="#0b0b0b", highlightthickness=0, bd=0, width= int(int(adaptive_width)/5), height= int(int(adaptive_height)/2))
                qr_canvas.place(relx= 0.8, rely= 0.45, anchor= "center")
                qr_label = tk.Label(qr_canvas, image= "")
                qr_label.place(relx=0.5, anchor= "n")
                qr.create(link, qr_label, 160)

                pic_label = tk.Frame(content_sub_label, highlightthickness=0, bd=0, width= int(int(adaptive_height) - int(int(adaptive_width)/5)), height= int(int(adaptive_height)/2))
                pic_label.place(relx= 0.35, rely= 0.45, anchor= "center")
                
                sliding_images = SlidingImages(pic_label, image_width= int(int(adaptive_height) - int(int(adaptive_width)/5)),
                                               image_height= int(int(adaptive_height)/2))
                image_paths =  [rel_path+"/new_files/"+gallery+"/a1.png",
                                rel_path+"/new_files/"+gallery+"/a2.png",
                                rel_path+"/new_files/"+gallery+"/a3.png",
                               ]
                sliding_images.set_images(image_paths)

                sliding_images.place(x=0, y=0)


                quote = tk.Label(qr_canvas, text="Scan this QR code for more", fg="white", bg="#0b0b0b", font=("calibri", 13), wraplength= 100)
                quote.place(relx= 0.45, rely= 0.8, anchor= "center")

            def get_link(index):
                g = open("data.txt", "r")
                content = g.readlines()
                title_text = content[index-1].strip()
                return title_text


            if page == "home":
                print("you are accessing home : "+ page_identifier)
                now_in_home = "h"+page_identifier

                if now_in_home == "hB1":
                    print("Displaying Centre Details")
                    show_qr(get_link(6), "home/centre")
                if now_in_home == "hB2":
                    print("Displaying Course Details")
                    show_qr(get_link(7), "home/course")
                if now_in_home == "hB3":
                    print("Displaying Refer & Earn Details")
                    show_qr(get_link(8), "home/refer")

        
            # if page == "explore":
            # Explore page is called within webview_call function (not from button_call() anymore. )
            

            if page == "achieve":
                print("you are accessing achievemts : "+ page_identifier)
                now_in_achieve = "a"+page_identifier

                if now_in_achieve == "aB1":
                    print("Displaying Roll of Honour Details")
                    show_qr(get_link(9), "achieve/roll")
                if now_in_achieve == "aB2":
                    print("Displaying Placement Details")
                    show_qr(get_link(10), "achieve/placement")
                if now_in_achieve == "aB3":
                    print("Displaying Certificate Details")
                    show_qr(get_link(11), "achieve/certificate")

            
            if page == "more":
                print("you are accessing more page : "+ page_identifier)
                now_in_more = "m"+page_identifier
                if now_in_more == "mB3":
                    print("you are trying to destroy the application running")
                    # showinfow, showwarning, showerror, askquestion, askokcancel, askyesno
                    def popup_1():
                        response = messagebox.askyesno("Exit Mainloop" ,"Application currently running will be closed ! \nDo you want to continue ?")
                        if response == 1:
                            self.close_application()
                    popup_1()
                if now_in_more == "mB2":
                    print("you are trying to EDIT the application !")
                    def popup_2():
                        response = messagebox.askyesno("Edit Application" ,"You should Restart the Application after editing ! \nDo you want to continue ?")
                        if response == 1:
                            edit_app_.settings()
                    popup_2()
                if now_in_more == "mB1":
                    print("Let's Setup the servo motors !")
                    def popup_2():
                        response = messagebox.askyesno("Servo Setup" ,"Let's Setup the servo motors ! \nDo you want to continue ?")
                        if response == 1:

                            pass
                            
                    popup_2()
    

        tk.Button(self.content_label, image= self.re_C1, border=0, highlightthickness=0, command= partial(container, FL_1, "B1"), activebackground="#0B0B0B").place(relx= x1, rely= y1, anchor= "center")
        tk.Button(self.content_label, image= self.re_C2, border=0, highlightthickness=0, command= partial(container, FL_2, "B2"), activebackground="#0B0B0B").place(relx= x2, rely= y2, anchor= "center")
        tk.Button(self.content_label, image= self.re_C3, border=0, highlightthickness=0, command= partial(container, FL_3, "B3"), activebackground="#0B0B0B").place(relx= x3, rely= y3, anchor= "center")


        self.main_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
        self.main_exit.place(relx= 0.9, rely= 0.9, anchor= "center")


    def webview_call(self, page, text, C1, C2, C3, FL_1, FL_2, FL_3, W, H, x1, x2, x3, y1, y2, y3):
        print("Redirected to : "+ text)
        footer = tk.Label(self.content_label, text= text, font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
        footer.place(relx=0.14, rely=0.92, anchor= "center")

        self.re_C1 = self.image_resize(C1, int(int(adaptive_width)/float(W)), int(int(adaptive_height)/float(H)))
        self.re_C2 = self.image_resize(C2, int(int(adaptive_width)/float(W)), int(int(adaptive_height)/float(H)))
        self.re_C3 = self.image_resize(C3, int(int(adaptive_width)/float(W)), int(int(adaptive_height)/float(H)))

        tk.Button(self.content_label, image= self.re_C1, border=0, highlightthickness=0, command= partial(self.web_container, page, FL_1, "B1"), activebackground="#0B0B0B").place(relx= x1, rely= y1, anchor= "center")
        tk.Button(self.content_label, image= self.re_C2, border=0, highlightthickness=0, command= partial(self.web_container, page, FL_2, "B2"), activebackground="#0B0B0B").place(relx= x2, rely= y2, anchor= "center")
        tk.Button(self.content_label, image= self.re_C3, border=0, highlightthickness=0, command= partial(self.web_container, page, FL_3, "B3"), activebackground="#0B0B0B").place(relx= x3, rely= y3, anchor= "center")


        self.main_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0, highlightthickness=0, activebackground="black", command= self.web_exit_main_page)
        self.main_exit.place(relx= 0.9, rely= 0.9, anchor= "center")

        self.web_view = None
        

    def web_exit_main_page(self):
        print("Returned to Main welocme page")
        self.page_label.place_forget()
        self.main_exit.place_forget()

    def web_exit_sub_page(self):
        self.content_sub_label.place_forget()
        self.sub_footer_label.pack_forget()
        self.sub_exit.place_forget()

    def web_container(self, page, footer_label, page_identifier):
        global content_sub_label, sub_exit, sub_footer_label

        self.content_sub_label = tk.Label(self.page_label, image= self.content_box, border=0, highlightthickness= 0)
        self.content_sub_label.place(relx= 0.5, rely= 0.53, anchor= "center")
        self.sub_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0
                                , highlightthickness=0, activebackground="black", command= self.web_exit_sub_page)
        self.sub_exit.place(relx= 0.9, rely= 0.9, anchor= "center")
        self.sub_footer_label = tk.Label(self.content_sub_label, text= footer_label, font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
        self.sub_footer_label.place(relx=0.14, rely=0.92, anchor= "center")

        if page == "explore":
            print("you are accessing explore : "+ page_identifier)
            now_in_explore = "e"+page_identifier

            if now_in_explore == "eB1":
                print("Displaying Student Login Page")
                self.open_web_view( "https://erp.nttftrg.com/")                  

            if now_in_explore == "eB2":
                print("Displaying Project Documents")
                self.open_web_view( "https://sites.google.com/view/echo-robot/documentation")

            if now_in_explore == "eB3":
                print("Displaying About Creators")
                self.open_web_view( "https://sites.google.com/view/echo-robot/the-creators")

    def open_web_view(self, open_url):
        if not self.web_view:
            self.web_view = WebView(open_url)
            

    # X #
    def close_application(self):
        # closes the entire tkinter application
        self.master.destroy()    



    def image_resize(self, image_path, width, height):
        try:
            raw = Image.open( image_path)
            resized = raw.resize((width, height), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(resized)
        except Exception as e:
            print("error resizing image: {e}")
            return None


class WebView(tk.Toplevel):
    def __init__(self, url):
        super().__init__()
    
        #self.geometry(str(screen_width)+"x"+str(screen_height))
        self.configure(bg="black")
        self.geometry("100x100")

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.web_view = tk.Label(self, text= "web view")
        self.web_view.pack(fill= "both", expand= True)

        self.open_webpage(url)

    def open_webpage(self, url):
        webbrowser.open(url)   

    def on_close(self):
        self.destroy() 


def set_screen_size(width, height):
    global bt_size, adaptive_width, adaptive_height
    button_size = int(width)+int(height)
    bt_size = int(button_size/20)
    adaptive_width = width
    adaptive_height = height
    

    print(bt_size)
    print("bt size is collected successfully")

        


# old version of code

"""

"""
