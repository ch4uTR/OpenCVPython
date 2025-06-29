import cv2
import numpy as np

img = cv2.imread("Resources/dog.png")

#USING NUMPY.HSTACK WE CAN PRESENT IMAGES TOGETHER
imgHor = np.hstack((img, img))
cv2.imshow("Horizontal Images", imgHor)

#VERTICAL
imgVert = np.vstack((img,img))
cv2.imshow("Vertical Images", imgVert)

cv2.waitKey(0)