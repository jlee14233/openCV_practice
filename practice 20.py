"""
openCV 6 4/6
2D histogram
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt



src = cv2.imread('img/joker.PNG')
# cv2.imshow('img1',src)

hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

hbins = 30
sbins = 32

channels=[0,1]
scale=10
hist=cv2.calcHist([hsv],channels,None,[30,32],[0,180,0,256])
maxvalue = cv2.minMaxLoc(hist,None)

histimg =np.zeros((sbins*scale,hbins*scale),dtype=np.uint8)
print(hist)
print(maxvalue[1])
for h in range(0,hbins):
    for s in range(0,sbins):
        binval=hist[h,s]
        intensity = int(binval*255/maxvalue[1])
        cv2.rectangle(histimg, (h*scale,s*scale),((h+1)*scale-1,(s+1)*scale-1),intensity,-1)

cv2.namedWindow('Source',1)
cv2.imshow('Source',src)

cv2.namedWindow('H-S histogram',1)
cv2.imshow('H-S histogram',histimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


