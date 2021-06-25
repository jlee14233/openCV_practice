import numpy as np
import cv2

img= cv2.imread("img/character.jpg")
img2= img.copy() ## c++ 에서의 clone의 개념을 numpy에서는 copy로 표현하게 됨
banjeon = cv2.bitwise_not(img,img)


print(img.shape)
#img의 shape를 알았기 떄문에
#
# r=img2.copy()[x//4:x//2,y//4:y//2] ##작은수 -> 큰 수로 넘어가야 된다.
white= img.copy()
white[:,:]=255

double= np.concatenate([white,white],axis=1)

x=350
y=1240

cv2.imshow('white',double)

print(double.shape)

double[:,:y//2]=img
double[:,y//2:]=img2
#2가지 반전된 것과 아닌 것을 모두 담기 위해서 white로 마스크를 함,
#이후에 반전시킨 이미지와 아닌 이미지를 저장
#white의 크기를 concatenate를 이용해서 2배로 늘려줌.
#위의 영역을 위로 지정하고 shape를 이용하여, x,y의 값을 알아봄
#x,y의 값을 사용하여 리스트의 크기에 맞춰서 영역을 복사시켜줌.


cv2.imshow('copy',double)


# cv2.imshow('r',r)
# cv2.imshow('one',img2)
# cv2.imshow('img',banjeon)
cv2.waitKey(0)

cv2.destroyAllWindows()


## 350, 620, 3 (마지막은 색의 차원을 이야기 하는 것)
## 좌표화 할 수 있