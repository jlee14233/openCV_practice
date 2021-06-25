import numpy as np
import cv2


#gpgpu general purpose gpu
#cuda toolkit 처리

gpuimg, gpuimg_out = cv2.cuda_GpuMat

img=cv2.imread('img/brain.jpg')
cv2.imshow("img",img)
#
# gpuimg.upload(img)
# gpuimg_out=cv2.bitwise_not(gpuimg)
# imgout= gpuimg_out.download()
##현재 쿠다가 없어서 안되는걸지도?
#
# cv2.imshow("gpu",imgout)

cv2.waitKey(0)
cv2.destroyAllWindows()