
import tkinter as tk
import time
from PIL import ImageTk,Image
from threading import *
from tkinter import messagebox
from functools import partial
import edit_app_
import qr
import speech_n_tts
import echo_servo

m_key = "roger"
# updated code

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="black")

        print(" This snippet is running from application.py > working fine.")

"""
# old version of code

def bg_resizer(raw, w_value, h_value):
    global final     
    file = ImageTk.getimage(raw)
    resized = file.resize(((int(w_value)), (int(h_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    return final


def app(win, w_value, h_value):                      # call this later # call from speech R after collecting name

    #Resources
    welcome_bg = PhotoImage(file = f"files/background.png")
    page_bg = PhotoImage(file = f"files/page_bg.png")

    main_b1 = PhotoImage(file = f"files/img0.png")
    main_b2 = PhotoImage(file = f"files/img1.png")
    main_b3 = PhotoImage(file = f"files/img2.png")
    main_b4 = PhotoImage(file = f"files/img3.png")
    main_b5 = PhotoImage(file = f"files/img4.png")
    main_b6 = PhotoImage(file = f"files/img5.png")
    exit_b = PhotoImage(file = f"files/exit_b0.png")

    content_box = PhotoImage(file = f"files/content_box.png")

    home_c1 = PhotoImage(file = f"files/home/home_c1.png")
    home_c2 = PhotoImage(file = f"files/home/home_c2.png")
    home_c3 = PhotoImage(file = f"files/home/home_c3.png")

    ach_c1 = PhotoImage(file = f"files/achieve/ach_1.png")
    ach_c2 = PhotoImage(file = f"files/achieve/ach_2.png")
    ach_c3 = PhotoImage(file = f"files/achieve/ach_3.png")

    exp_c1 = PhotoImage(file = f"files/explore/exp_c1.png")
    exp_c2 = PhotoImage(file = f"files/explore/exp_c2.png")
    exp_c3 = PhotoImage(file = f"files/explore/exp_c3.png")

    more_1 = PhotoImage(file = f"files/more/more_1.png")
    more_2 = PhotoImage(file = f"files/more/more_2.png")
    more_3 = PhotoImage(file = f"files/more/more_3.png")

    map_1 = PhotoImage(file = f"files/map/map_1.png")
    map_2 = PhotoImage(file = f"files/map/map_2.png")

    con_1 = PhotoImage(file = f"files/contact/con_1.png")
    con_2 = PhotoImage(file = f"files/contact/con_2.png")
    con_3 = PhotoImage(file = f"files/contact/con_3.png")
    con_4 = PhotoImage(file = f"files/contact/con_4.png")
    con_5 = PhotoImage(file = f"files/contact/con_5.png")


    global resized_welcome_bg, resized_page_bg, re_main_b1, re_main_b2, re_main_b3, re_main_b4, re_main_b5, re_main_b5, re_main_b6
    
    print("importing app here")
    C1 = Canvas(win, background="red", width= w_value, height= h_value, highlightthickness= 0)
    C1.place(x=0, y=0)
    #Label(C1, text="Code design & Developed by @Anupam_dex").place(x=0, y=0)

    resized_welcome_bg = bg_resizer(welcome_bg, w_value, h_value)
    C1.create_image(0,0, anchor= NW, image= resized_welcome_bg)
    
    g = open("data.txt", "r")
    content = g.readlines()
    title_text = content[1].strip()
    greet_text = (content[2].strip()) +" " + (content[4].strip())
    time_specifier = content[3].strip()
    print(title_text)
    print(greet_text)

    L1 = Label(C1, text= title_text , font=("Times", int(int(h_value)/20)), bg="#0B0B0B", fg="white")
    L1.place(relx= 0.5, rely= 0.11, anchor= CENTER)

    L2 = Label(C1, text= greet_text , font=("Calibri", int(int(h_value)/10)), bg="black", fg="white")
    L2.place(relx= 0.5, rely= 0.48, anchor= CENTER)

    L3 = Label(C1, text= time_specifier , font=("calibri", int(int(h_value)/20)), bg="black", fg="white")
    L3.place(relx= 0.5, rely= 0.6, anchor= CENTER)

    #clock
    clock_canvas = Canvas(C1, background="black", width=100, height=50, bd=0, borderwidth=0, highlightthickness=0)
    clock_canvas.place(x=55, y=45)

    def one23():
        time_box(clock_canvas)
    from clock_tk import time_box
    clock_thread = Thread(target= one23)
    clock_thread.start()

    ##
    def button_call(page, text, C1, C2, C3, FL_1, FL_2, FL_3, W, H, x1, x2, x3, y1, y2, y3):
        global re_C1, re_C2, re_C3
        print("Redirected to : "+ text)
        footer = Label(content_label, text= text, font=("calibri", int(int(h_value)/35), "italic"), bg="black", fg="white")
        footer.place(relx=0.14, rely=0.92, anchor= CENTER)

        re_C1 = bg_resizer(C1, int(int(w_value)/float(W)), int(int(h_value)/float(H)))
        re_C2 = bg_resizer(C2, int(int(w_value)/float(W)), int(int(h_value)/float(H)))
        re_C3 = bg_resizer(C3, int(int(w_value)/float(W)), int(int(h_value)/float(H)))

        def exit_sub_page():
            content_sub_label.place_forget()
            sub_footer_label.pack_forget()
            sub_exit.place_forget()

        def container(footer_label, page_identifier):
            global content_sub_label, sub_exit, sub_footer_label
            #Label(content_label, width= 800, height= 500).place(x=0, y=0)
            content_sub_label = Label(page_label, image= re_content_box, border=0, highlightthickness= 0)
            content_sub_label.place(relx= 0.5, rely= 0.5, anchor= CENTER)
            sub_exit = Button(page_label, image= e_b, border=0
                                , highlightthickness=0, activebackground="black", command= exit_sub_page)
            sub_exit.place(relx= 0.9, rely= 0.85, anchor= CENTER)
            sub_footer_label = Label(content_sub_label, text= footer_label, font=("calibri", int(int(h_value)/35), "italic"), bg="black", fg="white")
            sub_footer_label.place(relx=0.14, rely=0.92, anchor= CENTER)

            def show_qr(link, gallery):
                qr_canvas = Canvas(content_sub_label, bg="#0b0b0b", highlightthickness=0, bd=0, width= int(int(w_value)/5), height= int(int(h_value)/2))
                qr_canvas.place(relx= 0.8, rely= 0.45, anchor= CENTER)
                qr_label = Label(qr_canvas, image= "")
                qr_label.place(relx=0.5, anchor= "n")
                qr.create(link, qr_label, 160)

                pic_label = Label(content_sub_label, highlightthickness=0, bd=0, width= int(int(h_value) - int(int(w_value)/5)), height= int(int(h_value)/2))
                pic_label.place(relx= 0.35, rely= 0.45, anchor= CENTER)
                    
                path = "new_files/"+gallery+"/"
                image_files = [path+'a1.png',path+'a2.png',path+'a3.png']  # Replace with your image filenames

                #slideshow = ImageSlideshow(image_files, pic_label, int(int(h_value) - int(int(w_value)/5)), int(int(h_value)/2))

                quote = Label(qr_canvas, text="Scan this QR code for more", fg="white", bg="#0b0b0b", font=("calibri", 13), wraplength= 100)
                quote.place(relx= 0.45, rely= 0.8, anchor= CENTER)

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
                    show_qr(get_link(5), "home/centre")
                if now_in_home == "hB2":
                    print("Displaying Course Details")
                    show_qr(get_link(6), "home/course")
                if now_in_home == "hB3":
                    print("Displaying Refer & Earn Details")
                    show_qr(get_link(7), "home/refer")

            if page == "achieve":
                print("you are accessing achievemts : "+ page_identifier)
                now_in_achieve = "a"+page_identifier

                if now_in_achieve == "aB1":
                    print("Displaying Roll of Honour Details")
                    show_qr(get_link(8), "achieve/roll")
                if now_in_achieve == "aB2":
                    print("Displaying Placement Details")
                    show_qr(get_link(9), "achieve/placement")
                if now_in_achieve == "aB3":
                    print("Displaying Certificate Details")
                    show_qr(get_link(10), "achieve/certificate")

            if page == "explore":
                print("you are accessing explore : "+ page_identifier)
                now_in_explore = "e"+page_identifier

                if now_in_explore == "aB1":
                    print("Displaying Student Login Page")


                
###
            if page == "more":
                print("you are accessing more page : "+ page_identifier)
                now_in_more = "m"+page_identifier
                if now_in_more == "mB3":
                    print("you are trying to destroy the application running")
                    # showinfow, showwarning, showerror, askquestion, askokcancel, askyesno
                    def popup_1():
                        response = messagebox.askyesno("Exit Mainloop" ,"Application currently running will be closed ! \nDo you want to continue ?")
                        if response == 1:
                            win.quit()
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

        Button(content_label, image= re_C1, border=0, highlightthickness=0, command= partial(container, FL_1, "B1"), activebackground="#0B0B0B").place(relx= x1, rely= y1, anchor= CENTER)
        Button(content_label, image= re_C2, border=0, highlightthickness=0, command= partial(container, FL_2, "B2"), activebackground="#0B0B0B").place(relx= x2, rely= y2, anchor= CENTER)
        Button(content_label, image= re_C3, border=0, highlightthickness=0, command= partial(container, FL_3, "B3"), activebackground="#0B0B0B").place(relx= x3, rely= y3, anchor= CENTER)


    def call(page):
        global page_frame, page_label, resized_page_bg, re_content_box, content_label
        global re_map_1, re_map_2, re_con_1, re_con_2, re_con_3
 
        page_frame = Frame(C1, width= w_value, height= h_value)
        page_frame.place(x=0, y=0)
        
        resized_page_bg = bg_resizer(page_bg, w_value, h_value)
        page_label = Label(page_frame, image= resized_page_bg, border=0, highlightthickness= 0)
        page_label.place(x=0, y=0)

        re_content_box = bg_resizer(content_box, int(int(w_value)*(6/8)), int(int(h_value)*(4/5)))
        content_label = Label(page_label, image= re_content_box, border=0, highlightthickness= 0)
        content_label.place(relx= 0.5, rely= 0.5, anchor= CENTER)
        ##

        def exit_main_page():
            print("Returned to Main welocme page")
            page_frame.place_forget()
            page_label.place_forget()
            main_exit.place_forget()

        global e_b
        e_b = bg_resizer(exit_b, int(int(w_value)/8), int(int(h_value)/8))
        main_exit = Button(page_label, image= e_b, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
        main_exit.place(relx= 0.9, rely= 0.85, anchor= CENTER)

        if page == "home":
            button_call(page, "Home", home_c1, home_c2, home_c3, 
                        "Centre", "Courses", "Refer & Earn", "4.4", "2.2", "0.2", "0.5", "0.8", "0.45", "0.45", "0.45")

        if page == "explore":
            button_call(page, "Explore", exp_c1, exp_c2, exp_c3, 
                        "Student Login", "Documents", "Creators", "4.4", "2.2", "0.2", "0.5", "0.8", "0.45", "0.45", "0.45")
            
        if page == "contact":
            print("Redirected to : Contacts")
            re_con_1 = bg_resizer(con_1, int(int(w_value)/1.8), int(int(h_value)/1.8))
            re_con_2 = bg_resizer(con_2, int(int(w_value)/1.8), int(int(h_value)/1.8))
            re_con_3 = bg_resizer(con_3, int(int(w_value)/1.8), int(int(h_value)/1.8))
            re_con_4 = bg_resizer(con_4, int(int(w_value)/1.8), int(int(h_value)/1.8))
            re_con_5 = bg_resizer(con_5, int(int(w_value)/1.8), int(int(h_value)/1.8))

            show_con = Label(content_label, image= re_con_1)
            show_con.place(relx= 0.5, rely= 0.45, anchor= CENTER)

            def set_page(cmd_1, cmd_2):
                show_con.place_forget()
                show_con.place(relx= 0.5, rely= 0.45, anchor= CENTER)
                Button(content_label, text="⟫", command= cmd_1).place(relx= 0.9, rely= 0.45, anchor= CENTER)
                Button(content_label, text="⟪", command= cmd_2).place(relx= 0.1, rely= 0.45, anchor= CENTER)
                footer = Label(content_label, text= "Contacts", font=("calibri", int(int(h_value)/35), "italic"), bg="black", fg="white")
                footer.place(relx=0.14, rely=0.92, anchor= CENTER)
                
            def show_con_2():
                show_con.config(image= re_con_2)
                set_page(show_con_3, show_con_1)
            def show_con_1():
                show_con.config(image= re_con_1)
                set_page(show_con_2, show_con_5)
            def show_con_3():
                show_con.config(image= re_con_3)
                set_page(show_con_4, show_con_2)
            def show_con_4():
                show_con.config(image= re_con_4)
                set_page(show_con_5, show_con_3)
            def show_con_5():
                show_con.config(image= re_con_5)
                set_page(show_con_1, show_con_4)

            set_page(show_con_2, show_con_3)
            main_exit = Button(page_label, image= e_b, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
            main_exit.place(relx= 0.9, rely= 0.85, anchor= CENTER)

        if page == "map":
            print("Redirected to : Maps")
            re_map_1 = bg_resizer(map_1, int(int(w_value)/1.8), int(int(h_value)/1.8))
            re_map_2 = bg_resizer(map_2, int(int(w_value)/1.8), int(int(h_value)/1.8))
            
            footer = Label(content_label, text= "Maps", font=("calibri", int(int(h_value)/35), "italic"), bg="black", fg="white")
            footer.place(relx=0.14, rely=0.92, anchor= CENTER)

            show_map = Label(content_label, image= re_map_1)
            show_map.place(relx= 0.5, rely= 0.45, anchor= CENTER)

            def show_map_1():
                show_map.config(image= re_map_1)
                print("Maps - First Floor")
            def show_map_2():
                show_map.config(image= re_map_2)
                print("Maps - Second Floor")

            Button(content_label, text="⟪", command= show_map_1).place(relx= 0.1, rely= 0.45, anchor= CENTER)
            Button(content_label, text="⟫", command= show_map_2).place(relx= 0.9, rely= 0.45, anchor= CENTER)
            main_exit = Button(page_label, image= e_b, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
            main_exit.place(relx= 0.9, rely= 0.85, anchor= CENTER)


        if page == "achieve":
            button_call(page, "Achievements", ach_c1, ach_c2, ach_c3, 
                        "Roll of honour", "Placements", "Certificates", "4.4", "2.2", "0.2", "0.5", "0.8", "0.45", "0.45", "0.45")


        if page == "more":
            button_call(page, "More", more_1, more_2, more_3, 
                        "Servo Syncing", "Advanced  Settings", "Exit from Mainloop", "2", "6", "0.4", "0.4", "0.4", "0.2", "0.45", "0.7")


    button_size = int(w_value)+int(h_value)
    bt_s = int(button_size/20)

    re_main_b1 = bg_resizer(main_b1, bt_s, bt_s)
    re_main_b2 = bg_resizer(main_b2, bt_s, bt_s)
    re_main_b3 = bg_resizer(main_b3, bt_s, bt_s)
    re_main_b4 = bg_resizer(main_b4, bt_s, bt_s)
    re_main_b5 = bg_resizer(main_b5, bt_s, bt_s)
    re_main_b6 = bg_resizer(main_b6, bt_s, bt_s)

    Button(C1, image= re_main_b1, command= partial(call, "home" )
           , border=0, highlightthickness=0, activebackground="#0B0B0B").place(relx= 0.2, rely=0.8)
    Button(C1, image= re_main_b2, command= partial(call, "explore" )
           , border=0, highlightthickness=0, activebackground="#0B0B0B").place(relx= 0.3, rely=0.8)
    Button(C1, image= re_main_b3, command= partial(call, "contact" )
           , border=0, highlightthickness=0, activebackground="#0B0B0B").place(relx= 0.4, rely=0.8)
    Button(C1, image= re_main_b4, command= partial(call, "map" )
           , border=0, highlightthickness=0, activebackground="#0B0B0B").place(relx= 0.5, rely=0.8)
    Button(C1, image= re_main_b5, command= partial(call, "achieve" )
           , border=0, highlightthickness=0, activebackground="#0B0B0B").place(relx= 0.6, rely=0.8)
    Button(C1, image= re_main_b6, command= partial(call, "more" )
           , border=0, highlightthickness=0, activebackground="#0B0B0B").place(relx= 0.7, rely=0.8)
    


    win.mainloop()

def filler(winx, wx_value, hx_value):
    global distance, C1
    global w_value, h_value, win
    w_value = wx_value
    h_value = hx_value
    
    echo_logo = PhotoImage(file = f"files/echo_logo.png")

    C1 = Canvas(winx, background="black", width= wx_value, height= hx_value, highlightthickness= 0)
    C1.place(x=0, y=0)

    resized_welcome_bg = bg_resizer(echo_logo, int(int(wx_value)/1), int(int(hx_value)/3))
    C1.create_image(0,0, anchor= NW, image= resized_welcome_bg)

    distance_label = Label(C1, text= "The distance measured is ")
    distance_label.place(relx= 0.2, rely= 0.9, anchor= CENTER)

    def ultrasonic():
    
        print("ultrasonic running // TEST")          # TEST TEST TEST
        for i in range(0,60,10):
            time.sleep(1)
            print(i)
            distance = i
            distance_label.configure(text= "The distance measured is : "+ str(distance))
            if distance == 50:
                C1.place_forget()
                name_identifier(winx, w_value, h_value)


            else:
                pass

    '''
        #ultrasonic sensor program for raspberry pi
        prev_distance = 0
        printed_message = False
        def ultrasonic_condition():
            global prev_distance
            global printed_message
            
            distance = ultrasonic.run()
            if ( not printed_message and distance < 100) :
                printed_message = True
                print("The distance is less than 100")
                C1.place_forget()
                name_identifier(win, w_value, h_value)
                
            elif (prev_distance < 100 and distance > 100) :
                printed_message = False
                print("The distance is more than 100")

            prev_distance = distance
            return distance

        ultrasonic_condition()
    ''' 

    Thread(target= ultrasonic ).start()

def name_identifier(win, w_value, h_value):
    speech_n_tts.sr_window(win, w_value, h_value)


def main_frame():
    #Thread(target= echo_servo.start()).start()
    
    app(win, w_value, h_value)

"""