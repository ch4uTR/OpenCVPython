import cv2
import numpy as np



##################################################################
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
##################################################################
IMG_WIDTH = 640
IMG_HEIGHT = 480
##################################################################
KERNEL = np.ones((5,5))
##################################################################

cap = cv2.VideoCapture(0)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(10, 150)


########################### PREPROCESS THE IMAGE AND RETURN USEFUL PROCESSED IMAGES #####################
def preprocess(img):
    """
    takes an image and returns a dictionary with grayscale, blurred, canny, dilate and erode images
    """
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    imgDial = cv2.dilate(imgCanny, KERNEL, iterations=2)
    imgThreshold = cv2.erode(imgDial, KERNEL, iterations=1)

    return {"Resized" : img ,"Gray" : imgGray, "Blur" : imgBlur, "Canny" : imgCanny, "Dial" : imgDial, "Threshold" : imgThreshold}

#############################################################################################################
def getContours(img, imgContour):
    biggest = np.array([])
    maxArea = 0

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (0, 255, 0), 10)
    return biggest


def getWarp(img, biggestContour):

    width, height = img.shape[1], img.shape[0]
    pts1 = biggest.reshape(4, 2).astype(np.float32)
    pts2 = np.float32([[0, 0], [IMG_WIDTH, 0], [IMG_WIDTH, IMG_HEIGHT], [0, IMG_HEIGHT]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (IMG_WIDTH, IMG_HEIGHT))
    return imgOutput

while True:
    success, img = cap.read()
    prep_dict = preprocess(img)
    imgContour = prep_dict["Resized"].copy()#coppied the original img
    biggest = getContours(prep_dict["Threshold"], imgContour)

    if biggest is not None and biggest.size != 0:
        imgWarp = getWarp(img, biggest)
        cv2.imshow('Result', imgWarp)
    else:
        cv2.imshow('Result', imgContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break