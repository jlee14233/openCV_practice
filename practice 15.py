"""
openCV lecture 4 6/8
"""
import numpy as np
import cv2

bg=np.zeros((500,1000,3),dtype=np.uint8)
bg1=np.zeros((500,1000,3),dtype=np.uint8)
bg2=np.zeros((500,1000,3),dtype=np.uint8)

img=cv2.imread('img/poster.jpg')

mask=np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype=np.uint8)
##data type까지 함께 맞춰주어야 한다.
lc=cv2.circle(mask,(400,250),250,(255,255,255),-1)

#
# mask=cv2.resize(bg1,dsize=(img.shape[1],img.shape[0]))

And=cv2.bitwise_and(mask,img)
# cv2.imshow('img',img)
# cv2.imshow('mask',mask)

cv2.imshow('and',And)


"""
rc=cv2.circle(bg2,(600,250),250,(255,255,255),-1)
 
And=cv2.bitwise_and(lc,rc)
Or=cv2.bitwise_or(lc,rc)
Xor=cv2.bitwise_xor(lc,rc)
Not=cv2.bitwise_not(lc)
 
cv2.imshow('and',And)
cv2.imshow('or',Or)
cv2.imshow('xor',Xor)
cv2.imshow('not',Not)
cv2.imshow('lc',lc)
cv2.imshow('rc',rc)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()