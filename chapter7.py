import cv2
import numpy as np

PATH = "Resources/lenna.png"
img = cv2.imread(PATH)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)




def empty(a: int):
    pass

#CREATE A NEW WINDOW FOR BAR
cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", (640,240))

cv2.createTrackbar("Hue Min", "Track Bars", 109, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 160, 179, empty)
cv2.createTrackbar("Saturation Min", "Track Bars", 39, 255, empty)
cv2.createTrackbar("Saturation Max", "Track Bars", 146, 255, empty)
cv2.createTrackbar("Value Min", "Track Bars", 101, 255, empty)
cv2.createTrackbar("Value Max", "Track Bars", 205, 255, empty)

while True:
    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Saturation Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Saturation Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Value Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Value Max", "Track Bars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper =  np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Mask", mask)
    cv2.imshow("Original", img)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(10)





#109 160 39 146 101 205