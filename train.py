from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Train:
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
        title_lbl = Label(bg,text = "TRAIN DATA SET",font = ("Comic Sans MS", 30, "bold"),bg = "#000000",fg = "white")
        title_lbl.place(x=0,y=0,width = 1530,height = 70)
        
        #train_btn
        btn_1 = Button(bg,text = "Train Data",command = self.train_classifier,font = ("Comic Sans MS", 25,"bold"),bg="#325288",fg = "#ffffff")
        btn_1.place(x=30,y=380,width = 1470,height = 70)
       
    def train_classifier(self):
        data_dir = ("data")
        path = [ os.path.join(data_dir,file) for file in os.listdir(data_dir) ]
        faces =[]
        ids = []
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            idss = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(idss)
            cv2.imshow("Training....",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        
        #====train======
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classfiermodel.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Train Data","Data is trained Successfully")
        
            
        
            
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    frs = Train(root)
    root.mainloop()
