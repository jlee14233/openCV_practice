## constant operation openCV 4 (1/8~2/8)


import cv2
import numpy as np


img= cv2.imread('img/dot.png')
print(img.shape)
img_add = img+200
img_substract = img.copy()
#
# img_substract[:,:,0] = img[:,:,0]-10
# img_substract[:,:,1] = img[:,:,1]-40
# img_substract[:,:,2] = img[:,:,2]-200


img_mul = img.copy()

img_mul[:,:,0] = img[:,:,0]*10
img_mul[:,:,1] = img[:,:,1]*2
img_mul[:,:,2] = img[:,:,2]*1

img_div = img.copy()
img_div = img_div/2

# img_absdiff= img.copy()


cv2.imshow('img',img)
cv2.imshow('add',img_substract)
cv2.imshow('mul',img_mul)
cv2.imshow('div',img_div)
cv2.imshow('absdiff',img_absdiff)
cv2.waitKey(0)
cv2.destroyAllWindows()