import cv2

img=cv2.imread("Resources/pica.png")
cv2.imshow("original",img)
print(img.shape)#to know the size of the image (picka image width=1920 height=1080)

Resize=cv2.resize(img,(480,640))
cv2.imshow("Resized",Resize)
print(Resize.shape)
cv2.waitKey(0)