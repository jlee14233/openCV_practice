##openCV 4 (3/8-4/8)

import cv2
import numpy as np
import multiprocessing as mp ## 병렬처리에 대한 것은 다음으로 미루기.
"""
img = cv2.imread('img/pattern.jpg')
img2 = cv2.imread('img/dot.png')

reimg=cv2.resize(img,dsize=(img2.shape[1],img2.shape[0]))

img_add =cv2.add(reimg,img2)
# img_add=img2+reimg
img_subtract =cv2.subtract(reimg,img2)
# img_divide=cv2.divide(reimg,img2)
# img_multi=cv2.multiply(reimg,img2)


if alpha <0.0:
    alpha=0
elif alpha>=1.0:
    alpha=1


for i in range(0,11,1):
    alpha=i*0.1
    beta=1.0-alpha
    add=cv2.addWeighted(reimg,alpha,img2,beta,0)
    cv2.imshow('addWeighted', add)
    cv2.waitKey(500)


# cv2.imshow('img',reimg)
# cv2.imshow('img2',img2)
# cv2.imshow('img_add',img_add)
cv2.imshow('img_subtract',img_subtract)

# cv2.imshow('img_multi',img_multi)
# cv2.imshow('img_divide',img_divide)
"""


## 차 영상 만들기 프레임을 두번 뽑아서 빼면 된다.
cap = cv2.VideoCapture(0)
old_frame=cap.read()
while(True):

    ret, old_frame = cap.read()
    ret2, new_frame = cap.read()

    if ret == False:
        break

    sub_frame =cv2.subtract(old_frame,new_frame)

    cv2.imshow("video",new_frame)
    # sobel = cv2.Sobel(img,0,1,0)
    # cv2.imshow("sobel",sobel)
    cv2.imshow('sub',sub_frame)

    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()