import cv2
print("package imported!")

#IMAGE
"""img = cv2.imread("Resources/dog.png")
cv2.imshow("Output", img)
cv2.waitKey(0)"""

#VIDEO
"""cap = cv2.VideoCapture("Resources/file_example_MP4_640_3MG.mp4") #A sequence of images!
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break  """

#WEBCAM
cap = cv2.VideoCapture(0)
cap.set(3, 640) #width
cap.set(4, 480) #height
cap.set(10, 100) #brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break