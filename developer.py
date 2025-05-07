from re import X
from tkinter import BOTTOM, HORIZONTAL, RIGHT, VERTICAL, Y, Label, StringVar, Tk, ttk, Button, Frame, LabelFrame, messagebox, RIDGE
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector 
import cv2
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face_Recognition_System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="Blue")
        title_lbl.place(x=0, y=1, width=1530, height=45)

        img_top = Image.open(r"Collage_image\face-recognition-System-scaled-1.WEBP")
        img_top = img_top.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

 
        left_bg_label = Label(self.root, image=self.photoimg_top)
        left_bg_label.place(x=0, y=55, width=1530, height=720)

        main_frame = Frame(left_bg_label, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=490, height=600)
        

        # img_top1 = Image.open(r"Collage_image\face-recognition-System-scaled-1.WEBP")
        # img_top1 = img_top1.resize((200,200), Image.Resampling.LANCZOS)
        # self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

 
        # left_bg_label = Label(main_frame, image=self.photoimg_top1)
        # left_bg_label.place(x=300, y=0, width=200, height=200)

        #Developer Info
        dev_label = Label(main_frame, text="Deveploper Name: ", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x =0 , y= 5)

        dev_label = Label(main_frame, text="Sahil Deshmukh B.E(Computer Engineering)", font=("times new roman", 16, "bold"), bg="white")
        dev_label.place(x =0 , y= 45)

        dev_label = Label(main_frame, text="Sai More B.E(Computer Engineering)", font=("times new roman", 16, "bold"), bg="white")
        dev_label.place(x =0 , y= 85)

        dev_label = Label(main_frame, text="Vaidehi Patil B.E(Computer Engineering)", font=("times new roman", 16, "bold"), bg="white")
        dev_label.place(x =0 , y= 125)

        dev_label = Label(main_frame, text="Ashish Mhashalkar B.E(Computer Engineering)", font=("times new roman", 16, "bold"), bg="white")
        dev_label.place(x =0 , y= 165)

        





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()