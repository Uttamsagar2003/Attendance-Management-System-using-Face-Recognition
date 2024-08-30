import cv2
import face_recognition
import os
import pickle
from datetime import datetime

def mark_attendance(name):
    if not os.path.exists('attendance'):
        os.makedirs('attendance')

    attendance_file = 'attendance/attendance.csv'
    if not os.path.isfile(attendance_file):
        with open(attendance_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Time'])

    with open(attendance_file, 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def main():
    # Load known faces and encodings
    if not os.path.isfile('encodings/encodings.pickle'):
        print("Error: 'encodings/encodings.pickle' file not found.")
        return

    with open('encodings/encodings.pickle', 'rb') as f:
        known_encodings, known_names = pickle.load(f)

    # Initialize the webcam
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam. Ensure it's connected and not used by another application.")
        return

    print("Webcam is open. Press 'q' to quit.")
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Convert image from BGR to RGB
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find faces in the current frame
        face_locations = face_recognition.face_locations(img)
        face_encodings = face_recognition.face_encodings(img, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

            mark_attendance(name)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
