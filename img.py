import numpy as np
import cv2

img = cv2.imread("./imgs/body.png")

body_cascade = cv2.CascadeClassifier("C:\\Users\\Joelr\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_lowerbody.xml")
face_cascade = cv2.CascadeClassifier('C:\\Users\\Joelr\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in body:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    face = face_cascade.detectMultiScale(gray, 1.3, 5,)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
