import cvlib as cv
import cv2
from imutils.video import FPS
import time
import serial

arduino = serial.Serial("COM3", 9600)

cap = cv2.VideoCapture("walk.mp4")

fps = FPS().start()
while cap.isOpened():

    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 500))
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.1, model='yolov3-tiny')
    if "person" in label:
        for i in range(len(label)):
            if label[i] == "person":
                cv2.rectangle(frame, (bbox[i][0], bbox[i][1]), (bbox[i][2], bbox[i][3]), (0, 0, 255), 2)
                middle = (int((bbox[i][0] + bbox[i][2]) / 2), int((bbox[i][1] + bbox[i][3]) / 2))
                cv2.circle(frame, middle, 5, (255, 0, 0), 5)
                middle = f"x{middle[0]}y{middle[1]}"
                arduino.write(middle.encode())
                print("sending:", middle)


    cv2.imshow("Real-time object detection", frame)
    time.sleep(0.5)
    fps.update()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cap.release()
cv2.destroyAllWindows()
