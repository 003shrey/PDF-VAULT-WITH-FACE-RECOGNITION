# face capture krne ke saare codes yha likh lete hain

import cv2
import os

# pehle check krte hain ki known_faces folder hai ya nahi
if not os.path.exists("known_faces"):
    os.makedirs("known_faces")

# webcam chalu krte hain yha pe
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam open nahi ho rahi. Please check device.")
    exit()

print("Camera chalu ho gaya. Face screen ke center mein lao, 's' dabake capture karo.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera se frame read nahi ho pa raha.")
        break

    # live video show karte hain
    cv2.imshow("Press 's' to capture your face", frame)

    # user se input lete hain
    key = cv2.waitKey(1)

    if key == ord('s'):
        save_path = "known_faces/shreyansh.jpg"
        cv2.imwrite(save_path, frame)
        print(f"Face capture ho gaya aur save hua: {save_path}")
        break

    elif key == ord('q'):
        print("Capture cancel kar diya.")
        break

cap.release()
cv2.destroyAllWindows()
