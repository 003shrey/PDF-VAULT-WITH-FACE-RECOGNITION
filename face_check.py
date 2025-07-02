# face recognise yha karte hain

import face_recognition
import cv2
import os

def verify_face():
    known_image = face_recognition.load_image_file("known_faces/shreyansh.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if not ret:
        print(" web cam ni khula")
        return False

    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        if True in matches:
            print(" Face verified")
            cap.release()
            return True

    print(" Face not recognized")
    cap.release()
    return False
