
    def webview_call(self, page, text, C1, C2, C3, FL_1, FL_2, FL_3, W, H, x1, x2, x3, y1, y2, y3):
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

        def web_container(footer_label, page_identifier):
            global content_sub_label, sub_exit, sub_footer_label
            content_sub_label = tk.Label(self.page_label, image= self.content_box, border=0, highlightthickness= 0)
            content_sub_label.place(relx= 0.5, rely= 0.53, anchor= "center")
            sub_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0
                                , highlightthickness=0, activebackground="black", command= exit_sub_page)
            sub_exit.place(relx= 0.9, rely= 0.9, anchor= "center")
            sub_footer_label = tk.Label(content_sub_label, text= footer_label, font=("calibri", int(int(adaptive_height)/35), "italic"), bg="black", fg="white")
            sub_footer_label.place(relx=0.14, rely=0.92, anchor= "center")

            if page == "explore":
                print("you are accessing explore : "+ page_identifier)
                now_in_explore = "e"+page_identifier

                if now_in_explore == "eB1":
                    print("Displaying Student Login Page")

                if now_in_explore == "eB1":
                    print("Displaying Project Documents")

                if now_in_explore == "eB1":
                    print("Displaying About Creators")

            
        tk.Button(self.content_label, image= self.re_C1, border=0, highlightthickness=0, command= partial(web_container, FL_1, "B1"), activebackground="#0B0B0B").place(relx= x1, rely= y1, anchor= "center")
        tk.Button(self.content_label, image= self.re_C2, border=0, highlightthickness=0, command= partial(web_container, FL_2, "B2"), activebackground="#0B0B0B").place(relx= x2, rely= y2, anchor= "center")
        tk.Button(self.content_label, image= self.re_C3, border=0, highlightthickness=0, command= partial(web_container, FL_3, "B3"), activebackground="#0B0B0B").place(relx= x3, rely= y3, anchor= "center")


        self.main_exit = tk.Button(self.page_label, image= self.exit_b_image, border=0, highlightthickness=0, activebackground="black", command= exit_main_page)
        self.main_exit.place(relx= 0.9, rely= 0.9, anchor= "center")