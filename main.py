from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
 

class FaceRecognitionSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       
        img2 = Image.open(r"E:\FaceRecogniseSystem\images\bg.jpg")
        img2 = img2.resize((1530,790),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img2)
        bg = Label(self.root,image = self.photoimage1)
        bg.place(x = 0,y = 0,width = 1530,height = 789)



if __name__ == "__main__":
    root = Tk()
    frs = FaceRecognitionSystem(root)
    root.mainloop()
