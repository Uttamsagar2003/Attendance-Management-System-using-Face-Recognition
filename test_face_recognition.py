import face_recognition

# Load a sample image and get face encodings
try:
    image = face_recognition.load_image_file('dataset/person1/person1_image1.jpg')  # Replace with a valid image path
    face_encodings = face_recognition.face_encodings(image)
    
    if face_encodings:
        print("Face encoding found:", face_encodings[0])
    else:
        print("No face encoding found.")
except Exception as e:
    print("An error occurred:", e)
