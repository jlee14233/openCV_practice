## openCV 3 6/6 trackBAR

def onChange(pos):
    pass
## onchange를 그냥 pass로 만들어줌

import cv2
import numpy as np

img = cv2.imread('img/dot.png')

slider=0
slider_max=15

cv2.namedWindow('img')
cv2.createTrackbar('Trackbar', 'img', slider, slider_max, onChange)
cv2.setTrackbarPos('Trackbar','img',7)
##pos를 setting.

while cv2.waitKey(1)!=ord('q'):
    track=cv2.getTrackbarPos('Trackbar','img')
    ## 여기에서 pos를 계속 해서 받아줘야지 변화가 생김.
    sobel=cv2.Sobel(img,0,1,0,ksize=(2*int(track)+1))
    cv2.imshow('img',sobel)

cv2.destroyAllWindows()