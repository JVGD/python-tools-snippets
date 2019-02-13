import numpy as np
import cv2

# Video source from camera id
src = 0

# Video source from file
src = "/home/jvgd/datasets/video/Mexico_start.mp4"

# Getting source
cap = cv2.VideoCapture(src)

# Read until video is completed
while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Releasing cap object and cleaning images
cap.release()
cv2.destroyAllWindows()