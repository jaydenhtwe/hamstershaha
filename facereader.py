import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
webcamName = 'hi'

# resolution setter
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

haarcascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# opens webcam
while True:
    isTrue, frame = webcam.read()

    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rectangle = haarcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces_rectangle:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), thickness = 2)

    cv2.imshow(webcamName, frame)

    # closes the window after pressing esc or the X button
    if cv2.waitKey(20) & 0xFF == 27 or cv2.getWindowProperty(webcamName, cv2.WND_PROP_VISIBLE) < 1:
        break

webcam.release()
cv2.destroyAllWindows()