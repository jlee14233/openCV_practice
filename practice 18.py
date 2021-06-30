"""
openCV 6 histogram(1/6-3/6)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img= cv2.imread('img/human.png')


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',gray)

# histogram을 직접 그릴 떄 #
print(gray.shape)
# width=gray.shape[1]
# height=gray.shape[0]

hists, bins = np.histogram(gray,256, [0,256])

print(hists)
# histogram_buffer=np.zeros((256,1),np.uint8)
# # print(len(histogram_buffer))
# maxValue=0
# # print(histogram_buffer)
# for i in range (0,width):
#     for j in range(0,height):
#         v=gray[j,i]
#         print(v)
#         histogram_buffer[v] +=1
#
# for i in range(0,255):
#     if maxValue<histogram_buffer[i]:
#         maxValue=histogram_buffer[i]

# normalize=cv2.normalize(hist,None,0,255,cv2.NORM_MINMAX)

# # print(maxValue)
# maxvalue=max(histogram_buffer)
#
# # print(histogram_buffer)
# # histogram=np.zeros((255,maxvalue+1),np.uint8)


hist=cv2.calcHist([gray],[0],None,[256],[0,256])
print(hist)
normalize1=cv2.normalize(hist,None,0,10,cv2.NORM_MINMAX)
normalize=cv2.normalize(hists,None,0,10,cv2.NORM_MINMAX)

# print(hist)
# plt.plot(hist)
# plt.plot(hists)
# plt.plot(histogram_buffer)
plt.plot(normalize)
plt.plot(normalize1)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()