import cv2
import numpy as np

"""img = np.zeros((512,512,3), np.uint8)
print(img.shape)
cv2.imshow("Black Image Using Numpy Zeros - 512x512", img)"""

"""#Use : to cover the whole img
img[:] = 250,0,0 #Blue
cv2.imshow("Blue Image", img)"""

"""img[:256, :256] = 0, 250, 0
img[:256, 256:] = 250, 0, 0
img[256:, :256] = 0, 0, 250
img[256:, 256:] = 250, 250, 250

cv2.imshow("Green Image", img)"""


"""#CREATING LINES
img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 2)
cv2.line(img, (0, img.shape[0]), (img.shape[1],0), (0,255,0), 2)
cv2.imshow("Black Image With Green Line", img)"""

img = np.zeros((512,512,3), np.uint8)
cv2.rectangle(img, (10,10), (502, 502), (0,0,255),cv2.FILLED )
cv2.circle(img, (256,256), 50, (0,255,0), cv2.FILLED)
cv2.putText(img, "OpenCV Chapter-3", (100,200),cv2.FONT_ITALIC, 1, (255, 0, 0), 3)
cv2.imshow("Image", img)

cv2.waitKey(0)
