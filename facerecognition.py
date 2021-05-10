from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import cv2
import mysql.connector
 

class Recognize:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Background image
        bg_img = Image.open(r"E:\FaceRecogniseSystem\images\face_detector1.jpg")
        bg_img = bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(bg_img)
        bg = Label(self.root,image = self.photoimage)
        bg.place(x = 0,y = 0,width = 1530,height = 790)
        
        #title
        title_lbl = Label(bg,text = "Detect Faces And Take Attendance",font = ("Comic Sans MS", 25, "bold"),bg = "#23049d",fg = "white")
        title_lbl.place(x=0,y=0,width = 1530,height = 90)
        
        #button
        btn = Button(bg,text = "Take Attendance",command = self.face_recog,font = ("Comic Sans MS", 25, "bold"),bg = "#23049d",fg = "white")
        btn.place(x= 30,y = 350,height = 70,width = 1470)
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                ids,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int(100*(1-predict/300))
                
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "pavan@123",database = "facerecognitionsystem")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select name from student_db where reg = "+str(ids))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                my_cursor.execute("select roll from student_db where reg = "+str(ids))
                j = my_cursor.fetchone()
                j = "+".join(j)
                
                if confidence>79:
                    cv2.putText(img,f"Roll : {j}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Name : {i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,f"Unknown",(x,y-55),cv2.FONT_HERSHEY_PLAIN,0.8,(255,255,0),3)
                coord = [x,y,w,h]
            return coord
        
        def recognizee(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf) 
            return img
        
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classfiermodel.xml")   
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret,img = video_cap.read()
            img = recognizee(img,clf,faceCascade)
            
            cv2.imshow("Taking Attendance",img)
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    frs = Recognize(root)
    root.mainloop()
