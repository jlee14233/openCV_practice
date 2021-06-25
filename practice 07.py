## openCV practice/3(1/6-2/6)

import numpy as np
import cv2

background=np.zeros([500,500,3],dtype='uint8')
background[:,:,:]=255

## line -> 들어갈 이미지, 첫번째 포인트, 두번째 포인트, 색상, 굵기.
cv2.line(background,(10,10),(300,300),(0,0,255),5)
cv2.line(background,(20,10),(320,300),(255,255,4))


##circle -> 이미지, 원점, 반지름, 색상 , 굵기
## 굵기에서 -1를 사용하면 원이 채워짐.
cv2.circle(background,(250,250),50,(255,0,0),-1)
cv2.circle(background,(400,400),150,(0,0,200),3)

##rectangle -> 들어갈 이미지, 첫번째 포인트, 두번째 포인트, 색상, 굵기.
## 굵기에서 -1를 사용하면 사각형이 채워짐.
cv2.rectangle(background,(20,10),(320,300),(255,255,4),5)
cv2.rectangle(background,(10,10),(300,300),(0,0,255),-1)

##ellipse  #!-> 이미지, 중심좌표, 축 절반의 길이(장축,단축), 타원 기울기(1개의 변수)
##(타원을 그릴 길이)(0,360 ->100%모두 그림), 색상, 굵기

cv2.ellipse(background,(100,100),(100,50),30,0,360,(200,50,10),7)
cv2.ellipse(background,(300,300),(100,50),70,0,270,(89,89,255),-1)

## ellipse #2 -> 사각형 박스 안에 타원을 그려넣는 방법
## ellipse-> 이미지, 박스, 생상, 굵기,

cv2.ellipse(background,((150,150),(250,150),90),(0,255,0),4)



cv2.imshow('background',background)





cv2.waitKey(0)
cv2.destroyAllWindows()