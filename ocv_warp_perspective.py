import numpy as np
import cv2

img=cv2.imread("img.png")
width,height=250,350

pts1=np.float32([[253,64],[684,64],[253,450],[684,450]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",imgOutput)
cv2.waitKey(0)