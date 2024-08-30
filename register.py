import cv2
import os

def register_face():
    name = input("Enter your name: ")
    
    # Ensure the dataset directory exists
    dataset_dir = 'dataset'
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    
    # Create a subdirectory for the person if it doesn't exist
    person_dir = os.path.join(dataset_dir, name)
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)

    # Initialize webcam
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Register")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Display the frame
        cv2.imshow("Register", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:  # SPACE pressed
            img_name = f"{name}_{img_counter}.jpg"
            img_path = os.path.join(person_dir, img_name)
            cv2.imwrite(img_path, frame)
            print(f"{img_name} written!")
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register_face()
