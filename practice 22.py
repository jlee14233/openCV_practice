"""
project  ## data 수집용?
침입자 검출
background subtraction ==== 7/15
noise remove contour  // 7/15
morphology

moving average
upload image

multi threading
"""

import cv2
import numpy as np
import multiprocessing as mp

cap=cv2.VideoCapture(0)
cv2.namedWindow('cap')
# cv2.namedWindow('substract')
cv2.namedWindow('threshold')


print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print(type(cap))
old_frame = np.zeros((int(height),int(width),3),dtype=np.uint8)

thes_x=100

count=0
skip=50



while cv2.waitKey(1)!=ord('q'):

    count+=1
    if count<skip:
        print('skip count',count)
        continue

    if old_frame.all()==0:
        ret, old_frame = cap.read()
        bg_frame_binary = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
        continue

    ret2, frame=cap.read()
    binary=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    abs_frame=cv2.absdiff(bg_frame_binary,binary)

    ret, sub_frame= cv2.threshold(abs_frame,thes_x,255,cv2.THRESH_BINARY)
    con_frame=sub_frame.copy()
    contours, hierarchy = cv2.findContours(sub_frame.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,0,255),5,hierarchy=hierarchy)

    cv2.imshow('cap', frame)
    # cv2.imshow('substract',abs_frame)
    cv2.imshow('threshold',sub_frame)



cap.release()
cv2.destroyAllWindows()
