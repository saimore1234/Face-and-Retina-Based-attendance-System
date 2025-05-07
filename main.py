from tkinter import Label, Tk, Button, Toplevel  # Added Button import
from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from employee import Employee
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition1 import Face_Recognition
from attendance import Attendance
from developer import Developer

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face_Recognition_System")

        # Load and resize the first image
        img = Image.open(r"Collage_image\images.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Display the first image in a label
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Load and resize the second image
        img1 = Image.open(r"Collage_image\images (2).jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Display the second image in a label
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Load and resize the third image
        img2 = Image.open(r"Collage_image\face.png")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Display the third image in a label
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # Load and resize the background image
        img3 = Image.open(r"Collage_image\0455.jpg_wh300.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Display the background image in a label
        bg = Label(self.root, image=self.photoimg3)
        bg.place(x=0, y=130, width=1530, height=710)

        # Title label
        title_lbl = Label(bg, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #__________________Time____________________________
        def time():
            string =    strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl= Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='black')
        lbl.place(x=0,y= 0,width=110,height=50)
        time()

        # Load and resize the student button image
        img4 = Image.open(r"Collage_image\images.png")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Create the button with the image (Student button)
        employee_button = Button(bg, image=self.photoimg4, command=self.employee_details, cursor="hand2")
        employee_button.place(x=200, y=100, width=220, height=220)

        # Create the button with text (Student Details button)
        employee_details_button = Button(bg, text="Employee Details", command=self.employee_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=200, y=300, width=220, height=40)

        # Second Detect face Button
        img5 = Image.open(r"Collage_image\facedetector.jpeg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # Create the button with the image (Face detector)
        employee_button = Button(bg, image=self.photoimg5, cursor="hand2",command=self.face_data)
        employee_button.place(x=500, y=100, width=220, height=220)

        # Create the button with text (Face Detector)
        employee_details_button = Button(bg, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img6 = Image.open(r"Collage_image\attendance.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        # Create the button with the image (Face detector)
        employee_button = Button(bg, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        employee_button.place(x=800, y=100, width=220, height=220)

        # Create the button with text (Face Detector)
        employee_details_button = Button(bg, text="Attendance System", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=800, y=300, width=220, height=40)

        # Retina system Button
        img7 = Image.open(r"Collage_image\helpdesk.jpeg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        # Create the button with the image (help Desk)
        employee_button = Button(bg, image=self.photoimg7, cursor="hand2")
        employee_button.place(x=1100, y=100, width=220, height=220)

        # Create the button with text (help Desk)
        employee_details_button = Button(bg, text="Retina System", cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=1100, y=300, width=220, height=40)

        # Train Face Button
        img8 = Image.open(r"Collage_image\FaceTrain.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        # Create the button with the image (Train face)
        employee_button = Button(bg, image=self.photoimg8, cursor="hand2",command=self.train_data)
        employee_button.place(x=200, y=380, width=220, height=220)

        # Create the button with text (Train face)
        employee_details_button = Button(bg, text="Train Face", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=200, y=580, width=220, height=40)

        # Photos Button
        img9 = Image.open(r"Collage_image\photos.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        # Create the button with the image (Photos Button)
        employee_button = Button(bg, image=self.photoimg9, cursor="hand2",command=self.open_img)
        employee_button.place(x=500, y=380, width=220, height=220)

        # Create the button with text (Photos Button)
        employee_details_button = Button(bg, text="Photos Data", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=500, y=580, width=220, height=40)

        # Developer Button
        img10 = Image.open(r"Collage_image\Developer.png")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        # Create the button with the image (Photos Button)
        employee_button = Button(bg, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        employee_button.place(x=800, y=380, width=220, height=220)

        # Create the button with text (Photos Button)
        employee_details_button = Button(bg, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=800, y=580, width=220, height=40)

        # Exit Button
        img11 = Image.open(r"Collage_image\Exit.png")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        # Create the button with the image (Photos Button)
        employee_button = Button(bg, image=self.photoimg11, cursor="hand2",command=self.iexit)
        employee_button.place(x=1100, y=380, width=220, height=220)

        # Create the button with text (Photos Button)
        employee_details_button = Button(bg, text="Exit Data", cursor="hand2",command=self.iexit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        employee_details_button.place(x=1100, y=580, width=220, height=40)



    def open_img(self):
        os.startfile("data")

    
    def iexit(self):
        self.iexit= tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this system",parent = self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return




#================================Function Buttons========================
    def employee_details(self):
        print("Employee details button clicked")  # Added print statement
        self.new_window = Toplevel(self.root) 
        self.app = Employee(self.new_window) 
    
    def train_data(self):
        print("Train Data button clicked")  # Added print statement
        self.new_window = Toplevel(self.root) 
        self.app = Train(self.new_window) 

    def face_data(self):
        print("Face Data button clicked")  # Added print statement
        self.new_window = Toplevel(self.root) 
        self.app = Face_Recognition(self.new_window) 
    
    def attendance_data(self):
        print("Attendance Data button clicked")  # Added print statement
        self.new_window = Toplevel(self.root) 
        self.app = Attendance(self.new_window)

    def developer_data(self):
        print("Attendance Data button clicked")  # Added print statement
        self.new_window = Toplevel(self.root) 
        self.app = Developer(self.new_window) 


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
