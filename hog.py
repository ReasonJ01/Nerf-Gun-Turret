import numpy as np
import cv2

cap = cv2.VideoCapture('imgs/production ID_4423925.mp4')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (rects, weights) = hog.detectMultiScale(gray, winStride=(5, 5), padding=(8, 8), scale=1.05)
    for x, y, w, h in rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()