"""
open CV 6 3/6- HSV
색상 모델
"""


import cv2
from matplotlib import pyplot as plt
import numpy as np
"""
# def calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
# def histogram(a, bins=10, range=None, normed=None, weights=None, density=None):
#
img=cv2.imread('img/joker.png')
hbins= [30]

channels = [0]
hranges=[0,180]

# bins =np.array(range(6,186,6))
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist, bins = np.histogram(hsv_img , 30 , [0,180])

# a = '#%02x%02x%02x' % (255,255,255)
#뒷부분안 color로 입력하면 hexa코드로 자동 변환이 된다,.

# bins =np.array(range(0,180,6))
# hist=cv2.calcHist([hsv_img],channels,None,hbins,hranges)
# print(hist)
# print(bins[0])
# a=[[[0,255,255]]]
# a=np.uint8(a)
### HSV색상코드를 RGB로 변환하기 위해서 위와 같이 해줘야 함.
# RGB=cv2.cvtColor(a,cv2.COLOR_HSV2RGB)
# print(RGB)

cvtcolor=[]
hexacode=[]
for i in bins[:-1]:
    t=int(i)
    color=[[[t,255,255]]]
    color=np.uint8(color)
    rgb=cv2.cvtColor(color,cv2.COLOR_HSV2RGB)
    cvtcolor.append(rgb)

for i in cvtcolor:
    a = '#%02x%02x%02x' % (i[0][0][0], i[0][0][1], i[0][0][2])
    hexacode.append(a)
print(hexacode)

plt.bar(bins[:-1],hist,width=6,color=hexacode)
cv2.imshow('img',img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

"""


"""
openCV 6 2D histogram

"""

img=cv2.imread('img/joker.png')
hbins= [30]
sbins= [32]
hranges=[0,180]
sranges=[0,256]
channels=[0,1]
