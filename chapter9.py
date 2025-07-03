import cv2
import numpy as np
import random

random.seed(34)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
PATH =  "Resources/Lenna.png"
MULTI_FACE_PATH = "Resources/multiple_Faces.png"

img = cv2.imread(PATH)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

img2 = cv2.imread(MULTI_FACE_PATH)
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(img2Gray, scaleFactor=1.1, minNeighbors=4)
for (x, y, w, h) in faces:
    cv2.rectangle(img2, (x, y), (x + w, y + h), random.choice(COLORS), 2)


height = min(img.shape[0], img2.shape[0])
img = cv2.resize(img, (int(img.shape[1] * height / img.shape[0]), height))
img2 = cv2.resize(img2, (int(img2.shape[1] * height / img2.shape[0]), height))

duo = np.hstack((img, img2))
cv2.imshow("Single & Multiple Faces", duo)
cv2.waitKey(0)


cv2.waitKey(0)

