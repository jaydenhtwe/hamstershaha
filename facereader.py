import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)

# resolution setter
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 450)

while True:
    isTrue, frame = webcam.read()
    webcamName = 'hi'
    cv.imshow(webcamName, frame)

    # closes the window after pressing esc or the X button
    if cv.waitKey(20) & 0xFF == 27 or cv.getWindowProperty(webcamName, cv.WND_PROP_VISIBLE) < 1:
        break

webcam.release()
cv.destroyAllWindows()