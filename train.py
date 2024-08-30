import os
import face_recognition
import pickle

def train_model():
    known_encodings = []
    known_names = []

    for person_name in os.listdir('dataset'):
        person_folder = f"dataset/{person_name}"
        for image_file in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_file)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            
            if encoding:
                known_encodings.append(encoding[0])
                known_names.append(person_name)

    if not os.path.exists('encodings'):
        os.makedirs('encodings')

    with open('encodings/encodings.pickle', 'wb') as f:
        pickle.dump((known_encodings, known_names), f)
    
    print("Model trained and encodings saved.")

if __name__ == "__main__":
    train_model()
