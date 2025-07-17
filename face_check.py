# face_check.py
# yeh script stored image aur webcam se face match karke access allow karta hai

import face_recognition
import cv2
import time
import os

def verify_face():
    # Step 1: Known image load karo
    image_path = "known_faces/shreyansh_fixed.jpg"
    
    if not os.path.exists(image_path):
        print("Known face image file nahi mili.")
        return False

    known_image = face_recognition.load_image_file(image_path)
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        print("Face image mein recognizable face nahi mila. Check karo image sahi hai ya nahi.")
        return False

    known_encoding = known_encodings[0]

    # Step 2: Webcam access lo
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Webcam open nahi ho pa rahi.")
        return False

    print("Camera chalu ho gaya hai... Face align karo.")

    # Step 3: 10 frames capture karo taaki camera stable ho jaye
    for _ in range(10):
        ret, frame = cap.read()
        if not ret:
            print("Camera frame read nahi ho pa raha.")
            cap.release()
            return False
        time.sleep(0.1)  # thoda delay dete hain for better capture

    # Step 4: Last frame ko process karo
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    if not face_encodings:
        print("Camera se koi face detect nahi hua. Light ya position check karo.")
        cap.release()
        return False

    # Step 5: Match check karo
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        if True in matches:
            print("Face match ho gaya.")
            cap.release()
            return True

    print("Face match nahi hua.")
    cap.release()
    return False
