"""
openCV 5 1-2 binary image
2color image threshold (임계값)
"""

## histogram을 이용해서 threshold를 결정하게 됨.
##adaptive threshold을 이용

def onchange(x):
    pass

import cv2
import numpy as np

"""
img= cv2.imread('img/r.jpg')
# cv2.namedWindow('img',0)
cv2.namedWindow('binary',0)

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

option=np.array([[cv2.THRESH_BINARY],[cv2.THRESH_TRUNC],[cv2.THRESH_BINARY_INV],[cv2.THRESH_TOZERO],[cv2.THRESH_TRIANGLE]])

cv2.createTrackbar('option','binary',0,len(option),onchange)
cv2.createTrackbar('Threshold','binary',128,255,onchange)

while cv2.waitKey(1)!=ord('q'):

    option = cv2.getTrackbarPos('option', 'binary')
    threshold= cv2.getTrackbarPos('Threshold','binary')
    ret, binary=cv2.threshold(gray,threshold,255,option)

    cv2.imshow('binary',binary)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

##adaptive Threshold

cv2.namedWindow('img')
cv2.namedWindow('threshold')
cv2.namedWindow('mean')
cv2.namedWindow('gauss')

img=cv2.imread('img/r.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, threshold= cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
mean= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)
gauss = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)

cv2.imshow('threshold',threshold)
cv2.imshow('mean',mean)
cv2.imshow('gauss',gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
