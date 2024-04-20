# Face_Recognition

This Python code utilizes OpenCV (cv2) to perform face and cat detection in images or through a webcam. It provides options to detect cats, humans, or both in a given image or through live video from the webcam.

## Installation

1. **Python**: Make sure you have Python installed on your system (version 3.x recommended).
2. **OpenCV**: Install OpenCV by running `pip install opencv-python`.

## Usage

### 1. Detect Cats using a JPG image
   - Select option 1.
   - Enter the path of the JPG image when prompted.

### 2. Detect Humans using a JPG image
   - Select option 2.
   - Enter the path of the JPG image when prompted.

### 3. Detect Cats and Humans using a JPG image
   - Select option 3.
   - Enter the path of the JPG image when prompted.

### 4. Detect using the webcam
   - Select option 4.
   - A live video stream from the webcam will open.
   - Press 'q' to exit.

### 5. Exit
   - Select option 5 to exit the program.

## Functions

- `detect_cat(image_path)`: Detects cats in a JPG image.
- `detect_human(image_path)`: Detects humans in a JPG image.
- `detect_humanandcat(image_path)`: Detects both humans and cats in a JPG image.
- `detect_webcam()`: Detects humans and cats in real-time using the webcam.
- `detect_catandhuman_frame(frame)`: Detects both humans and cats in a single frame.
- `display()`: Displays the menu for selecting detection options.
- `speak(audio)`: Function to speak the menu options using text-to-speech.

## Dependencies

- `opencv-python`: OpenCV library for image processing and computer vision tasks.
- `pyttsx3`: Text-to-speech library for speaking the menu options.

## Credits

- The face and cat detection algorithms utilize pre-trained Haar Cascade classifiers provided by OpenCV.
- Webcam integration is achieved using OpenCV's VideoCapture functionality.

 