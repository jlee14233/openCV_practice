"""
openCV 4 7
noise generation
"""
#
# import cv2
# import numpy as np
# import random
#
# img=cv2.imread('img/design.jpg')
#
# img_dot=img.copy()
# img_gray=cv2.cvtColor(img_dot,cv2.COLOR_BGR2GRAY)
# gaussian_noise =np.empty((img_gray.shape[0],img_gray.shape[1]),dtype=img.dtype)
# mean = float(0)
# std = float(10)
# cv2.randn(gaussian_noise,mean,std)
#
# min,max,min_loc,max_loc= cv2.minMaxLoc(gaussian_noise)
# cv2.threshold(gaussian_noise,(min+max)//2,255,cv2.THRESH_BINARY)
#
# img_gray = img_gray+gaussian_noise
#
# ##openCV에서 비효율적이당
#
# # for i in range(0,100000):
# #     x= random.randint(0,img.shape[0]-1)
# #     y= random.randint(0,img.shape[1]-1)
# #
# #     img_dot[x,y,:]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
# cv2.imshow('origin',img)
# cv2.imshow('noise',img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

"""
openCV 4 -8
LUT/ loop 비교
"""

import numpy as np
import cv2
import time


# table=np.random.randint(255,size=(1000,1000))
# Lut=np.zeros((256,1),dtype='uint8')
#
# start=time.time()
# for i in range(0,256):
#     t= int(i*1.14)
#     if t > 255:
#         t=255
#
#     Lut[i]=t
#
# for i in range (0,1000):
#     for j in range (0,1000):
#         table[i,j] =  Lut[table[i,j]]
#
# end=time.time()
#
# print(end-start)
#
# table=np.random.randint(255,size=(1000,1000))
# start=time.time()
#
# for i in range(0,1000):
#     for j in range(0,1000):
#         t =table[i,j]*1.14
#         if t>255:
#             t=255
#         table[i,j]=t
#
# end=time.time()
#
# print(end-start)
#
# 한번에 처리하느냐, 나누어서 처리하느냐에 따라 속도 차이가 5배정도가 난다.
# 효율성에 큰 영향을 미치는 요소가 된다. 이걸 생각하면 앞의 부분도 수정이 가능!

"""
Look up table의 개념을 바탕으로 applycolormap을 이용할 수 있다.
영상의 픽셀값에 따라서 색상을 변화시킴
"""

img=cv2.imread('img/source.jpg')
cv2.namedWindow('img',0)
#
# start=time.time()
# img_color=cv2.applyColorMap(img,cv2.COLORMAP_JET)
# cv2.imshow('cool',img_color)
# end=time.time()
#

cv2.imshow('img',img)
# print(end-start)

Lut=np.zeros((256,1),dtype='uint8')
factor= int(256//2)

for i in range(0,256):
    Lut[i]=factor *(i//factor)
    print(Lut[i])

reduced=cv2.LUT(img,Lut)
cv2.imshow('reduced',reduced)

cv2.waitKey(0)
cv2.destroyAllWindows()

##gray의 색상과 BGR의 색상이 모두 applycolormap에선 동일하게 나옴.
## applycolormap의 처리 과정이 gray를 기본 바탕으로 하기 때문.
