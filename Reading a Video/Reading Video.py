import cv2
print("pakage imported")

vid=cv2.VideoCapture("Resources/African_Wildlife.mp4")

while True:
    success,img = vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break