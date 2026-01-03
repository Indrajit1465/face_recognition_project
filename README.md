# Face Recognition Project (True / False)

This project implements a simple face recognition system using Python.
The system works in two stages:
1. Register a face (first-time)
2. Verify the face (returns True if matched, otherwise False)

## Tech Stack
- Python 3.10
- OpenCV
- dlib
- face-recognition
- NumPy

## Project Structure
```bash
face_recognition_project/
├── register_face.py
├── verify_face.py
├── requirements.txt
└── .gitignore
```

## How to Run

### 1. Create virtual environment
```bash
python -m venv myvenv
myvenv\Scripts\activate
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Register face
```bash
python register_face.py
```

### 4. Verify face
```bash
python verify_face.py
```

### Output

Displays True if the face matches

Displays False if the face does not match

### Notes

- Works best in good lighting conditions

- Designed for single-user verification




