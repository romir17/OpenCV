import cv2
print("pakage imported")
img=cv2.imread("resources/lena.png") #using function imread to read the images
cv2.imshow("output",img) #using function imshow to display the image
cv2.waitKey(0) #waitkey function to see the image for specific period of time