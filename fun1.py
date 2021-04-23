import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    numBilateralFilters = 1

    img_color = frame

    for _ in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 2, 2, 2)

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.medianBlur(img_gray, 7)

    img_edge = cv2.adaptiveThreshold(img_blur, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    output = cv2.bitwise_and(img_color, img_edge)

    cv2.imshow('fun1', output)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


