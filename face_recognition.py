
from re import X
from tkinter import BOTTOM, HORIZONTAL, RIGHT, VERTICAL, Y, Label, StringVar, Tk, ttk, Button, Frame, LabelFrame, messagebox, RIDGE
from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import mysql.connector 
import cv2
import os
import numpy as np


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face_Recognition_System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=1, width=1530, height=45)

        img_top = Image.open(r"Collage_image\FaceDetect.jpg")
        img_top = img_top.resize((650,700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        left_bg_label = Label(self.root, image=self.photoimg_top)
        left_bg_label.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"Collage_image\FaceDetect2.jpeg")
        img_bottom = img_bottom.resize((950,700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        left_bg_label = Label(self.root, image=self.photoimg_bottom)
        left_bg_label.place(x=650, y=55, width=950, height=700)

        student_details_button = Button(left_bg_label, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkblue", fg="white")
        student_details_button.place(x=365, y=620, width=200, height=40)

    #---------------------------Attendance------------------------------------------------------------

    def mark_attendance(self,i,s,d,e):
        with open("Attendance.csv","r+",newline="\n")as f :
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (s not in name_list)and (d not in name_list)and (e not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{e},{s},{i},{d},{dtString},{d1},Punch In")

    #-------------------------------------------Face Recognition-----------------------------------------------

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            if img is None:
                print("Empty frame received")
                return img

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="12@02", database="face_iris_attendence")
                my_cursor = conn.cursor()

                def safe_fetch(query):
                    my_cursor.execute(query)
                    res = my_cursor.fetchone()
                    return "+".join(res) if res else "Unknown"

                i = safe_fetch("Select Emp_name from employee where employee_id=" + str(id))
                s = safe_fetch("Select jobtitle from employee where employee_id=" + str(id))
                d = safe_fetch("Select Dep from employee where employee_id=" + str(id))
                e = safe_fetch("Select employee_id from employee where employee_id=" + str(id))

                if confidence > 77:
                    cv2.putText(img, f"ID :{e}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Employee name:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Job Title:{s}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,s,d,e)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        if hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
            clf = cv2.face.LBPHFaceRecognizer_create()
        else:
            clf = cv2.face.LBPHFaceRecognizer.create()

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13 or cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
