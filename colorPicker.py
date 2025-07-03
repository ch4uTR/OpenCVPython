import cv2
import numpy as np
from numpy.ma.extras import hstack

FRAME_WIDTH = 640
FRAME_HEIGHT = 480

cap = cv2.VideoCapture(0)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(10, 150)

def empty(a):
    pass

cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", (640,240))

cv2.createTrackbar("Hue Min", "Track Bars", 109, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 160, 179, empty)
cv2.createTrackbar("Saturation Min", "Track Bars", 39, 255, empty)
cv2.createTrackbar("Saturation Max", "Track Bars", 146, 255, empty)
cv2.createTrackbar("Value Min", "Track Bars", 101, 255, empty)
cv2.createTrackbar("Value Max", "Track Bars", 205, 255, empty)



while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Saturation Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Saturation Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Value Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Value Max", "Track Bars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])

    cv2.imshow("Result", hstack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()