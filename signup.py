import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import hashlib, random, smtplib, os
import subprocess

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

otp_sent = ""

def send_otp():
    global otp_sent
    otp_sent = str(random.randint(100000, 999999))
    try:
        sender = 'sahidesh02@gmail.com'  # your email here
        app_password = 'absrgmcukmcpcknp'  # your app password here
        receiver = email_entry.get().strip()

        if not receiver:
            messagebox.showerror("Missing Email", "Please enter your email before requesting OTP.")
            return

        message = f'Subject: OTP Verification\n\nYour OTP is: {otp_sent}'

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.sendmail(sender, receiver, message)

        messagebox.showinfo("OTP Sent", f"OTP has been sent to {receiver}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send OTP: {e}")

def register():
    name = name_entry.get().strip()
    lname = lname_entry.get().strip()
    email = email_entry.get().strip()
    mobile = mobile_entry.get().strip()
    password = pass_entry.get().strip()
    confirm = confirm_entry.get().strip()
    otp_input = otp_entry.get().strip()

    if not otp_input:
        messagebox.showwarning("Missing OTP", "Please enter the OTP received via email.")
        return

    if otp_input != otp_sent:
        messagebox.showerror("Invalid OTP", "The entered OTP is incorrect.")
        return

    if not password or not confirm:
        messagebox.showerror("Error", "Password fields cannot be empty.")
        return

    if password != confirm:
        messagebox.showerror("Mismatch", "Password and Confirm Password do not match.")
        return

    hashed_pass = hash_password(password)

    with open("users.txt", "a") as f:
        f.write(f"{name},{lname},{email},{mobile},{hashed_pass}\n")

    messagebox.showinfo("Success", "Registered Successfully!")
    window.destroy()
    subprocess.Popen(["python", "Login.py"])

# ---------- GUI START ----------
window = tk.Tk()
window.title("Sign Up")
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

bg_img = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\b11.jpg")  # Replace with actual background
bg_img = bg_img.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
bg_photo = ImageTk.PhotoImage(bg_img)

tk.Label(window, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="white", bd=10)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(frame, text="Create New Account", font=("Arial", 20, "bold"), bg="white", fg="green")
title.grid(row=0, column=0, columnspan=2, pady=20)

fields = [
    ("First Name", "name_entry"),
    ("Last Name", "lname_entry"),
    ("Email", "email_entry"),
    ("Mobile Number", "mobile_entry"),
    ("Password", "pass_entry"),
    ("Confirm Password", "confirm_entry"),
    ("Enter OTP", "otp_entry")
]

entries = {}

for idx, (label_text, var_name) in enumerate(fields):
    tk.Label(frame, text=label_text, font=("Arial", 14), bg="white").grid(row=idx+1, column=0, padx=20, pady=10, sticky="e")
    entry = tk.Entry(frame, font=("Arial", 14), show="*" if "Password" in label_text and "Confirm" not in label_text else "")
    entry.grid(row=idx+1, column=1, padx=20, pady=10)
    entries[var_name] = entry

name_entry = entries["name_entry"]
lname_entry = entries["lname_entry"]
email_entry = entries["email_entry"]
mobile_entry = entries["mobile_entry"]
pass_entry = entries["pass_entry"]
confirm_entry = entries["confirm_entry"]
otp_entry = entries["otp_entry"]

btn_frame = tk.Frame(frame, bg="white")
btn_frame.grid(row=len(fields)+2, column=0, columnspan=2, pady=20)

tk.Button(btn_frame, text="Send OTP", command=send_otp, font=("Arial", 12), bg="orange", width=15).grid(row=0, column=0, padx=20)
tk.Button(btn_frame, text="Register", command=register, font=("Arial", 12), bg="green", fg="white", width=15).grid(row=0, column=1, padx=20)

window.mainloop()
