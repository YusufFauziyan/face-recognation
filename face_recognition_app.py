import cv2
import face_recognition
import os
import numpy as np

# Load known faces
known_face_encodings = []
known_face_names = []

known_faces_dir = "known_faces"
for file in os.listdir(known_faces_dir):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image_path = os.path.join(known_faces_dir, file)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(file)[0])

# Initialize camera
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not open video source")
    exit()

# Set camera properties
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video_capture.set(cv2.CAP_PROP_FPS, 30)

cv2.namedWindow('Face Recognition', cv2.WINDOW_NORMAL)
cv2.startWindowThread()

try:
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Find all faces in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            # Find the best match
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            # Scale back up face locations
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            # Draw rectangle and label
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        
        cv2.imshow('Face Recognition', frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
            
except KeyboardInterrupt:
    print("Stopping...")
finally:
    video_capture.release()
    cv2.destroyAllWindows()
    for i in range(1, 5):
        cv2.waitKey(1)