import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
webcamName = 'hi'

# resolution setter
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# opens webcam
while True:
    isTrue, frame = webcam.read()

    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), thickness = 2)

        roi_gray = gray[y + h // 2: y + h, x: x + w]
        smiles, reject_lvl, lvl_weights = smile_cascade.detectMultiScale3(roi_gray, scaleFactor=1.05, minNeighbors=60, minSize=(25, 25), outputRejectLevels=True)
        for (sx, sy, sw, sh), weight in zip(smiles, lvl_weights):
            if weight < 3:
                continue
            cv2.rectangle(frame, (x + sx, y + h // 2 + sy), (x + sx + sw, y + h // 2 + sy + sh), (0, 255 ,0), 2)

    cv2.imshow(webcamName, frame)

    # closes the window after pressing esc or the X button
    if cv2.waitKey(20) & 0xFF == 27 or cv2.getWindowProperty(webcamName, cv2.WND_PROP_VISIBLE) < 1:
        break

webcam.release()
cv2.destroyAllWindows()