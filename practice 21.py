import cv2
import numpy as np
from matplotlib import pyplot as plt


"""
stretch 이미지 추가했음 50 ~ 100 사이의 영상 -> 다시 normalize 하는 형식으로 스트레치 할 것.
"""
# img= cv2.imread('img/mountain.jpg')
#
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('gray',0)
# cv2.namedWindow('stretch',0)
#
# stretch=cv2.normalize(gray,None,50,100,cv2.NORM_MINMAX)
# hist_gray=cv2.calcHist([gray],[0],None,[256],[0,256])
# hist_str=cv2.calcHist([stretch],[0],None,[256],[0,256])
#
# cv2.imshow('stretch',stretch)
# cv2.imshow('gray',gray)
# plt.plot(hist_gray)
# plt.plot(hist_str)
# plt.show()
# #
# # cv2.imwrite("img/stretch.jpg",stretch)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
stretch
"""
img=cv2.imread('img/stretch.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('equal',0)
cv2.namedWindow('versus',0)

stretch=cv2.normalize(gray,None,0,255,cv2.NORM_MINMAX)
hist_gray=cv2.calcHist([gray],[0],None,[256],[0,256])
hist_str=cv2.calcHist([stretch],[0],None,[256],[0,256])


"""
equlization (평탄화)
"""

equalize=cv2.equalizeHist(gray)
hist_equal=cv2.calcHist([equalize],[0],None,[256],[0,256])

cv2.imshow('versus',np.hstack((gray,stretch,equalize)))
# cv2.imshow('equal',equalize)
plt.plot(hist_gray)
plt.plot(hist_str)
plt.plot(hist_equal)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
