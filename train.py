from re import X
from tkinter import BOTTOM, HORIZONTAL, RIGHT, VERTICAL, Y, Label, StringVar, Tk, ttk, Button, Frame, LabelFrame, messagebox, RIDGE
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector 
import cv2
import os
import numpy as np

#We are Using LBPH Face Recognition algorithm to train the data in ML and this train the data by next each pixel in color code and with threesold of 90
#the color no of one each 3x3 pixel below 90 pixel are denoted as 0 and then 90 pixel are denoted as 1 and 90 is blank and then it is converted into decimal

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face_Recognition_System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=1, width=1530, height=45)

        img_top = Image.open(r"Collage_image\Screenshot 2025-01-18 052535.png")
        img_top = img_top.resize((1530,320), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

 
        left_bg_label = Label(self.root, image=self.photoimg_top)
        left_bg_label.place(x=0, y=55, width=1530, height=345)
    #==========================Button==============================

        student_details_button = Button(self.root, text="Train Data",command=self.train_classfier, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        student_details_button.place(x=0, y=380, width=1530, height=60)   

    #=========================Button=============================     

        img_bottom = Image.open(r"Collage_image\Train Data.WEBP")
        img_bottom = img_bottom.resize((1530,320), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

     
        left_bg_label = Label(self.root, image=self.photoimg_bottom)
        left_bg_label.place(x=0, y=440, width=1530, height=325)
    

    def train_classfier(self):
        data_dir=("data")
        path = [ os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img, 'uint8') #uint8 is data type in array
            id=int(os.path.split(image)[1].split('.')[1]) #split the image name and get the id 
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        # Training the classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
