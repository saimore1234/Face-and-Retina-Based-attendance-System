from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root 
        self.root.title("Register")

         # Dynamically set to screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        #======================Variables-------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #===============Background Image=============================
        bg_img = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\b11.jpg")
        bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #=========================Left Image
       # Constants for layout
        LEFT_IMG_WIDTH = 470
        LEFT_IMG_HEIGHT = 550
        LEFT_IMG_X = 50
        LEFT_IMG_Y = 100  # Center vertically

        # Load and resize the left image
        left_img = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\r.jpg")
        left_img = left_img.resize((LEFT_IMG_WIDTH, LEFT_IMG_HEIGHT), Image.Resampling.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(left_img)

        # Place the image
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=LEFT_IMG_X, y=LEFT_IMG_Y, width=LEFT_IMG_WIDTH, height=LEFT_IMG_HEIGHT)
#===================MAin Frame=====================
        frame = Frame(self.root,bg="white")
        frame.place(x=520,y= 100 ,height=550,width=800)

        register_lbl = Label(frame,text = "REGISTER HERE",font = ("Times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

#================LAbels and Entry fields=====================================
        fname = Label(frame,text="First Name",font = ("Times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font = ("Times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)


        l_name = Label(frame,text="Last Name",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font = ("Times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #=============row 2
        contact = Label(frame,text="Contact No",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font = ("Times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text="Email id",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font = ("Times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #======row 3
        security_Q = Label(frame,text="Select Security Question",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font = ("Times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your First Pet Name","Your Birth Place","Your bestfriend Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
       


        security_A = Label(frame,text="Security Answer",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA,font = ("Times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #-=====row 4

        pswd= Label(frame,text="Password ",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font = ("Times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd = Label(frame,text="Confirm Password",font = ("Times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font = ("Times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #========================Check Button==============================
        
        self.var_check = IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Conditions",font=("times new roman",12),bg="white",fg="black",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #+++++++++++++++++++++++Buttond

        img = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\register.png")
        img = img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)    

        
        img1 = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\login.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=420,width=300)


    #=======================Function Dlecaration=================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please Agree all terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12@02",database="face_iris_attendence")
            mycursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist with this email",parent=self.root)
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                     ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully",parent=self.root)







        
        






if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
