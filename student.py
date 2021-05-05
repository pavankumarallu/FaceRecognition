from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
 

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #Background image
        bg_img = Image.open(r"E:\FaceRecogniseSystem\images\bg.jpg")
        bg_img = bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(bg_img)
        bg = Label(self.root,image = self.photoimage)
        bg.place(x = 0,y = 0,width = 1530,height = 790)
        
        #title
        title_lbl = Label(bg,text = "Student Record",font = ("Comic Sans MS", 30, "bold"),bg = "#000000",fg = "white")
        title_lbl.place(x=0,y=0,width = 1530,height = 70)
       
       
        #main frame
         
        main_frame = Frame(bg,bd = 2,bg="#000")
        main_frame.place(x = 30, y = 90, width = 1470, height = 650)

        #-----------------------------------------------------------------left label frame-----------------------------------------------------------------------------------
        Left_frame = LabelFrame(main_frame,bd = 5,relief = RIDGE,text = "Student Details",font = ("Comic Sans MS", 12, "bold"),bg="#000",fg="#ffffff")
        Left_frame.place(x = 10,y = 10,width = 690,height = 600)
        
        # --------------------course current-----------------------------
        Left_label_Course = LabelFrame(Left_frame,bd = 2,relief = RIDGE,text = "Course details",font = ("Comic Sans MS", 12, "bold"),bg="#000",fg="#ffffff")
        Left_label_Course.place(x = 10,y = 15,width = 660,height = 150)
        
        #department
        
        dep_label = Label(Left_label_Course,text = "Department",font = ("Comic Sans MS", 12, "bold"),fg="#ffffff",bg="#000")
        dep_label.grid(row=0,column = 0,padx = 5,sticky = W)
        
        dep_combobox = ttk.Combobox(Left_label_Course,font = ("Comic Sans MS", 10),state = "readonly")
        dep_combobox["values"] = ("Select department","CSE","IT","ECE")
        dep_combobox.current(0)
        dep_combobox.grid(row= 0,column = 1,padx = 5,pady =20,sticky = W)
        
        #Semester
        
        sem_label = Label(Left_label_Course,text = "Semester",font = ("Comic Sans MS", 12, "bold"),fg="#ffffff",bg="#000")
        sem_label.grid(row=1,column = 0,padx = 5,sticky = W)
        
        sem_combobox = ttk.Combobox(Left_label_Course,font = ("Comic Sans MS", 10),state = "readonly")
        sem_combobox["values"] = ("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth")
        sem_combobox.current(0)
        sem_combobox.grid(row= 1,column = 1,padx = 5,pady =15,sticky = W)
        
        
        # -------------------------personal details---------------------------
        Left_label_det = LabelFrame(Left_frame,bd = 2,relief = RIDGE,text = "Personal Details",font = ("Comic Sans MS", 12, "bold"),bg="#000",fg="#ffffff")
        Left_label_det.place(x = 10,y = 180,width = 660,height = 380)
        
        #Student Name
 
        name_label = Label(Left_label_det,text = "Student Name",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        name_label.grid(row=0,column = 0,padx = 15,pady = 5,sticky = W)

        name_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        name_entry.grid(row=0,column = 1,padx = 15,pady = 5,sticky = W)
       
        #Roll no
 
        roll_label = Label(Left_label_det,text = "Student Roll",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        roll_label.grid(row=1,column = 0,padx = 15,pady = 5,sticky = W)
        
        roll_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        roll_entry.grid(row=1,column = 1,padx = 15,pady = 5,sticky = W)
 
        #Registration No
        roll_label = Label(Left_label_det,text = "Registration Number",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        roll_label.grid(row=0,column = 2,padx = 15,pady = 5,sticky = W)
        
        roll_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        roll_entry.grid(row=0,column = 3,padx = 15,pady = 5,sticky = W)
        
        #Email
        email_label = Label(Left_label_det,text = "Email",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        email_label.grid(row=1,column = 2,padx = 15,pady = 5,sticky = W)
        
        email_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        email_entry.grid(row=1,column = 3,padx = 15,pady = 5,sticky = W)
       
        #Phone Number
        phone_label = Label(Left_label_det,text = "Phone",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        phone_label.grid(row=2,column = 0,padx = 15,pady = 5,sticky = W)
        
        phone_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        phone_entry.grid(row=2,column = 1,padx = 15,pady = 5,sticky = W)
       
       #DOB
        dob_label = Label(Left_label_det,text = "Date of Birth",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        dob_label.grid(row=2,column = 0,padx = 15,pady = 5,sticky = W)
        
        dob_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        dob_entry.grid(row=2,column = 1,padx = 15,pady = 5,sticky = W)
        
        #Nationality
        nat_label = Label(Left_label_det,text = "Nationality",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        nat_label.grid(row=2,column = 2,padx = 15,pady = 5,sticky = W)
  
        nat_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        nat_entry.grid(row=2,column = 3,padx = 15,pady = 5,sticky = W)
        
        
        #Gender
        gen_label = Label(Left_label_det,text = "Gender",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        gen_label.grid(row=3,column = 0,padx = 15,pady = 5,sticky = W)
        
        gen_combobox = ttk.Combobox(Left_label_det,font = ("Comic Sans MS", 10),state = "readonly",width = 15)
        gen_combobox["values"] = ("male","female")
        gen_combobox.current(0)
        gen_combobox.grid(row= 3,column = 1,padx = 15,pady =5,sticky = W)


        #father's name
        fat_label = Label(Left_label_det,text = "Father Name",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        fat_label.grid(row=3,column = 2,padx = 15,pady = 5,sticky = W)
        fat_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"))
        fat_entry.grid(row=3,column = 3,padx = 15,pady = 5,sticky = W)
 
        #button frame
        btn_frame = Frame(Left_label_det,bd = 2, relief = RIDGE,bg = "#000")
        btn_frame.place(x = 5,y = 260,width = 645,height = 50)
        
        take_pic_sample = Button(btn_frame,text = "Take Photo",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        take_pic_sample.grid(row = 0,column = 0)
        
        Update_pic_sample = Button(btn_frame,text = "Update Photo",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        Update_pic_sample.grid(row = 0,column = 1)
    
        save_btn = Button(btn_frame,text = "Save",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        save_btn.grid(row = 0,column = 0,padx = 5,pady = 2)

        reset_btn = Button(btn_frame,text = "Reset",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        reset_btn.grid(row = 0,column = 1,padx = 5,pady = 2)

        delete_btn = Button(btn_frame,text = "Delete",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        delete_btn.grid(row = 0,column = 2,padx = 5,pady = 2)
        
        Update_btn = Button(btn_frame,text = "Update",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        Update_btn.grid(row = 0,column = 3,padx = 5,pady = 2)

        
        #button frame
        btn_frame_2 = Frame(Left_label_det,bd = 2, relief = RIDGE,bg = "#000")
        btn_frame_2.place(x = 5,y = 170,width = 645,height = 50)
        
        take_pic_sample = Button(btn_frame_2,text = "Take Photo Samples",font = ("Comic Sans MS", 12, "bold"),width = 30,fg = "#000",bg = "#ffffff")
        take_pic_sample.grid(row = 0,column = 0,padx=5,pady=2)
        
        Update_pic_sample = Button(btn_frame_2,text = "Update Photo Samples",font = ("Comic Sans MS", 12, "bold"),width = 30,fg = "#000",bg = "#ffffff")
        Update_pic_sample.grid(row = 0,column = 1,padx=5,pady=2)
        

        #--------------------------------------------------------------------Right label frame---------------------------------------------------------------------------
        Right_frame = LabelFrame(main_frame,bd = 5,relief = RIDGE,text = "All Students",font = ("Comic Sans MS", 12, "bold"),bg="#000",fg="#ffffff")
        Right_frame.place(x = 740,y = 10,width = 690,height = 600)
        
        #===================Searching======================
        Search_frame = LabelFrame(Right_frame,bd = 2,relief = RIDGE,text = "Search",font = ("Comic Sans MS", 12, "bold"),bg="#000",fg="#ffffff")
        Search_frame.place(x = 10,y = 10,width = 660,height = 80)
        
        Searchby_label = Label(Search_frame,text = "Search By",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        Searchby_label.grid(row=0,column = 0,padx = 10,pady = 5,sticky = W)
        
        Searchby_combobox = ttk.Combobox(Search_frame,font = ("Comic Sans MS", 10),state = "readonly",width = 15)
        Searchby_combobox["values"] = ("Select","Registration Number")
        Searchby_combobox.current(0)
        Searchby_combobox.grid(row= 0,column = 1,padx = 15,pady =5,sticky = W)
        
        search_entry = ttk.Entry(Search_frame,width = 14,font = ("Comic Sans MS", 10, "bold"))
        search_entry.grid(row=0,column = 2,padx = 5,pady = 5,sticky = W)
        
        
        show_btn = Button(Search_frame,text = "Show all",font = ("Comic Sans MS", 12, "bold"),width = 10,height=1,fg = "#000",bg = "#ffffff")
        show_btn.grid(row = 0,column = 4,padx = 10,pady = 2)
        
        Search_btn = Button(Search_frame,text = "Search",font = ("Comic Sans MS", 12, "bold"),width = 10,height=1,fg = "#000",bg = "#ffffff")
        Search_btn.grid(row = 0,column = 3,padx = 3,pady = 2)
        
        #===================Searching======================
        table_frame = Frame(Right_frame,bd = 2,relief = RIDGE,bg="#000")
        table_frame.place(x = 10,y = 100,width = 660,height = 450)
        
        scroll_x = ttk.Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient = VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column = ("Registrationnumber","Course","RollNo","Name","Email","PhoneNumber","DOB","Genders","Photo"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)
        
        self.student_table.heading("Registrationnumber",text = "Registration number")
        self.student_table.heading("Course",text = "Course")
        self.student_table.heading("RollNo",text = "Roll No")
        self.student_table.heading("Name",text = "Name")
        self.student_table.heading("Email",text = "Email")
        self.student_table.heading("PhoneNumber",text = "Phone Number")
        self.student_table.heading("DOB",text = "DOB")
        self.student_table.heading("Genders",text = "Gender")
        self.student_table.heading("Photo",text = "Photo Status")
        
        
        self.student_table["show"] = "headings"
        self.student_table.pack(fill = BOTH,expand = 1)
        
        
        

if __name__ == "__main__":
    root = Tk()
    frs = Student(root)
    root.mainloop()