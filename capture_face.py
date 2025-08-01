# capture_face.py (Updated to work with the new main.py)

import cv2
import os

# --- Configuration ---
# The folder where we store the user's reference image
KNOWN_FACES_DIR = "known_faces"
# The path for the user's photo, matching the path in main.py
USER_FACE_PATH = os.path.join(KNOWN_FACES_DIR, "user_face.jpg")


def capture_face():
    """
    Captures and saves a single photo of the user for face verification.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(KNOWN_FACES_DIR):
        os.makedirs(KNOWN_FACES_DIR)
        print(f"Created directory: {KNOWN_FACES_DIR}")

    # Start the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam. Please check the connection.")
        return

    print("\n--- Face Capture ---")
    print("Camera is active.")
    print("Please position your face in the center of the screen.")
    print("Press 's' to save the picture.")
    print("Press 'q' to quit without saving.")
    print("--------------------")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame from webcam.")
            break

        # Display the live video feed
        cv2.imshow("Press 's' to capture, 'q' to quit", frame)

        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Save the captured frame to the specified path
            cv2.imwrite(USER_FACE_PATH, frame)
            print(f"\nSuccess! Face captured and saved to: {USER_FACE_PATH}")
            break
        elif key == ord('q'):
            print("\nCapture cancelled. No image was saved.")
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_face()

