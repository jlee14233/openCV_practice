import cv2
import numpy as np

print('-2_4/9---')

# img = cv2.imread("img/ball.png")
#
# cv2.imshow("ball",img)
#
# print(img.shape)
# y=313
# x=470
#
# for i in range(y//10*7,y//10*8):
#     for j in range(0,x):
#         b=img[i,j,0]
#         g=img[i,j,1]
#         r=img[i,j,2]
#
#         img[i,j,0]=255-b ##if b = 255  : 255-255 = 0 흰색에서 검은색으로 변경되기 때문에 색상반전 이미지가 생성되는 것.
#         img[i,j,1]=255-g
#         img[i,j,2]=255-r
# ## C++에서 위를 하기 위해서 쓰는 코드
# ## b= img.data[i*img.step + j+ img.elemSize() + 0];
# ## c++과 비교하면 굉장히 간단하게 나오는 것을
#
# cv2.imshow("banjeon",img)
#
#
#
print('-2_5/9---')

# ## 이미지 저장하기 및 채널별 저장하기.
# img=cv2.imread("img/poster.jpg")
# cv2.imwrite("img/trans_movie.png",img)
# cv2.imwrite("img/trans_movie.tif",img)
# cv2.imwrite("img/trans_movie.bmp",img)
#
# img2=cv2.Sobel(img,0,1,0)
#
# cv2.imshow("sobel",img2)
#
# b=img[:,:,0]
# g=img[:,:,1]
# r=img[:,:,2]
#
# cv2.imwrite("img/b.jpg",b)
# cv2.imwrite("img/r.jpg",r)
# cv2.imwrite("img/g.jpg",g)
#
# print(img.shape)
# print(b.shape)
#
print('-2_6/9---') ## 이 부분은 집에가서 다시 하기!
##비디오 파일 저장하기.
## gif파일도 동영상 읽기가 가능하니까 상관하지 말고 하면 될듯.



cap= cv2.VideoCapture('video/go5.gif')
fourcc=cv2.VideoWriter_fourcc(*'XVID')
w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)  ##이미지나 영상의 width를 불러오는 함수. 그냥 shape으로 확인하기 싫을 때 쓰기 좋음!
h=cap.get(cv2.CAP_PROP_FRAME_HEIGHT) ## 모르는 부분은 그냥 openCV 공홈에서 함수를 찾아보는것이 좋을 듯!

writer=cv2.VideoWriter("video/write_go5.avi",fourcc,30.0,(int(w),int(h)))



while(True):
    ret, img = cap.read(0)

    if ret == False:
        break

    # cv2.imshow("video",img)
    sobel = cv2.Sobel(img,0,1,0)
    # cv2.imshow("sobel",sobel)
    writer.write(sobel)

    if cv2.waitKey(1)&0xFF == 27:
        break


cv2.waitKey(0)
cap.release()
writer.release()
cv2.destroyAllWindows()
