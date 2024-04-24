import cv2
import numpy as np
import sys

face_cascade = cv2.CascadeClassifier("../XML/haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("../XML/haarcascade_smile.xml")

cap = cv2.VideoCapture('')
cap.set(3, 640)
cap.set(4, 480)
sF = 1.05

while cap.isOpened():
    ret, frame = cap.read()
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=sF,
        minNeighbors=8,
        minSize=(55, 55),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in smile:
            print("Trovato un sorriso!")
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
    cv2.namedWindow('Smile Detector', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Smile Detector', 960, 540)

    cv2.imshow('Smile Detector', frame)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
