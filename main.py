from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
 

class FaceRecognitionSystem:
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
        title_lbl = Label(bg,text = "FACE RECOGNITION ATTENDANCE SYSTEM",font = ("Comic Sans MS", 35, "bold"),bg = "#000000",fg = "white")
        title_lbl.place(x=0,y=0,width = 1530,height = 90)
        
        #---------------------------------------Buttons Row 1--------------------------------------------
        #student button
        btn_img_1 = Image.open(r"E:\FaceRecogniseSystem\images\student_btn.jpg")
        btn_img_1 = btn_img_1.resize((220,220),Image.ANTIALIAS)
        self.photoimage_1 = ImageTk.PhotoImage(btn_img_1)
        
        btn_1 = Button(bg,image = self.photoimage_1,command = self.student_page,cursor = "hand2")
        btn_1.place(x = 200,y = 250,height =220,width = 220)
        btn_1_text = Button(bg,text = "Student record",command = self.student_page,cursor = "hand2",font = ("Comic Sans MS", 20, "bold"),bg = "#000000",fg = "white")
        btn_1_text.place(x = 200,y = 450,height =45,width = 220)
        
        
        
        
        #Detect Faces
        btn_img_2 = Image.open(r"E:\FaceRecogniseSystem\images\detectface.jpg")
        btn_img_2 = btn_img_2.resize((220,220),Image.ANTIALIAS)
        self.photoimage_2 = ImageTk.PhotoImage(btn_img_2)
        
        btn_2 = Button(bg,image = self.photoimage_2,cursor = "hand2")
        btn_2.place(x = 500,y = 250,height =220,width = 220)
        btn_2_text = Button(bg,text = "Detect Faces",cursor = "hand2",font = ("Comic Sans MS", 18, "bold"),bg = "#000000",fg = "white")
        btn_2_text.place(x = 500,y = 450,height =45,width = 220)
        

        #Attendance
        btn_img_3 = Image.open(r"E:\FaceRecogniseSystem\images\attendance.png")
        btn_img_3 = btn_img_3.resize((220,220),Image.ANTIALIAS)
        self.photoimage_3 = ImageTk.PhotoImage(btn_img_3)
        
        btn_3 = Button(bg,image = self.photoimage_3,cursor = "hand2")
        btn_3.place(x = 800,y = 250,height =220,width = 220)
        btn_3_text = Button(bg,text = "Attendance",cursor = "hand2",font = ("Comic Sans MS", 18, "bold"),bg = "#000000",fg = "white")
        btn_3_text.place(x = 800,y = 450,height =45,width = 220)
        
        
        
        #support
        btn_img_4 = Image.open(r"E:\FaceRecogniseSystem\images\di.jpg")
        btn_img_4 = btn_img_4.resize((220,220),Image.ANTIALIAS)
        self.photoimage_4 = ImageTk.PhotoImage(btn_img_4)
        
        btn_4 = Button(bg,image = self.photoimage_4,cursor = "hand2")
        btn_4.place(x = 1100,y = 250,height =220,width = 220)
        btn_4_text = Button(bg,text = "Train Data",cursor = "hand2",font = ("Comic Sans MS", 18, "bold"),bg = "#000000",fg = "white")
        btn_4_text.place(x = 1100,y = 450,height =45,width = 220)
        
        
    def student_page(self):
        self.new_window = Toplevel(self.root)
        self.stud_det = Student(self.new_window)
                                                                                                                                  
if __name__ == "__main__":
    root = Tk()
    frs = FaceRecognitionSystem(root)
    root.mainloop()
