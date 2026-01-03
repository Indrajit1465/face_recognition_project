import cv2
import face_recognition
import numpy as np
import os

ENCODING_PATH = "known_face/face_encoding.npy"

if not os.path.exists(ENCODING_PATH):
    print("No registered face found. Run register_face.py first.")
    exit()

known_encoding = np.load(ENCODING_PATH)

cap = cv2.VideoCapture(0)

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_frame, face_locations
    )

    result_text = "False"

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            [known_encoding], face_encoding, tolerance=0.5
        )
        if matches[0]:
            result_text = "True"

    cv2.putText(
        frame,
        result_text,
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0) if result_text == "True" else (0, 0, 255),
        3
    )

    cv2.imshow("Face Verification", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
