import cv2

def detect_cat(image_path):
    # Load the pre-trained Haar Cascade classifier for cat detection
    cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale (required for the detector)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform cat detection
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around the detected cats
    for (x, y, w, h) in cats:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'CAT', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image with detected cats
    cv2.imshow('Detected Cats', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()









def detect_human(image_path):
    # Load the pre-trained Haar Cascade classifier for cat detection
    human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    img=cv2.imread(image_path)
    # Convert the image to grayscale (required for the detector)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform cat detection
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected cats
    for (x, y, w, h) in humans:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'HUMAN', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    # Display the image with detected cats
    cv2.imshow('Detected Humans', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()







def detect_humanandcat(image_path):
    # Load the pre-trained Haar Cascade classifier for cat detection
    human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale (required for the detector)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform cat detection
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))

    # Draw rectangles around the detected cats
    for (x, y, w, h) in cats:
        center = (x + w // 2, y + h // 2)
        radius = w // 2
        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.putText(img, 'CAT', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Draw rectangles around the detected humans
    for (x, y, w, h) in humans:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'HUMAN', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image with detected cats and humans
    cv2.imshow('Detected Humans and Cats', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_catandhuman_frame(frame):
    # Load the pre-trained Haar Cascade classifier for cat and human detection
    cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
    human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
   
    # Convert the frame to grayscale (required for the detectors)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform cat and human detection
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))


    # Draw rectangles around the detected humans
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'HUMAN', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    for (x, y, w, h) in cats:
        center = (x + w // 2, y + h // 2)
        radius = w // 2
        cv2.circle(frame, center, radius, (0, 255, 0), 2)
        cv2.putText(frame, 'CAT', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    return frame

def detect_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            # Break the loop if the frame couldn't be captured (e.g. if the webcam is disconnected)
            break

        # Detect humans and cats in the current frame and draw rectangles around them
        frame = detect_catandhuman_frame(frame)

        # Display the frame with detected humans and cats
        cv2.imshow('Webcam - Detected Humans ', frame)
    # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam capture and close all windows
    cap.release()
    cv2.destroyAllWindows()




       
         


import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def display():
    while True:
        print("FACE DETECTION:")
        
        print("1. To Detect Cats using jpg image")
        
        print("2. To Detect Humans using jpg image")
        
        print("3. To Detect cats and humans using jpg")
        
        print("4. To Detect using web camera")
        
        print("5. Exit")
      
        
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
            
        if choice == '1':
            image_path = input("Enter the path of the JPG image: ")
            detect_cat(image_path)#detect_cats is function name
        elif choice == '2':
             image_path = input("Enter the path of the JPG image: ")
             detect_human(image_path)#detect_humans is function name
        elif choice == '3':
             image_path = input("Enter the path of the JPG image: ")
             detect_humanandcat(image_path)
        elif choice == '4':
            detect_webcam()
        elif choice=='5':
            print("exiting the program.")
            break
        else:
            print("Invalid option please enter again:")

print("FACE DETECTION:")
speak("FACE DETECTION:")
print("1. To Detect Cats using jpg image")
speak("option one,To Detect Cats using jpg image")
print("2. To Detect Humans using jpg image")
speak("option 2, To Detect Humans using jpg image")
print("3. To Detect cats and humans using jpg")
speak("option 3, To Detect cats and humans using jpg")
print("4. To Detect using web camera")
speak("option 4, To Detect using web camera")
print("5. Exit")
speak("option 5, Exit")
    
speak("Enter your choice") 
choice = input("Enter your choice (1/2/3/4/5): ")
    
        
if choice == '1':
    image_path = input("Enter the path of the JPG image: ")
    detect_cat(image_path)#detect_cats is function name
    display()
elif choice == '2':
    image_path = input("Enter the path of the JPG image: ")
    detect_human(image_path)#detect_humans is function name
    display()
elif choice == '3':
    image_path = input("Enter the path of the JPG image: ")
    detect_humanandcat(image_path)
    display()
elif choice == '4':
    detect_webcam()
    display()
elif choice=='5':
    print("exiting the program.")
else:
    print("Invalid option please enter again:")
    display()