import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lr = np.array([30, 150, 50])
    ur = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lr, ur)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('fun', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
