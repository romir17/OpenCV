import cv2
print("pakage imported")

vid=cv2.VideoCapture(0)
vid.set(3,360)#width
vid.set(4,480)#height
vid.set(10,100)#brightness level

while True:
    success,img = vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break