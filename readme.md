

### FACE RECONGATION PY

```markdown
# 🧠 Face Recognition App

A simple real-time face recognition app using Python, OpenCV, and the `face_recognition` library. It uses your webcam to detect and recognize faces based on a folder of known face images.

---

## 🚀 Features

- 📷 Real-time face detection and recognition from webcam.
- 🧠 Compares detected faces with pre-encoded known faces.
- 🏷️ Displays bounding boxes and name labels.
- 🖼️ Easy setup: just drop images of known faces into a folder.

---

## 🛠️ Requirements

- Python 3.8 or higher
- OpenCV
- face_recognition
- NumPy

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/face-recognition-app.git
cd face-recognition-app
```

2. **Install the dependencies**

```bash
pip install -r requirements.txt
```

> **Note for macOS M1/M2 users:**  
If you encounter issues with installing `dlib` (a dependency of `face_recognition`), install these first:

```bash
brew install cmake
brew install boost
pip install dlib
```

---

## 📁 Project Structure

```
face-recognition-app/
├── face_recognition_app.py      # Main app script
├── known_faces/                 # Folder with known face images
│   ├── john_doe.jpg             # Example: detected as "john_doe"
│   └── jane_doe.png
├── requirements.txt
└── README.md
```

> All images in the `known_faces` folder should contain **only one face**, and the filename (without extension) will be used as the person's name.

---

## ▶️ Usage

1. Put the face images into the `known_faces/` directory.
2. Run the script:

```bash
python face_recognition_app.py
```

3. The app will start your webcam and begin detecting faces.
4. Press `q` to quit the program.

---

## 📸 Supported Image Formats

- `.jpg`
- `.png`
- `.jpeg`

---

## 🤖 Libraries Used

- [face_recognition](https://github.com/ageitgey/face_recognition) — for face detection and encoding
- [OpenCV](https://opencv.org/) — for video capture and UI
- [NumPy](https://numpy.org/) — for array and math operations
