import cv2
import numpy as np

img=cv2.imread("img.png")
print(img.shape)

resizedImg=cv2.resize(img,(200,200))
crppedImg=img[0:200,200:500]
cv2.imshow("Resized",resizedImg)
cv2.imshow("Original",img)
cv2.imshow("Cropped",crppedImg)
cv2.waitKey(0)