# PDF Vault with Face Recognition

This is a desktop-based secure PDF vault system that uses face recognition for login authentication.
The application is currently under development. More features and improvements are being added progressively.

## Current Features

- Face recognition-based login using webcam
- Basic Tkinter-based GUI interface
- Modular code: separate logic for GUI and face verification
- Known face stored locally and matched in real-time

## Technologies Used

- Python 3.12
- OpenCV
- face_recognition
- dlib
- Tkinter

## Project Structure

.
├── main.py               # GUI and application flow
├── face_check.py         # Face recognition logic
├── capture_face.py       # Utility to save known face
├── vault/                # Directory to store PDFs
├── known_faces/          # Stores known face image (e.g. shreyansh_fixed.jpg)
├── requirements.txt      # Required Python packages
├── change_log.md         # Development progress log
└── README.md             # Project documentation (this file)

## Upcoming Features

- PDF Upload, View, and Delete functionality
- AES-based file encryption and decryption
- Access logs and error handling
- Password fallback authentication
- Polished GUI with user-friendly controls

## Status

Under development. Not ready for production use.
