import cv2
import numpy as np


FRAME_WIDTH = 640
FRAME_HEIGHT = 480

cap = cv2.VideoCapture(0)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(10, 150)

#USING colorPicker.py I found out 2 color

colors = [[60,44,19,102,127,149], [152,153,129,179,219,198]]
color_values = [[0,255,0], [0,0,255]]
points = []


def find_color(img, colors, imgResult, point_list):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i, color in enumerate(colors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        point = getContours(mask)
        if point is not None:
            cv2.circle(imgResult, point, 10, color_values[i], 2, cv2.FILLED)
            point_list.append([point[0], point[1], color_values[i]])
        cv2.imshow(f"Color{i+1}", mask)


def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 1)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            return x + w//2, y #top point
    return None

def drawPoints(img, points):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 10, point[2], 2, cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    find_color(img, colors, imgResult, points)
    if len(points) > 0:
        drawPoints(imgResult, points)
    cv2.imshow("Result", imgResult)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

