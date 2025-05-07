from re import X
from tkinter import BOTTOM, HORIZONTAL, RIGHT, VERTICAL, Y, Label, StringVar, Tk, ttk, Button, Frame, LabelFrame, messagebox, RIDGE
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector 
import cv2
import os

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face_Recognition_System")

        #==============variables=========================
        self.var_dep = StringVar()
        self.var_jobtitle = StringVar()
        self.var_emp_type = StringVar()
        self.var_work_loc = StringVar()
        self.var_employee_id = StringVar()
        self.var_Emp_name = StringVar()
        self.var_Work_shift = StringVar()
        self.var_Salary = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_Qualify = StringVar()  # Only defined once
        self.var_Search = StringVar()

        # Load and resize the first image
        img = Image.open(r"Collage_image\images12.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Display the first image in a label
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Load and resize the second image
        img1 = Image.open(r"Collage_image\img2.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Display the second image in a label
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Load and resize the third image
        img2 = Image.open(r"Collage_image\gp2.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Display the third image in a label
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # Load and resize the background image
        img3 = Image.open(r"Collage_image\white.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Display the background image in a label
        bg_image_label = Label(self.root, image=self.photoimg3)
        bg_image_label.place(x=0, y=130, width=1530, height=710)

        # Title label (centered the title)
        title_lbl = Label(bg_image_label, text="Employee Management System", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=480, y=0, width=599, height=55)

        # Create the main frame
        main_frame = Frame(bg_image_label, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Left_frame.place(x=10, y=10, width=730, height=580)

        # Left label image
        img_left = Image.open(r"Collage_image\group1.jpg")
        img_left = img_left.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        # Display the background image in a label inside the left frame
        left_bg_label = Label(Left_frame, image=self.photoimg_left)
        left_bg_label.place(x=5, y=0, width=720, height=130)

        # Current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Employee information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky="W")

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), width=20, state="read only")
        dep_combo["values"] = ("Select Department", "IT","Human Resources","Sales","Marketing","Finance","Operations")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky="W")

        # Course
        job_title_label = Label(current_course_frame, text="Job Title", font=("times new roman", 13, "bold"), bg="white")
        job_title_label.grid(row=0, column=2, padx=10, sticky="W")

        job_title_combo = ttk.Combobox(current_course_frame, textvariable=self.var_jobtitle, font=("times new roman", 13, "bold"), width=20, state="read only")
        job_title_combo["values"] = ("Select Job Title", "Software Engineer", "HR Manager", "Sales Executive", "Marketing Specialist","Team Lead","Other")
        job_title_combo.current(0)
        job_title_combo.grid(row=0, column=3, padx=2, pady=10, sticky="W")

        # Year
        employee_type_label = Label(current_course_frame, text="Employee Type", font=("times new roman", 13, "bold"), bg="white")
        employee_type_label.grid(row=1, column=0, padx=10, sticky="W")

        employee_type_combo = ttk.Combobox(current_course_frame, textvariable=self.var_emp_type, font=("times new roman", 13, "bold"), width=20, state="read only")
        employee_type_combo["values"] = ("Select Type", "Full-Time", "Part-Time", "Contract", "Intern")
        employee_type_combo.current(0)
        employee_type_combo.grid(row=1, column=1, padx=2, pady=10, sticky="W")

        # Semester
        work_location_label = Label(current_course_frame, text="Work Location", font=("times new roman", 13, "bold"), bg="white")
        work_location_label.grid(row=1, column=2, padx=10, sticky="W")

        work_location_combo = ttk.Combobox(current_course_frame, textvariable=self.var_work_loc, font=("times new roman", 13, "bold"), width=20, state="read only")
        work_location_combo["values"] = ("Select Location", "Headquarters", "Remote","Branch Office 1","Branch Office 2","Client Site")
        work_location_combo.current(0)
        work_location_combo.grid(row=1, column=3, padx=2, pady=10, sticky="W")

        # Student Information
        Employee_Deatils_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Employee Deatils", font=("times new roman", 12, "bold"))
        Employee_Deatils_frame.place(x=5, y=250, width=720, height=300)

        # Student ID
        emp_id_label = Label(Employee_Deatils_frame, text="Employee ID", font=("times new roman", 13, "bold"), bg="white")
        emp_id_label.grid(row=0, column=0, padx=10,pady=5, sticky="W")

        emp_id_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_employee_id, font=("times new roman", 13, "bold"), width=20)
        emp_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

        # Student Name
        name_label = Label(Employee_Deatils_frame, text="Employee Name", font=("times new roman", 13, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10,pady=5, sticky="W")

        name_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_Emp_name, font=("times new roman", 13, "bold"), width=20)
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky="W")

        # Class Division
        div_label = Label(Employee_Deatils_frame, text="Work Shift", font=("times new roman", 13, "bold"), bg="white")
        div_label.grid(row=1, column=0, padx=10,pady=5, sticky="W")


        shift_combo = ttk.Combobox(Employee_Deatils_frame, textvariable=self.var_Work_shift, font=("times new roman", 13, "bold"), width=18, state="read only")
        shift_combo["values"] = ("Select Shift","Morning Shift","Evening Shift","Night Shift")
        shift_combo.current(0)
        shift_combo.grid(row=1, column=1, padx=10, pady=5, sticky="W")


        # Roll Number
        roll_label = Label(Employee_Deatils_frame, text="Salary", font=("times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=1, column=2, padx=10,pady=5, sticky="W")

        roll_entry = ttk.Entry(Employee_Deatils_frame,textvariable=self.var_Salary, font=("times new roman", 13, "bold"), width=20)
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky="W")

        # Gender (Radio Buttons)
        roll_label = Label(Employee_Deatils_frame, text="Gender", font=("times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=2, column=0, padx=10,pady=5, sticky="W")

        gender_combo = ttk.Combobox(Employee_Deatils_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width=18, state="read only")
        gender_combo["values"] = ("Select Gender","Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky="W")


        # Date of Birth (DOB)
        dob_label = Label(Employee_Deatils_frame, text="Date of Birth", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10,pady=5, sticky="W") 

        dob_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_dob, font=("times new roman", 13, "bold"), width=20)
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky="W")

        # Email
        email_label = Label(Employee_Deatils_frame, text="Email", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10,pady=5, sticky="W")

        email_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_email, font=("times new roman", 13, "bold"), width=20)
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        # Phone Number
        phone_label = Label(Employee_Deatils_frame, text="Phone No.", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10,pady=5, sticky="W")

        phone_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_phone, font=("times new roman", 13, "bold"), width=20)
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky="W")

        # Address
        address_label = Label(Employee_Deatils_frame, text="Address", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10,pady=5, sticky="W")

        address_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_address, font=("times new roman", 13, "bold"), width=20)
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky="W")

        # Teacher Name
        teacher_label = Label(Employee_Deatils_frame, text="Qualification", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10,pady=5, sticky="W")

        teacher_entry = ttk.Entry(Employee_Deatils_frame, textvariable=self.var_Qualify, font=("times new roman", 13, "bold"), width=20)
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky="W")

        # radio Button
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(Employee_Deatils_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=5,sticky="W")
        
        self.var_radio2= StringVar()
        radiobtn2=ttk.Radiobutton(Employee_Deatils_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1,padx=10,pady=5,sticky="W")


        # Button frame
        btn_frame = Frame(Employee_Deatils_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Update
        Update_btn = Button(btn_frame,command=self.update_data, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)
    

        # Delete
        Delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)

        # Reset
        Reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)

        # Second Button
        btn_frame1 = Frame(Employee_Deatils_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=245, width=715, height=30)

        Take_Photo_btn = Button(btn_frame1, command=self.generate_dataset,text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Take_Photo_btn.grid(row=1, column=0)

        # Update photo button 
        Update_Photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Update_Photo_btn.grid(row=1, column=1)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Database", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Right_frame.place(x=750, y=10, width=730, height=580)

        # Right label image
        img_Right = Image.open(r"Collage_image\group1.jpg")
        img_Right = img_Right.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        # Display the image in a label inside the right frame
        Right_bg_label = Label(Right_frame, image=self.photoimg_Right)
        Right_bg_label.place(x=5, y=0, width=720, height=130)

        #============Search System===========
        Search_frame = LabelFrame(Right_frame, bd=2, bg="White", relief=RIDGE, text=" Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        Search_label = Label(Search_frame, text="Search By: ", font=("times new roman", 13, "bold"), bg="red", fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")
        
        Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), width=15, state="read only")
        Search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky="W")

        Search_entry = ttk.Entry(Search_frame, font=("times new roman", 13, "bold"), width=15)
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky="W")

        # Button in Search frame
        Search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=3, padx=4)

        ShowAll_btn = Button(Search_frame, text="ShowAll", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=4, padx=4)

        #=========================Table Frame===============
        table_frame = Frame(Right_frame, bd=2, bg="White", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Employee_table = ttk.Treeview(
            table_frame,
            columns=(
                "Dep", "Jobtitle", "emp_type", "work_loc", "id", "name",
                "Work_shift", "Salary", "gender", "dob", "email", "phone",
                "address", "Qualify", "photo"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill="x")
        scroll_y.pack(side=RIGHT, fill="y")
        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)

        # Adding column headings
        self.Employee_table.heading("Dep", text="Department")
        self.Employee_table.heading("Jobtitle", text="Job Title")
        self.Employee_table.heading("emp_type", text="Employee Type")
        self.Employee_table.heading("work_loc", text="Work Location")
        self.Employee_table.heading("id", text="Employee ID")
        self.Employee_table.heading("name", text="Name")
        self.Employee_table.heading("Work_shift", text="Work Shift")
        self.Employee_table.heading("Salary", text="Salary")
        self.Employee_table.heading("gender", text="Gender")
        self.Employee_table.heading("dob", text="Date of Birth")
        self.Employee_table.heading("email", text="Email")
        self.Employee_table.heading("phone", text="Phone Number")
        self.Employee_table.heading("address", text="Address")
        self.Employee_table.heading("Qualify", text="Qualification")
        self.Employee_table.heading("photo", text="Photo Sample Status")

        self.Employee_table["show"] = "headings"

        # Setting column widths
        self.Employee_table.column("Dep", width=100)
        self.Employee_table.column("Jobtitle", width=100)
        self.Employee_table.column("emp_type", width=100)
        self.Employee_table.column("work_loc", width=100)
        self.Employee_table.column("id", width=100)
        self.Employee_table.column("name", width=100)
        self.Employee_table.column("Work_shift", width=100)
        self.Employee_table.column("Salary", width=100)
        self.Employee_table.column("gender", width=100)
        self.Employee_table.column("dob", width=100)
        self.Employee_table.column("email", width=100)
        self.Employee_table.column("phone", width=100)
        self.Employee_table.column("address", width=100)
        self.Employee_table.column("Qualify", width=100)
        self.Employee_table.column("photo", width=150)

        self.Employee_table.pack(fill=BOTH, expand=1)
        self.Employee_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    #=============================Function Declaration================================
    
    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_jobtitle.get()=="Select Department" or self.var_Emp_name.get()=="" or self.var_employee_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password = "12@02",database="face_iris_attendence" )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_jobtitle.get(),
                                                                                                            self.var_emp_type.get(),
                                                                                                            self.var_work_loc.get(),
                                                                                                            self.var_employee_id.get(),
                                                                                                            self.var_Emp_name.get(),
                                                                                                            self.var_Work_shift.get(),
                                                                                                            self.var_Salary.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_Qualify.get(),
                                                                                                            self.var_radio1.get()
                                                                                                        
                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added Successfully",parent = self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #==========================fetech data==============================
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="12@02",
                database="face_iris_attendence"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM employee")  # Ensure table name is correct
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Employee_table.delete(*self.Employee_table.get_children())
                for record in data:
                    self.Employee_table.insert("", "end", values=record)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No records found in the database.", parent=self.root)

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)






    #==================get cursor=========================================
    def get_cursor(self, event=""):
        try:
            # Get the currently selected row
            cursor_focus = self.Employee_table.focus()
            content = self.Employee_table.item(cursor_focus)
            data = content["values"]  # Extract the data from the selected row

            # Check if data exists
            if data:
                self.var_dep.set(data[0])
                self.var_jobtitle.set(data[1])
                self.var_emp_type.set(data[2])
                self.var_work_loc.set(data[3])
                self.var_employee_id.set(data[4])
                self.var_Emp_name.set(data[5])
                self.var_Work_shift.set(data[6])
                self.var_Salary.set(data[7])
                self.var_gender.set(data[8])
                self.var_dob.set(data[9])
                self.var_email.set(data[10])
                self.var_phone.set(data[11])
                self.var_address.set(data[12])
                self.var_Qualify.set(data[13])
            else:
                # Handle empty selection
                messagebox.showinfo("Info", "No record selected.", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)


    #UPDATE FUNCTION====================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_jobtitle.get()=="Select Department" or self.var_Emp_name.get()=="" or self.var_employee_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this employee details",parent=self.root)
                if Update >0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12@02", database="face_iris_attendence")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employee set Dep=%s, jobtitle=%s,emp_type=%s, work_loc=%s,Emp_name=%s, Work_shift=%s, Salary=%s, Gender=%s,Dob=%s,Email=%s, Phone=%s, Address=%s, Qualify=%s, PhotoSample=%s where employee_id=%s",(

                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_jobtitle.get(),
                                                                                                                                                                                self.var_emp_type.get(),
                                                                                                                                                                                self.var_work_loc.get(),
                                                                                                                                                                                self.var_Emp_name.get(),
                                                                                                                                                                                self.var_Work_shift.get(),
                                                                                                                                                                                self.var_Salary.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_Qualify.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_employee_id.get()
                                                                                                                                                                            ))
            
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Employee details sccessfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #DELETE FUNCTION==================================================================
    def delete_data(self):
        if self.var_employee_id.get()=="":
            messagebox.showerror("Error","Employee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Details Delete","Are you sure you want to delete this employee details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12@02", database="face_iris_attendence")
                    my_cursor = conn.cursor()
                    sql="DELETE FROM employee WHERE employee_id=%s"
                    val=(self.var_employee_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted employee details",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #RESET FUNCTION==================================================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_jobtitle.set("Select Job Title")
        self.var_emp_type.set("Select Type")
        self.var_work_loc.set("Select location")
        self.var_employee_id.set("")
        self.var_Emp_name.set("")
        self.var_Work_shift.set("Select shift")
        self.var_Salary.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_Qualify.set("")
        self.var_radio1.set("")

    #==================GENERATE Data Set or Take  Photo Samples==================================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_jobtitle.get() == "Select Job Title" or self.var_Emp_name.get() == "" or self.var_employee_id.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="12@02", database="face_iris_attendence")
                my_cursor = conn.cursor()

                # Insert or update student data
                my_cursor.execute("SELECT * FROM employee WHERE  employee_id=%s", (self.var_employee_id.get(),))
                result = my_cursor.fetchall()
                if len(result) == 0:
                    # Insert new student record
                    my_cursor.execute(
                        "INSERT INTO employee (Dep, jobtitle , emp_type, work_loc, employee_id,Emp_name , Work_shift, Salary, Gender, Dob, Email, Phone, Address, Qualify, PhotoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_dep.get(),
                            self.var_jobtitle.get(),
                            self.var_emp_type.get(),
                            self.var_work_loc.get(),
                            self.var_employee_id.get(),
                            self.var_Emp_name.get(),
                            self.var_Work_shift.get(),
                            self.var_Salary.get(),                      
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_Qualify.get(),
                            "Yes",
                        ),
                    )
                else:
                    # Update existing student record
                    my_cursor.execute(
                        "UPDATE employee SET Dep=%s, jobtitle=%s, emp_type=%s, work_loc=%s, Emp_name =%s, Work_shift=%s, Salary=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Qualify=%s, PhotoSample=%s WHERE employee_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_jobtitle.get(),
                            self.var_emp_type.get(),
                            self.var_work_loc.get(),
                            self.var_Emp_name.get(),
                            self.var_Work_shift.get(),
                            self.var_Salary.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_Qualify.get(),
                            "Yes",
                            self.var_employee_id.get(),
                        ),
                    )

                conn.commit()
                conn.close()

                # Set up OpenCV for face capture
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped
                    return None

                cap = cv2.VideoCapture(0  )
                img_id = 0

                if not cap.isOpened():
                    messagebox.showerror("Error", "Camera not detected. Please check your device.", parent=self.root)
                    return

                # Ensure data directory exists
                if not os.path.exists("data"):
                    os.makedirs("data")

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    cropped_face = face_cropped(frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"data/user.{self.var_employee_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", f"Dataset generated successfully for Student ID: {self.var_employee_id.get()}", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
