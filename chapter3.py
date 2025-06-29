import cv2
import numpy as np


img = cv2.imread("Resources/lenna.png") #512x512
#LEARN THE SHAPE
print(img.shape) # (512,512,3) (BGR in opencv)


imgResized = cv2.resize(img, (480,480))
imgStreched = cv2.resize(img, (1024,1024))

imgCropped = img[0:256, 256:512] #HEIGHT comes first
def compare_size():
    cv2.imshow("Lenna - 512x512", img)
    cv2.imshow("Lenna - 480x480", imgResized)
    cv2.imshow("Lenna - 1024x1024", imgStreched)
    cv2.waitKey(0)

def compare_crop():
    cv2.imshow("Lenna - 512x512", img)
    cv2.imshow("Lenna [0:256, 256:512]", imgCropped)
    cv2.waitKey(0)

compare_crop()
