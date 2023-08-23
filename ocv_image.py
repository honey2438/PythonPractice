import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)

img=cv2.imread('img.png')
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurImg=cv2.GaussianBlur(grayImg,(7,7),0)
cannyImg=cv2.Canny(img,100,100)
dialationImg=cv2.dilate(cannyImg,kernel,iterations=1)
erodedImg=cv2.erode(dialationImg,kernel,iterations=1)   

cv2.imshow('Gray',grayImg)
cv2.imshow('Blur',blurImg)
cv2.imshow('Canny',cannyImg)
cv2.imshow('Dialation',dialationImg)
cv2.imshow('Eroded',erodedImg)
cv2.waitKey(0)
