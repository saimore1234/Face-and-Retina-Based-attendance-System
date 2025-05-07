# Face-and-Retina-Based-attendance-System
In This repository simple pyhton code project are there and it made by using ML and DL algorithm
# 🎓 Face and Retina-Based Attendance System

## 📖 Introduction

The *Face and Retina-Based Attendance System* is an intelligent, Python-based desktop application that automates the process of attendance using two biometric features — *Facial Recognition* and *Iris (Retina) Detection*. The system is developed as a final-year engineering project and leverages computer vision techniques via OpenCV and an interactive GUI using Tkinter.

This hybrid system improves upon traditional and biometric-only attendance methods by incorporating both face and iris recognition to increase security and reliability. The project can work with a *mobile phone camera* (via IP Webcam or Camo app), enabling greater flexibility and cost-effectiveness.

---

## ✨ Key Features

- 🧑‍🏫 *Dual Biometric Authentication*: Uses both face and iris to ensure accurate identity verification.
- 📷 *Live Camera Support*: Connects with phone camera streams for real-time recognition.
- 📊 *Attendance Logging*: Marks and stores attendance entries in a structured CSV file.
- 🖥 *Fullscreen Tkinter GUI*: Interactive and visually appealing interface for ease of use.
- 📁 *Dataset Collection*: Allows new users to capture and store their face and iris data.
- ⏰ *Live Clock Dashboard*: Embedded clock on the main screen for real-time display.
- 🔐 *Offline Access*: Entirely offline system — no internet required.

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core Programming |
| OpenCV     | Face and Iris Detection & Recognition |
| Tkinter    | GUI Design |
| NumPy      | Image Array Manipulation |
| Pandas     | CSV File Handling |
| Camo/IP Webcam | Mobile Camera Integration |

---

## 📁 Project Structure

```plaintext
Face-Retina-Attendance-System/
│
├── main.py                  # Main GUI launcher
├── face_recognition.py      # Face detection & matching
├── iris_recognition.py      # Iris detection & matching
├── capture_dataset.py       # Module to capture & save datasets
├── attendance.csv           # Attendance record file
├── dataset/
│   ├── Person1/
│   ├── Person2/
│   └── ...
├── images/                  # GUI assets (icons, backgrounds)
├── utils/
│   ├── preprocessor.py
│   └── helpers.py
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
🚀 How to Run
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Face-Retina-Attendance-System.git
cd Face-Retina-Attendance-System
2️⃣ Install Required Libraries
Install all dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Setup Mobile Camera
Use the IP Webcam Android app or Camo app.

Note the stream URL (e.g., http://192.168.x.x:8080/video) and replace it in the code wherever needed.

4️⃣ Run the Application
bash
Copy
Edit
python main.py
📷 Sample Screenshots
Add screenshots in this section for better GitHub presentation.

Example:

Dashboard layout

Face and iris capture window

Attendance log preview

📊 Output
Attendance is stored in attendance.csv in the following format:

csv
Copy
Edit
Name, Date, Time, Authentication Type
John Doe, 2025-04-30, 10:21:45, Face+Iris
✅ Use Case Scenarios
Educational Institutions: Classroom attendance automation.

Offices & Labs: Secure employee check-in system.

Secure Access Systems: Enhanced identity verification.

🔮 Future Scope
📲 Add user login/signup system with admin control.

☁ Migrate attendance records to cloud (Firebase/MySQL).

🎛 Add voice feedback or alert system.

📱 Create a mobile companion app.

🙋 Author
Your Name
Final Year Computer Engineering Student
📍 India
🔗 GitHub Profile
✉ your.email@example.com

📄 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution.

🙏 Acknowledgements
OpenCV Community

Python Software Foundation

Inspiration from real-world biometric systems

vbnet
Copy
Edit

---

### ✅ Next Steps:

- Replace **yourusername**, **Your Name**, and **your.email@example.com** with your actual details.
- Add sample screenshots to the GitHub repo and link them under the "Screenshots" section.
- (Optional) Create a LICENSE file in the root directory with the MIT License text.

Would you like me to generate the requirements.txt as well?
