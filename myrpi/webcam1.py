import cv2

try:
    cap = cv2.VideoCapture(0)
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('/tmp/output.avi', fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret is True:
            out.write(frame)
        else:
            break
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    out.release()
