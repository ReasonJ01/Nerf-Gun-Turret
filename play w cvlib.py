import cvlib as cv
import cv2

cap = cv2.VideoCapture('imgs/production ID_4423925.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bbox, label, conf = cv.detect_common_objects(gray, confidence=0.25, model='yolov3-tiny')
    frame = cv.object_detection.draw_bbox(frame, bbox, label, conf)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()