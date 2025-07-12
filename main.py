# main.py

import tkinter as tk
from tkinter import messagebox
import face_recognition
import cv2
import os

# yeh function face verify karta hai webcam se
def verify_face():
    try:
        # stored face image ko load karte hain
        known_image = face_recognition.load_image_file("known_faces/shreyansh_fixed.jpg")
        known_encoding = face_recognition.face_encodings(known_image)[0]
    except:
        messagebox.showerror("Error", "Face image nahi mila. Pehle face capture karo.")
        return False

    # webcam se ek frame lete hain
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        messagebox.showerror("Error", "Webcam ka access nahi mila.")
        return False

    # frame ko chhota karke RGB mein convert karte hain
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # webcam frame se face encoding nikalte hain
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        if True in matches:
            return True

    return False

# agar face match hota hai, toh vault ka GUI open hota hai
def open_vault():
    vault_window = tk.Toplevel()
    vault_window.title("PDF Vault")
    vault_window.geometry("400x300")
    vault_window.configure(bg="black")

    tk.Label(
        vault_window,
        text="Welcome to your Vault!",
        font=("Segoe UI", 16, "bold"),
        fg="white",
        bg="black"
    ).pack(pady=40)

    # aage chal kar yahan Upload, View, Delete buttons add karenge
    tk.Button(
        vault_window,
        text="Close Vault",
        font=("Segoe UI", 12),
        command=vault_window.destroy,
        bg="gray20",
        fg="white",
        padx=10,
        pady=5
    ).pack(pady=10)

# jab user "Unlock Vault" dabata hai
def login():
    result = verify_face()
    if result:
        messagebox.showinfo("Access Granted", "Face match ho gaya. Vault khul raha hai.")
        open_vault()
    else:
        messagebox.showerror("Access Denied", "Face match nahi hua. Phir se try karo.")

# main login window
root = tk.Tk()
root.title("Secure PDF Vault")
root.geometry("300x200")
root.configure(bg="black")

tk.Label(
    root,
    text="Login with Face",
    font=("Segoe UI", 14, "bold"),
    fg="white",
    bg="black"
).pack(pady=30)

tk.Button(
    root,
    text="Unlock Vault",
    font=("Segoe UI", 12),
    command=login,
    bg="gray20",
    fg="white",
    padx=10,
    pady=5
).pack(pady=10)

root.mainloop()
