import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Grey scaling of the image
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0) #Adding Blurness to the image
imgCanny = cv2.Canny(img, 100, 250)  #Used for edge detection in images
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)#To increase the thickness of the edges
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)#To reduce the size of the edges

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)