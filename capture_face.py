#face capture krne ke saare codes yha likh lete hain

import cv2

# webcam chalu krte hain yha pe
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if ret:
    cv2.imshow("Captured Face", frame)
    cv2.imwrite("known_faces/shreyansh.jpg", frame)
    print(" Face captured hogya aur  saved as 'shreyansh.jpg'")
else:
    print(" Failed to capture face (wapas se kosis kro)")

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
