import cv2
import numpy as np
img=cv2.imread("Resources/lena.png")
print(img.shape)

Resize=cv2.resize(img,(480,640))
print(Resize.shape)

Crop=img[200:400,200:400]
cv2.imshow("Cropped Image",Crop)
cv2.waitKey(0)