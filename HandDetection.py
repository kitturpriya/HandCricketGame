import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize the hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Define the fingerup variable
fingerup = []

# Define the number variable
number = 0

# Start the video capture
cap = cv2.VideoCapture(0)

# Initialize the last_detection_time
last_detection_time = time.time()

# Loop over the video frames
while True:

    # Get the frame
    success, frame = cap.read()

    # Detect the hands
    hands, _ = detector.findHands(frame)

    # If a hand is detected and sleep for 3 secs interval
    if hands and time.time() - last_detection_time >= 2:

        # Get the landmarks of the hand
        lmlist = hands[0]

        # Find how many fingers are up
        fingerup = detector.fingersUp(lmlist)

        # Different conditions for different number of fingers up
        if fingerup == [0, 1, 0, 0, 0]:
            number = 1
        elif fingerup == [0, 1, 1, 0, 0]:
            number = 2
        elif fingerup == [0, 1, 1, 1, 0]:
            number = 3
        elif fingerup == [0, 1, 1, 1, 1]:
            number = 4
        elif fingerup == [1, 1, 1, 1, 1]:
            number = 5
        elif fingerup == [1, 0, 0, 0, 0]:
            number = 6


        # Display the number on the frame
        cv2.putText(frame, str(number), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Update the last_detection_time
        last_detection_time = time.time()

        # Print the number of fingers up
        print(number)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check if the user pressed the ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the video capture
cap.release()

# Destroy all windows
cv2.destroyAllWindows()