## openCV practice 3 (3/6~4/6 half)

import numpy as np
import cv2
import random


background=np.zeros([500,500,3],dtype='uint8')
background[:,:,:]=255
##polyline-> 이미지 파일, (pt를 다수로 넣음), True/False(닫힘,열림), 색상,굵기

point1= np.array([[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)]],dtype='int32')
point2= np.array([[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)],[random.randint(50,400),random.randint(50,400)]],dtype='int32')

##밑과 같은 형식으로 같이 그리는 것도 가능하당
cv2.polylines(background,[point1,point2],False,(0,255,0),3)
cv2.polylines(background,[point2],True,(255,0,0),3)

##채운 다각형을 만들 때 이렇게 만들 수 있음.
cv2.fillConvexPoly(background,point1,(0,0,0))
cv2.polylines(background,[point1],True,(255,0,0),3)

##TEXT -> 문자 넣기
## test -> 이미지, '글자' , 좌표값, 글씨체 , 폰트 크기, 폰트 색상, 폰트 두께

cv2.putText(background,'PYTHON',(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),3)


cv2.imshow('background',background)


cv2.waitKey(0)
cv2.destroyAllWindows()