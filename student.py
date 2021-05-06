from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #=============Variables====================
        self.var_dep = StringVar()
        self.var_regno = StringVar()
        self.var_Course = StringVar()
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_dob = StringVar()
        self.var_gen = StringVar()
        self.var_sem = StringVar()
        self.var_nat = StringVar()
        self.var_fat = StringVar()
        
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
        
        dep_combobox = ttk.Combobox(Left_label_Course,font = ("Comic Sans MS", 10),state = "readonly",textvariable = self.var_dep)
        dep_combobox["values"] = ("Select department","CSE","IT","ECE")
        dep_combobox.current(0)
        dep_combobox.grid(row= 0,column = 1,padx = 5,pady =20,sticky = W)
        
        #Semester
        
        sem_label = Label(Left_label_Course,text = "Semester",font = ("Comic Sans MS", 12, "bold"),fg="#ffffff",bg="#000")
        sem_label.grid(row=1,column = 0,padx = 5,sticky = W)
        
        sem_combobox = ttk.Combobox(Left_label_Course,font = ("Comic Sans MS", 10),state = "readonly",textvariable = self.var_sem)
        sem_combobox["values"] = ("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth")
        sem_combobox.current(0)
        sem_combobox.grid(row= 1,column = 1,padx = 5,pady =15,sticky = W)
        
        
        # -------------------------personal details---------------------------
        Left_label_det = LabelFrame(Left_frame,bd = 2,relief = RIDGE,text = "Personal Details",font = ("Comic Sans MS", 12, "bold"),bg="#000",fg="#ffffff")
        Left_label_det.place(x = 10,y = 180,width = 660,height = 380)
        
        #Student Name
 
        name_label = Label(Left_label_det,text = "Student Name",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        name_label.grid(row=0,column = 0,padx = 15,pady = 5,sticky = W)

        name_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_name)
        name_entry.grid(row=0,column = 1,padx = 15,pady = 5,sticky = W)
       
        #Roll no
 
        roll_label = Label(Left_label_det,text = "Student Roll",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        roll_label.grid(row=1,column = 0,padx = 15,pady = 5,sticky = W)
        
        roll_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_rollno)
        roll_entry.grid(row=1,column = 1,padx = 15,pady = 5,sticky = W)
 
        #Registration No
        reg_label = Label(Left_label_det,text = "Registration Number",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        reg_label.grid(row=0,column = 2,padx = 15,pady = 5,sticky = W)
        
        reg_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_regno)
        reg_entry.grid(row=0,column = 3,padx = 15,pady = 5,sticky = W)
        
        #Email
        email_label = Label(Left_label_det,text = "Email",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        email_label.grid(row=1,column = 2,padx = 15,pady = 5,sticky = W)
        
        email_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_email)
        email_entry.grid(row=1,column = 3,padx = 15,pady = 5,sticky = W)
       
        #Phone Number
        phone_label = Label(Left_label_det,text = "Phone",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        phone_label.grid(row=2,column = 0,padx = 15,pady = 5,sticky = W)
        
        phone_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_phone)
        phone_entry.grid(row=2,column = 1,padx = 15,pady = 5,sticky = W)
       
       #DOB
        dob_label = Label(Left_label_det,text = "Date of Birth",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        dob_label.grid(row=2,column = 0,padx = 15,pady = 5,sticky = W)
        
        dob_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_dob)
        dob_entry.grid(row=2,column = 1,padx = 15,pady = 5,sticky = W)
        
        #Nationality
        nat_label = Label(Left_label_det,text = "Nationality",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        nat_label.grid(row=2,column = 2,padx = 15,pady = 5,sticky = W)
  
        nat_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_nat)
        nat_entry.grid(row=2,column = 3,padx = 15,pady = 5,sticky = W)
        
        
        #Gender
        gen_label = Label(Left_label_det,text = "Gender",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        gen_label.grid(row=3,column = 0,padx = 15,pady = 5,sticky = W)
        
        gen_combobox = ttk.Combobox(Left_label_det,font = ("Comic Sans MS", 10),state = "readonly",width = 15,textvariable = self.var_gen)
        gen_combobox["values"] = ("male","female")
        gen_combobox.current(0)
        gen_combobox.grid(row= 3,column = 1,padx = 15,pady =5,sticky = W)


        #father's name
        fat_label = Label(Left_label_det,text = "Father Name",font = ("Comic Sans MS", 10, "bold"),fg="#ffffff",bg="#000")
        fat_label.grid(row=3,column = 2,padx = 15,pady = 5,sticky = W)
        fat_entry = ttk.Entry(Left_label_det,width = 17,font = ("Comic Sans MS", 10, "bold"),textvariable = self.var_fat)
        fat_entry.grid(row=3,column = 3,padx = 15,pady = 5,sticky = W)
 
        #button frame
        btn_frame = Frame(Left_label_det,bd = 2, relief = RIDGE,bg = "#000")
        btn_frame.place(x = 5,y = 260,width = 645,height = 50)
        
        take_pic_sample = Button(btn_frame,text = "Take Photo",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        take_pic_sample.grid(row = 0,column = 0)
        
        Update_pic_sample = Button(btn_frame,text = "Update Photo",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        Update_pic_sample.grid(row = 0,column = 1)
    
        save_btn = Button(btn_frame,text = "Save",command = self.add_data,font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        save_btn.grid(row = 0,column = 0,padx = 5,pady = 2)

        reset_btn = Button(btn_frame,text = "Reset",font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        reset_btn.grid(row = 0,column = 1,padx = 5,pady = 2)

        delete_btn = Button(btn_frame,text = "Delete",command=self.delete,font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        delete_btn.grid(row = 0,column = 2,padx = 5,pady = 2)
        
        Update_btn = Button(btn_frame,text = "Update",command = self.update_data,font = ("Comic Sans MS", 12, "bold"),width = 14,fg = "#000",bg = "#ffffff")
        Update_btn.grid(row = 0,column = 3,padx = 5,pady = 2)

        
        #button frame
        btn_frame_2 = Frame(Left_label_det,bd = 2, relief = RIDGE,bg = "#000")
        btn_frame_2.place(x = 5,y = 170,width = 645,height = 50)
        
        take_pic_sample = Button(btn_frame_2,text = "Take Photo Samples",command=self.take_photosample,font = ("Comic Sans MS", 12, "bold"),width = 30,fg = "#000",bg = "#ffffff")
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
        
        self.student_table = ttk.Treeview(table_frame,column = ("id","dep","sem","reg","roll","name","gender","dob","nat","email","fat","photo"),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)
        
        self.student_table.heading("id",text = "id")
        self.student_table.heading("dep",text = "Department")
        self.student_table.heading("sem",text = "Semester")
        self.student_table.heading("reg",text = "Reg No")
        self.student_table.heading("roll",text = "Roll No")
        self.student_table.heading("name",text = "Name")
        self.student_table.heading("gender",text = "Gender")
        self.student_table.heading("dob",text = "dob")
        self.student_table.heading("nat",text = "Nationality")
        self.student_table.heading("email",text = "Email")
        self.student_table.heading("fat",text = "Father Name")
        self.student_table.heading("photo",text = "Photo samples")
        
        self.student_table.column("id",width = 100)
        self.student_table.column("dep",width = 100)
        self.student_table.column("sem",width = 100)
        self.student_table.column("reg",width = 100)
        self.student_table.column("roll",width = 100)
        self.student_table.column("name",width = 100)
        self.student_table.column("gender",width = 100)
        self.student_table.column("dob",width = 100)
        self.student_table.column("nat",width = 100)
        self.student_table.column("email",width = 100)
        self.student_table.column("fat",width = 100)
        self.student_table.column("photo",width = 100)
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
                
        self.student_table["show"] = "headings"
        self.student_table.pack(fill = BOTH,expand = 1)
        self.fetch_data()
        
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_regno.get()=="" or self.var_rollno.get()=="":
           messagebox.showerror("Error","Please fill all the fileds")
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "pavan@123",database = "facerecognitionsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student_db values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    "1",
                    self.var_dep.get(),
                    self.var_sem.get(),
                    self.var_regno.get(),
                    self.var_rollno.get(),
                    self.var_name.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_nat.get(),
                    self.var_email.get(),
                    self.var_fat.get(),
                    "yes"
                
                ))
                self.var_dep.set("")
                self.var_sem.set("")
                self.var_regno.set("")
                self.var_name.set("")
                self.var_gen.set("")
                self.var_dob.set("")
                self.var_nat.set("")
                self.var_email.set("")
                self.var_fat.set("")
                self.var_rollno.set("")
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully Added into the database",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"error{str(es)}",parent = self.root)
    
    
    #======================fetch data=========================
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",username = "root",password = "pavan@123",database = "facerecognitionsystem")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student_db")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                
    
    # ===============get cursor======================  
    def get_cursor(self,event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[1])
        self.var_sem.set(data[2])
        self.var_regno.set(data[3])
        self.var_rollno.set(data[4])
        self.var_name.set(data[5])
        self.var_gen.set(data[6])
        self.var_dob.set(data[7])
        self.var_nat.set(data[8])
        self.var_email.set(data[9])
        self.var_fat.set(data[10])
        
    
    #=============Update===============
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_regno.get()=="" or self.var_rollno.get()=="":
            messagebox.showerror("Error","Please fill all the fileds")
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to Udate the student details",parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "pavan@123",database = "facerecognitionsystem")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student_db set dep=%s,sem=%s,reg=%s,name=%s,gender=%s,dob=%s,nationality=%s,email=%s,fathername=%s where roll=%s",(
                        
                        self.var_dep.get(),
                        self.var_sem.get(),
                        self.var_regno.get(),
                        self.var_name.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_nat.get(),
                        self.var_email.get(),
                        self.var_fat.get(),
                        self.var_rollno.get()
                    ))
                    
                    self.var_dep.set("")
                    self.var_sem.set("")
                    self.var_regno.set("")
                    self.var_name.set("")
                    self.var_gen.set("")
                    self.var_dob.set("")
                    self.var_nat.set("")
                    self.var_email.set("")
                    self.var_fat.set("")
                    self.var_rollno.set("")
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","Updated successfully",parent = self.root)
                
                conn.commit()
                conn.close()

                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error",f"Error : {str(es)}")
                
    #===============delete=============
    def delete(self):
        if self.var_rollno.get() == "":
            messagebox.showerror("Error","Student Roll required",parent = self.root)
        else:
            try : 
                delete = messagebox.askyesno("Delete","Do you want to delete this student",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "pavan@123",database = "facerecognitionsystem")
                    my_cursor = conn.cursor()
                    sql = "delete from student_db where roll=%s"
                    val = (self.var_rollno.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted successfully",parent =self.root)
                self.var_dep.set("")
                self.var_sem.set("")
                self.var_regno.set("")
                self.var_name.set("")
                self.var_gen.set("")
                self.var_dob.set("")
                self.var_nat.set("")
                self.var_email.set("")
                self.var_fat.set("")
                self.var_rollno.set("")
            except Exception as es:
                messagebox.showerror("Error",f"Error : {str(es)}")
                
    #=========================Generate dataset==========================
    def take_photosample(self):
        if self.var_regno.get()=="":
            messagebox.showerror("Error","Please fill details")
        else:
            #load data
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                       
            def face_cropped(img):
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                for (x,y,w,h) in faces:
                    face_cropped = img[y:y+h,x:x+w]
                    return face_cropped
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret,frame_my=cap.read()
                if face_cropped(frame_my) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(frame_my),(450,450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user."+self.var_regno.get()+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)
                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Success","Generated Data set")
        
        
                                           

if __name__ == "__main__":
    root = Tk()
    frs = Student(root)
    root.mainloop()