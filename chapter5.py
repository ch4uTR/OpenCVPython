import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

cv2.imshow("Cards", img)
print(img.shape)



width, height = img.shape[1], img.shape[0]
pts1 = np.float32([[225,90],[430,135],[165,380],[365,420]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgNew = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Single Card", imgNew)
cv2.waitKey(0)