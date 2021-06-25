##openCV 3(5/6~   mouse event
##assignment 영상에서 좌클릭시 움직일 때 선이 그어지도록 혹은 다른 이펙트를 줄 수 있도록.

import cv2
import numpy as np

def CallbackFucn(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        print("L botton down", x, y)
        cv2.circle(param, (x, y), 2, (255, 0, 0), 2)
        cv2.imshow('img',param)
    elif event ==cv2.EVENT_RBUTTONDOWN:
        print("R botton down",x,y)
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("M botton down",x,y)



img= cv2.imread('img/poster.jpg')
cv2.namedWindow('img',0)

cv2.setMouseCallback('img',CallbackFucn,img)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()