import cv2
import numpy as np

img=cv2.imread('img3.png')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(imgBlur,100,100)

cv2.imshow('Original',img)
cv2.imshow('Gray',imgGray)
cv2.imshow('Blur',imgBlur)
cv2.imshow('Canny',imgCanny)
cv2.waitKey(0)
