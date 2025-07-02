# main.py

import tkinter as tk
from tkinter import messagebox
import face_recognition
import cv2
import os

# Face verify function
def verify_face():
    try:
        # Known image load karo
        known_image = face_recognition.load_image_file("known_faces/shreyansh.jpg")
        known_encoding = face_recognition.face_encodings(known_image)[0]
    except:
        messagebox.showerror("Error", "Known face not found. Please capture your face first.")
        return False

    # Webcam se image lo
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        messagebox.showerror("Error", "Webcam access failed")
        return False

    # Resize karke recognition karo
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        if True in matches:
            return True

    return False

# Vault kholne ka GUI
def open_vault():
    vault_window = tk.Toplevel()
    vault_window.title("PDF Vault")
    vault_window.geometry("400x300")
    vault_window.configure(bg="black")

    tk.Label(vault_window, text="Welcome to your Vault!", font=("Arial", 16), fg="white", bg="black").pack(pady=20)

    # TODO: Upload / View / Delete PDF buttons yahan aayenge
    tk.Button(vault_window, text="Close Vault", command=vault_window.destroy).pack(pady=10)

# Login button ke liye action
def login():
    result = verify_face()
    if result:
        messagebox.showinfo("Access Granted", "Face recognized. Welcome!")
        open_vault()
    else:
        messagebox.showerror("Access Denied", "Face not matched. Try again.")

# GUI start
root = tk.Tk()
root.title("Secure PDF Vault")
root.geometry("300x200")
root.configure(bg="black")

tk.Label(root, text="Login with Face", font=("Arial", 14), fg="white", bg="black").pack(pady=30)
tk.Button(root, text="Unlock Vault", command=login).pack(pady=10)

root.mainloop()
