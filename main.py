# main.py (Updated with model initialization)
# Yeh file ab application ka logic aur setup sambhalegi.

import tkinter as tk
from tkinter import messagebox
from deepface import DeepFace
import cv2
import os
import time
from ui import create_login_window, open_vault_window # UI functions ko import karein

# --- Configuration ---
KNOWN_FACE_PATH = "known_faces/user_face.jpg"
MODEL_NAME = "VGG-Face"

def initialize_model():
    """
    Application start hone par face recognition model ko load aur setup karta hai.
    Yeh function pehli baar chalne par model download karega.
    """
    try:
        # Ek dummy/temporary root window banayein taaki messagebox dikh sake
        root = tk.Tk()
        root.withdraw() # Is window ko screen par na dikhayein

        messagebox.showinfo("Setup", "Pehli baar setup ho raha hai. Face recognition model download hoga. Kripya intezaar karein...")
        
        print(f"'{MODEL_NAME}' model ko load kiya ja raha hai...")
        DeepFace.build_model(MODEL_NAME)
        print("Model safaltapoorvak load ho gaya hai.")
        
        messagebox.showinfo("Setup Complete", "Setup poora ho gaya hai. Application ab shuru hogi.")
        root.destroy() # Temporary window ko band kar dein
        return True

    except Exception as e:
        messagebox.showerror("Model Error", f"Model download ya load nahi ho paaya. Kripya apna internet connection check karein.\nError: {e}")
        root.destroy()
        return False


def capture_and_verify_face():
    """Webcam se frame capture karke known face se verify karein."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Webcam nahi khul pa raha hai.")
        return False

    time.sleep(2)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if not ret:
        messagebox.showerror("Error", "Webcam se frame capture nahi ho paaya.")
        return False

    temp_face_path = "known_faces/temp_face.jpg"
    cv2.imwrite(temp_face_path, frame)

    try:
        result = DeepFace.verify(
            img1_path=KNOWN_FACE_PATH,
            img2_path=temp_face_path,
            model_name=MODEL_NAME,
            enforce_detection=True
        )
        if os.path.exists(temp_face_path):
            os.remove(temp_face_path)
        return result['verified']
    except ValueError:
        # Yeh error tab aata hai jab chehra detect nahi hota
        messagebox.showerror("Verification Error", "Chehra theek se detect nahi hua. Kripya saaf roshni mein seedhe camera ki taraf dekhein.")
        if os.path.exists(temp_face_path):
            os.remove(temp_face_path)
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Ek anjaan error aayi hai: {e}")
        if os.path.exists(temp_face_path):
            os.remove(temp_face_path)
        return False


def login(root_window, status_label):
    """
    Login process ko handle karein. Yeh function UI ko pass kiya jaata hai.
    """
    if not os.path.exists(KNOWN_FACE_PATH):
        messagebox.showerror("Setup Zaroori", f"User ka face '{KNOWN_FACE_PATH}' par nahi mila.\nPehle capture_face.py chalayein.")
        return

    status_label.config(text="Verify ho raha hai... Intezaar karein.")
    root_window.update_idletasks()

    result = capture_and_verify_face()
    
    status_label.config(text="")

    if result:
        root_window.withdraw()
        messagebox.showinfo("Access Mila", "Face match ho gaya. Vault khul raha hai.")
        open_vault_window()
        root_window.deiconify()
    else:
        messagebox.showerror("Access Nahi Mila", "Face match nahi hua.")


# --- Main Application Shuru Karein ---
if __name__ == "__main__":
    # Pehle model ko initialize karein
    if initialize_model():
        # Agar model safaltapoorvak load ho gaya hai, toh hi login window banayein
        create_login_window(login)

