# Building  a structure fior this app
from functools import partial
from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
from random import randint


##

def resizer(path, w_value, h_value):
    global final
    img = path
    raw = Image.open(img)
    #OPEN and RESIZE image
    resized = raw.resize(((int(h_value)), (int(w_value))), Image.Resampling.LANCZOS)
    final = ImageTk.PhotoImage(resized)
    #return final

def file():
    global abs_path, real_bg, thum_bg, thumb_label
    abs_path = filedialog.askopenfilename(initialdir="/new_files", title="select a file",
                                                filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg")))
    print("you have selected : " + abs_path)
    
    real_bg = resizer(abs_path, 500, 800)
    thum_bg = resizer(abs_path, 100, 150)

    thumb_label.config(image= thum_bg)

img_key = 1

def saved(path):
    global img_key
    image = Image.open(abs_path)
    
    image.save("new_files/"+path+"/a"+str(img_key)+".png")
    print("image file "+str(img_key)+" is saved")
    #print (str(count)+"th picture is added")
    if int(img_key) < 3 :
        img_key = img_key + 1
        choose_button.config(text= "choose Image file : "+ str(img_key))
        thumb_label.config(image="")

    else :
        img_key = 1

##

def settings():
    edit = Tk()
    edit.title("Advanced Settings >>")
    edit.geometry("500x300")
    edit.resizable(False, False)

    def hide_frames():
        # Loop through all childrens in frames and destroy
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        main_frame.pack_forget()
    app_menu = Menu(edit)
    edit.config(menu=app_menu, pady= 10)

    #create menu
    welcome_menu = Menu(app_menu)
    home_menu = Menu(app_menu)
    explore_menu = Menu(app_menu)
    achievements_menu = Menu(app_menu)
    about_menu = Menu(app_menu)

    app_menu.add_cascade(label="Welcome", menu= welcome_menu, columnbreak= 0)
    app_menu.add_cascade(label="Home", menu= home_menu, columnbreak= 0)
    app_menu.add_cascade(label="Explore", menu= explore_menu, columnbreak= 0)
    app_menu.add_cascade(label="Achievements", menu= achievements_menu, columnbreak= 0)
    app_menu.add_cascade(label="About", menu= about_menu, columnbreak= 0)

    def settings_page(Title_Text):
        hide_frames()
        global thumb_label, choose_button
        main_frame.place(x=0, y=0)
        Label(main_frame, text= "Edit "+Title_Text, font=("Calibri, 18")).place(x=20, y=40)
        Label(main_frame, text= "Enter the "+ Title_Text +" you wanted to Display >>").place(x=20, y=80)
        T1 = Text(main_frame, height= 2, width= 35,)
        T1.place(x=20, y=120)
        thumb_label = Label(main_frame, image="", height= 80, width= 120)
        thumb_label.place(x=350, y= 30)
        
        Label(main_frame, text= "(*changes made here will reflect in the main program.)", fg="red").place(x=20, y=160)
        Label(main_frame, text= "(*png files // 680x500 pix is recommended.)", fg="green").place(x=20, y=180)

        def reset_it(dir):
        
            for i in range (1,4):
                source = "files/"+dir+"/a"+str(i)+".png"
                dest = "new_files/"+dir+"/a"+str(i)+".png"
                current = Image.open(source)
                current.save(dest)
            print("Images in >> "+ dir + " >> is replaced with the default resource")

        def write_it(index, content):
            f = open("data.txt", "r")
            data = f.readlines()
            data[int(index)] = content+"\n"
            f =  open("data.txt", "w")
            f.writelines(data)

        if Title_Text == "Title Name" :
            T1.insert('end',"ECHO")
            def apply():
                global  Title
                Title = T1.get("1.0", 'end-1c')
                write_it("1", Title)
                print("Applied : "+Title)
            apply_button = Button(main_frame, text="Apply", command= apply)
            apply_button.place(x=20, y=220)

        if Title_Text == "Greeting Text" :
            T1.insert('end',"Hello")
            def apply():
                global Greeting
                Greeting = T1.get("1.0", 'end-1c')
                write_it("2", Greeting)
                print("Applied : "+Greeting)
            apply_button = Button(main_frame, text="Apply", command= apply)
            apply_button.place(x=20, y=220)

        def edit_config(Title_Text, line_index, dir):
            global apply_button, reset_button, choose_button, save_button
            def apply():
                global  roll
                roll = T1.get("1.0", 'end-1c')
                write_it(line_index, roll)
                print("Applied : "+ Title_Text)
                    
            apply_button = Button(main_frame, text="Apply", command= apply)
            apply_button.place(x=20, y=220)
            reset_button = Button(main_frame, text="Reset to default", command= partial(reset_it, dir))
            reset_button.place(x=80, y=220)
            choose_button = Button(main_frame, text="choose Image file : 1", command= file)
            choose_button.place(x=350, y=120)
            save_button = Button(main_frame, text="Save Image", fg="green", command= partial(saved, dir)).place(x=350, y=155)

        global NTTF
        NTTF = "https://sites.google.com/view/echo-robot/in-centre"
        if Title_Text == "Web Link for Centre" :
            T1.insert('end',NTTF)
            edit_config(Title_Text, "5", "home/centre", )

        global COURSES
        COURSES = "https://sites.google.com/view/echo-robot/in-courses"
        if Title_Text == "Course Details" :
            T1.insert('end',COURSES)
            edit_config(Title_Text, "6", "home/course", )
            
        global REFER
        REFER = "https://sites.google.com/view/echo-robot/in-refernearn"
        if Title_Text == "Refer & Earn Details" :
            T1.insert('end',REFER)
            edit_config(Title_Text, "7", "home/refer", )

        global ROLL
        ROLL = "  update the link  "
        if Title_Text == "Roll of honour Details" :
            T1.insert('end',ROLL)
            edit_config(Title_Text, "8", "achieve/roll", )

        global PLACEMENT
        PLACEMENT = "  update the link  "
        if Title_Text == "Placement Details" :
            T1.insert('end',PLACEMENT)
            edit_config(Title_Text, "9", "achieve/placements", )
        
        global CERTIFICATE
        CERTIFICATE = "  update the link  "
        if Title_Text == "Certificates Details" :
            T1.insert('end',CERTIFICATE)
            edit_config(Title_Text, "10", "achieve/certificate", )

        



    #welcome
    welcome_menu.add_command(label="Title text", command= partial(settings_page, "Title Name"))
    welcome_menu.add_command(label="Greeting text", command= partial(settings_page, "Greeting Text"))

    #home
    home_menu.add_command(label="Centre Details", command= partial(settings_page, "Web Link for Centre"))
    home_menu.add_command(label="Course Details", command= partial(settings_page, "Course Details"))
    home_menu.add_command(label="Refer & Earn", command= partial(settings_page, "Refer & Earn Details"))

    #achieve
    achievements_menu.add_command(label="Roll of honour", command= partial(settings_page, "Roll of honour Details"))
    achievements_menu.add_command(label="Placement", command= partial(settings_page, "Placement Details"))
    achievements_menu.add_command(label="Certificates", command= partial(settings_page, "Certificates Details"))

    # create frames
    main_frame = Frame(edit, width=500, height=500)

    edit.mainloop()

##
#settings()