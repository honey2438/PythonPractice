import cv2

cap=cv2.VideoCapture('vid.mp4')
cap.set(3,400)
cap.set(4,400)
cap.set(10,100)
while True:
    success,img=cap.read()
    if success:
        cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

