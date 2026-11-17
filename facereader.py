import cv2 as cv

webcam = cv.VideoCapture(0)

# rescale camera frame window popup
def rescaleFrame(frame, scale = 1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

webcam.set(cv.CAP_PROP_FRAME_WIDTH, 3)
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 1)

while True:
    isTrue, frame = webcam.read()

    frame_resize = rescaleFrame(frame)
    cv.imshow('hi', frame_resize)

    # closes the window after pressing esc
    if cv.waitKey(20) & 0xFF == 27:
        break


webcam.release()
cv.destroyAllWindows()