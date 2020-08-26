import numpy as np
import cv2
import serial

ard = serial.Serial("COM3", 9600)

cap = cv2.VideoCapture('imgs/production ID_4423925.mp4')

body_cascade = cv2.CascadeClassifier("C:\\Users\\Joelr\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_upperbody.xml")

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray, 1.3, 3, minSize=(50,50) )
    print(body)
    for x, y, w, h in body:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        middle = (int(x+(w / 2)), int(y+(h / 2)))
        cv2.circle(frame, middle, 5, (0, 0, 255), 3)
        print(np.







    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
