from re import X
from tkinter import BOTTOM, HORIZONTAL, RIGHT, VERTICAL, Y, Label, StringVar, Tk, ttk, Button, Frame, LabelFrame, messagebox, RIDGE
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face_Recognition_System")

        #=================variables===========================
        self.var_attend_id = StringVar()
        self.var_attend_jd = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_status = StringVar()

        img1 = Image.open(r"Collage_image\Attend1.png")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Display the second image in a label
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=800, height=200)

        # Load and resize the third image
        img2 = Image.open(r"Collage_image\Attend2.WEBP")
        img2 = img2.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=800, y=0, width=800, height=200)

#bg-----------------------
        img3 = Image.open(r"Collage_image\0455.jpg_wh300.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Display the background image in a label
        bg = Label(self.root, image=self.photoimg3)
        bg.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg, text="Employee Attendance Record", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Create the main frame
        main_frame = Frame(bg, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1460, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Attendance Details", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"Collage_image\group1.jpg")
        img_left = img_left.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_bg_label = Label(Left_frame, image=self.photoimg_left)
        left_bg_label.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame( Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=4, y=135, width=720, height=370)

        #Lablel and entry
        attendance_id_label = Label(left_inside_frame, text="Employee Id: ", font=("times new roman", 13, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10,pady=5, sticky="W")

        attendance_id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_id, font=("times new roman", 13, "bold"), width=20)
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

        # Job title
        job_title_label = Label(left_inside_frame, text="Job Title: ", font=("times new roman", 11, "bold"), bg="white")
        job_title_label.grid(row=0, column=2, padx=4,pady=8)

        job_title_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_jd, font=("times new roman", 11, "bold"), width=22)
        job_title_entry.grid(row=0, column=3, pady=8)


        #Name
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 11, "bold"), bg="white")
        Name_label.grid(row=1, column=0)

        Name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_name, font=("times new roman", 11, "bold"), width=22)
        Name_entry.grid(row=1, column=1, pady=8,)

        #Dep

        dep_label = Label(left_inside_frame, text="Department: ", font=("times new roman", 11, "bold"), bg="white")
        dep_label.grid(row=1, column=2)

        dep_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_dep,font=("times new roman", 11, "bold"), width=22)
        dep_entry.grid(row=1, column=3, pady=8,)

        #Time 

        Time_label = Label(left_inside_frame, text="Time: ", font=("times new roman", 11, "bold"), bg="white")
        Time_label.grid(row=2, column=0)

        Time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_time, font=("times new roman", 11, "bold"), width=22)
        Time_entry.grid(row=2, column=1, pady=8,)

        #Date

        Date_label = Label(left_inside_frame, text="Date: ", font=("times new roman", 11, "bold"), bg="white")
        Date_label.grid(row=2, column=2)

        Date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_date, font=("times new roman", 11, "bold"), width=22)
        Date_entry.grid(row=2, column=3, pady=8,)

        #attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 13, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0)


        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_attend_status, font=("times new roman", 13, "bold"), width=20, state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)

         # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        save_btn = Button(btn_frame, text="Import Csv", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Update
        Update_btn = Button(btn_frame, text="Export Csv",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)
    

        # Delete
        Delete_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)

        # Reset
        Reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)

        


        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Database", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Right_frame.place(x=750, y=10, width=700, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=680, height=455)

        #S++++++++Scorll Bar

        scoll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scoll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","job_title","name","department","time","date","attendance"),xscrollcommand=scoll_x.set,yscrollcommand=scoll_y.set)
        
        scoll_x.pack(side=BOTTOM,fill=X)
        scoll_y.pack(side=RIGHT,fill=Y)

        scoll_x.config(command=self.AttendanceReportTable.xview)
        scoll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("job_title",text="Job Title")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("job_title",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)

#=============================Face Data=======================================================
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #Import Csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export Csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent= self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir= os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is exported to"+os.path.basename(fln)+"Succesfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def getcursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_jd.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_status.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_jd.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("")

        

                               
                               
                               

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
