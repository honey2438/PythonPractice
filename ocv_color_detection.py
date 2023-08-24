import cv2
import numpy as np

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,lambda x:x)
cv2.createTrackbar("Hue Max","Trackbars",179,179,lambda x:x)
cv2.createTrackbar("Sat Min","Trackbars",0,255,lambda x:x)
cv2.createTrackbar("Sat Max","Trackbars",255,255,lambda x:x)
cv2.createTrackbar("Val Min","Trackbars",0,255,lambda x:x)
cv2.createTrackbar("Val Max","Trackbars",255,255,lambda x:x)

while True:

    img=cv2.imread("img.png")
    img=cv2.resize(img,(640,480))   
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max=cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min=cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max=cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min=cv2.getTrackbarPos("Val Min","Trackbars")
    v_max=cv2.getTrackbarPos("Val Max","Trackbars")
    mask=cv2.inRange(imgHSV,np.array([h_min,s_min,v_min]),np.array([h_max,s_max,v_max]))    
    imgResult=cv2.bitwise_and(img,img,mask=mask)
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    cv2.imshow("mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.imshow("HSV",imgHSV)
    cv2.waitKey(1)