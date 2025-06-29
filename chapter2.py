import cv2
import numpy

try:
    import numpy as np
    print("Numpy Imported")
except ImportError:
    import os
    print("Installing Numpy")
    os.system("pip install numpy")
    import numpy as np



img = cv2.imread("Resources/lenna.png")

#CONVERTING TO GRAYSCALE
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#BLUR
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

#EDGE
imgCanny = cv2.Canny(img, 100, 100)
imgCannyReducedTreshold = cv2.Canny(img, 150, 200)

#DILATION
kernel = np.ones((5,5), np.uint8) #defining a kernel
imgDilation = cv2.dilate(imgCanny, kernel=kernel, iterations=1)

#EROSION
imgEroded = cv2.erode(imgDilation, kernel=kernel, iterations=1)



def compare_threshold():
    cv2.imshow("Canny Image", imgCanny)
    cv2.imshow("Reduced Canny Image", imgCannyReducedTreshold)
    cv2.waitKey(0)

def compare_blur():
    cv2.imshow("Gray Image", imgGray)
    cv2.imshow("Blur Image", imgBlur)
    cv2.waitKey(0)

def compare_dilation():
    cv2.imshow("Canny Image", imgCanny)
    cv2.imshow("Dilation Image", imgDilation)
    cv2.waitKey(0)

def compare_erosion():
    cv2.imshow("Canny Image", imgCanny)
    cv2.imshow("Erosion Image", imgEroded)
    cv2.waitKey(0)


def compare_corners():
    cv2.imshow("Canny Image", imgCanny)
    cv2.imshow("Dilation Image", imgDilation)
    cv2.imshow("Erosion Image", imgEroded)
    cv2.waitKey(0)

compare_corners()


