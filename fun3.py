import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    numBilateralFilters = 1

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.medianBlur(img_gray, 7)

    img_edge = cv2.adaptiveThreshold(img_blur, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)

    cv2.imshow('fun2', img_edge)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


