## openCV 3 (4/6~   ##draw contours 외각선 검출

import numpy as np
import cv2
import random

img=cv2.imread('img/pattern.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

###사용할때 ret이 존재해야 제대로 인식된다. 왜 그런건지 모르겟당.
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# print(np.shape(img))
w=420
h=1000

dst=np.zeros([w,h,3],dtype='uint8')
dst[:,:,:]=255

contours,hierarchy = cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
###hierarchy _ 계츨구조
###contoures _ 외각을 구하는 함수
cv2.drawContours(dst,contours,-1,(0,0,255),1,8,hierarchy)

## drawcontours를 이용해서 백지에 그림을 그리는 것.
##여러가지 색상으로 contours를 넣고 싶을 경우

cv2.imshow('contours',dst)
# cv2.imshow('img',img)
# cv2.imshow('gray',gray)
cv2.imshow('binary',binary)

cv2.waitKey(0)
cv2.destroyAllWindows()