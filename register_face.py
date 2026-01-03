import cv2
import face_recognition
import numpy as np
import os

KNOWN_FACE_DIR = "known_face"
ENCODING_PATH = os.path.join(KNOWN_FACE_DIR, "face_encoding.npy")

os.makedirs(KNOWN_FACE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)

print("Press 's' to save face, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    if face_locations:
        face_encoding = face_recognition.face_encodings(
            rgb_frame, face_locations
        )[0]

        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)
    if key == ord('s') and face_locations:
        np.save(ENCODING_PATH, face_encoding)
        print("Face registered successfully")
        break
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
