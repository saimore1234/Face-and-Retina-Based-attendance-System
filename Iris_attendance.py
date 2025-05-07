from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import time
import os
import cv2
import csv
from datetime import datetime
import threading

# ======================
# HELPER FUNCTIONS
# ======================
def get_employee_name():
    """Get employee name/ID through dialog box"""
    name = simpledialog.askstring("Employee ID", "Enter employee name or ID:")
    return name.strip() if name else None

def initialize_attendance_file():
    """Create attendance CSV file if it doesn't exist"""
    if not os.path.exists("iris_attendance.csv"):
        with open("iris_attendance.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Timestamp"])

# ======================
# CORE FUNCTIONALITY
# ======================
def match_iris_and_mark_attendance():
    """Main attendance marking function"""
    print("[INFO] Starting live iris matching...")
    initialize_attendance_file()
    
    orb = cv2.ORB_create()
    dataset_path = "iris_data"
    
    if not os.path.exists(dataset_path):
        messagebox.showerror("Error", "Dataset folder 'iris_data/' not found!")
        return
    
    data = {}
    for person in os.listdir(dataset_path):
        person_dir = os.path.join(dataset_path, person)
        descriptors = []
        for img_file in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_file)
            img = cv2.imread(img_path, 0)
            if img is None:
                continue
            kp, des = orb.detectAndCompute(img, None)
            if des is not None:
                descriptors.append(des)
        if descriptors:
            data[person] = descriptors
    
    if not data:
        messagebox.showerror("Error", "No valid iris data loaded!")
        return
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open camera!")
        return
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    marked = set()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            kp_frame, des_frame = orb.detectAndCompute(gray, None)
            
            if des_frame is not None:
                for person, descriptors in data.items():
                    for des in descriptors:
                        matches = bf.match(des, des_frame)
                        matches = sorted(matches, key=lambda x: x.distance)
                        good_matches = [m for m in matches if m.distance < 50]
                        
                        if len(good_matches) > 5 and person not in marked:
                            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            try:
                                with open("iris_attendance.csv", "a", newline="") as f:
                                    writer = csv.writer(f)
                                    writer.writerow([person, now])
                                marked.add(person)
                                print(f"[ATTENDANCE] {person} marked present at {now}")
                                cv2.putText(frame, f"Marked: {person}", (50, 50),
                                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            except Exception as e:
                                print(f"[ERROR] CSV write failed: {e}")
            
            cv2.imshow("Iris Attendance System", frame)
            key = cv2.waitKey(1)
            if key == 27:  # ESC key
                break
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

def register_new_iris():
    """Function to register new iris patterns"""
    name = get_employee_name()
    if not name:
        print("Name input cancelled.")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open camera!")
        return

    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    save_dir = f"iris_data/{name}"
    os.makedirs(save_dir, exist_ok=True)
    count = len(os.listdir(save_dir))

    print("[INFO] Press 's' to save iris images, 'ESC' to quit.")
    key = None  # Initialize key variable

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        for (ex, ey, ew, eh) in eyes[:1]:  # Process only first detected eye
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
            iris = frame[ey:ey+eh, ex:ex+ew]
            iris_resized = cv2.resize(iris, (100, 100))
            cv2.imshow("Iris Crop", iris_resized)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                count += 1
                img_path = os.path.join(save_dir, f"iris{count}.png")
                cv2.imwrite(img_path, iris_resized)
                print(f"[SAVED] {img_path}")
            elif key == 27:
                break

        cv2.imshow("Iris Registration", frame)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# ======================
# GUI FUNCTIONS
# ======================
def open_iris_system():
    """Handle iris system menu choice"""
    choice = simpledialog.askstring("Iris System", 
                                   "Enter:\n1. Register new iris\n2. Mark attendance")
    
    if choice == '1':
        register_new_iris()
    elif choice == '2':
        thread = threading.Thread(target=match_iris_and_mark_attendance)
        thread.daemon = True
        thread.start()
    else:
        print("Invalid choice or operation cancelled")

def open_employee_data():
    print("Employee Data opened")

def open_attendance_system():
    print("Attendance System opened")

def open_retina_system():
    print("Retina System launched")

def open_train_iris():
    print("Train Iris started")

def open_photos_data():
    os.startfile("data")

def open_developer_info():
    print("Developer Info displayed")

def exit_app():
    root.destroy()

# ======================
# GUI SETUP
# ======================
root = Tk()
root.title("Iris Recognition Attendance System")
root.state('zoomed')

# Top Image Banner
try:
    top_img = Image.open(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/Screenshot 2025-01-18 052535.png")
    top_img = top_img.resize((root.winfo_screenwidth(), 100))
    top_photo = ImageTk.PhotoImage(top_img)
    top_lbl = Label(root, image=top_photo)
    top_lbl.place(x=0, y=0, relwidth=1)
except Exception as e:
    print(f"Error loading banner image: {e}")

# Clock + Title
clock_lbl = Label(root, font=("times new roman", 20, "bold"), bg="white", fg="black")
clock_lbl.place(x=20, y=105)

def update_time():
    clock_lbl.config(text=time.strftime('%I:%M:%S %p'))
    clock_lbl.after(1000, update_time)

update_time()

title_lbl = Label(root, text="IRIS RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                 font=("times new roman", 28, "bold"), fg="red", bg="white")
title_lbl.place(relx=0.5, y=105, anchor="n")

# Background
try:
    bg_img = Image.open(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/assets/background.jpeg")
    bg_img = bg_img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_lbl = Label(root, image=bg_photo)
    bg_lbl.place(x=0, y=150, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")

# Icon Buttons Frame
icon_frame = Frame(root, bg="black")
icon_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

def create_icon(image_path, text, row, col, command):
    """Helper to create uniform icon buttons"""
    try:
        img = Image.open(image_path).resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        btn = Button(icon_frame, image=photo, command=command, cursor="hand2", bd=0)
        btn.image = photo
        btn.grid(row=row*2, column=col, padx=30, pady=(10, 0))
        
        lbl = Label(icon_frame, text=text, font=("times new roman", 14, "bold"), 
                   bg="blue", fg="white", width=17)
        lbl.grid(row=row*2 + 1, column=col, pady=(0, 20))
    except Exception as e:
        print(f"Error creating icon {text}: {e}")

# Top Row Icons
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/images.png", 
            "Employee Details", 0, 0, open_employee_data)
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/assets/iris.png", 
            "Iris System", 0, 1, open_iris_system)
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/attendance.jpg", 
            "Attendance System", 0, 2, open_attendance_system)
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/assets/retina.png", 
            "Retina System", 0, 3, open_retina_system)

# Bottom Row Icons
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/assets/train.png", 
            "Train Iris", 1, 0, open_train_iris)
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/assets/photos.png", 
            "Photos Data", 1, 1, open_photos_data)
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/assets/dev.png", 
            "Developer", 1, 2, open_developer_info)
create_icon(r"C:/Users/SAHIL DESHMUKH.SAHIL/Desktop/FaceRecognition System/Collage_image/Exit.png", 
            "Exit", 1, 3, exit_app)

root.mainloop()