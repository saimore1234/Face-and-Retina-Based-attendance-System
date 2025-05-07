import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import hashlib
import os

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def toggle_login_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="👁️")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="🙈")

def login():
    email = username_entry.get().strip()
    pwd = password_entry.get().strip()

    if not (email and pwd):
        messagebox.showerror("Error", "Please enter all fields")
        return

    hashed = hash_password(pwd)

    if not os.path.exists("users.txt"):
        messagebox.showerror("Error", "No users registered")
        return

    with open("users.txt", "r") as f:
        for line in f:
            data = line.strip().split(',')
            if email == data[2] and hashed == data[4]:
                messagebox.showinfo("Login Success", f"Welcome {data[0]}!")
                root.destroy()
                subprocess.Popen(["python", "main.py"])
                return

    messagebox.showerror("Login Failed", "Invalid email or password")

def open_signup():
    root.destroy()
    subprocess.Popen(["python", "signup.py"])

# GUI Setup
root = tk.Tk()
root.title("Login Page")
root.state("zoomed")

# Background Image
bg = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\b11.jpg")
bg = bg.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_img = ImageTk.PhotoImage(bg)
tk.Label(root, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)

# Logo
logo = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\r.jpg")
logo = logo.resize((120, 120), Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(logo)
tk.Label(root, image=logo_img, bg="white").place(x=50, y=50)

# Login Frame
frame = tk.Frame(root, bg="white", bd=3)
frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)

tk.Label(frame, text="Login", font=("Helvetica", 24, "bold"), bg="white").pack(pady=20)

tk.Label(frame, text="Email ID", font=("Arial", 12), bg="white").pack(anchor='w', padx=30, pady=(10,0))
username_entry = tk.Entry(frame, font=("Arial", 12), width=30)
username_entry.pack(padx=30, pady=5)

tk.Label(frame, text="Password", font=("Arial", 12), bg="white").pack(anchor='w', padx=30, pady=(10,0))
password_entry = tk.Entry(frame, font=("Arial", 12), width=30, show="*")
password_entry.pack(padx=30, pady=5)

# Toggle Password Button
toggle_btn = tk.Button(frame, text="👁️", command=toggle_login_password, bg="white", bd=0)
toggle_btn.place(relx=0.86, rely=0.48)

# Login Button
tk.Button(frame, text="Login", command=login, font=("Arial", 14), bg="#27ae60", fg="white", width=20).pack(pady=20)

# Sign Up
tk.Label(frame, text="Don't have an account?", bg="white", font=("Arial", 10)).pack()
tk.Button(frame, text="Sign Up", command=open_signup, bg="#2980b9", fg="white", width=15).pack(pady=5)

root.mainloop()
