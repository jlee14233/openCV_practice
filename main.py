## opencv_C++ to python opencv

import numpy as np
import cv2

## pixel의 데이터를 처리 하기 위해서
#
# mat = np.float64((3,3))
# testarray = np.array([10,20,30,40,50],dtype='f')
# # 구분	numpy 자료형	OpenCV 자료형
# # 8비트 unsigned 정수	np.uint8	cv2.CV_8U
# # 8비트 signed 정수	np.int8	cv2.CV_8S
# # 16비트 unsigned 정수	np.uint16	cv2.CV_16U
# # 16비트 signed 정수	np.int16	cv2.CV_16S
# # 32비트 signed 정수	np.int32	cv2.CV_32S
# # 32비트 실수	np.float32	cv2.CV_32F
# # 64비트 실스	np.float64	cv2.CV_64F
# #
# # chennel= np.array([range(i,i+5) for i in range(1,11)])
# # print(chennel)
# #
# # testsize = np.ones((3,4))
# # full= np.full((3,4),10)
#
# # a=np.full((4,2,3),10, dtype='int64')
# # print(a)
# # print(a.dtype)
# # for k in range (0,4):
# #     for i in range(0,2):
# #         for j in range(0,3):
# #             a[k, i, j] = (k+1)*(i+1)*(j+1)
# # print(a)
# # print(a[3,1,2])
# #
# # # print(full)
# # # print(testsize)
# # # print(mat)
# # # print(testarray)
# #
# # # print(cmtx)
# # img = np.full((3,3),10,dtype='float32')
# # cmtx= np.full((10,1,2),11,dtype='float64')
# #
# # print(img)
# # print(cmtx)
#
#
# #numpy에서 곱셈 연산은 각 요소끼리 곱셈으로 행해짐
# #행렬곱으로 나타내고 싶으면 dot을 이용할 것 *m.dot(m2)
# #역행렬을 나타내고 싶으면 np.linalg.inv(m2) 이런 형식으로 나타내면 됨.
# #행렬곱에 대한 것을 참조하려면 그냥 구글링 해서 찾아보기
#
# 단위행렬 (Unit matrix): np.eye(n)
# 대각행렬 (Diagonal matrix): np.diag(x)
# 내적 (Dot product, Inner product): np.dot(a, b)
# 대각합 (Trace): np.trace(x)
# 행렬식 (Matrix Determinant): np.linalg.det(x)
# 역행렬 (Inverse of a matrix): np.linalg.inv(x)
# 고유값 (Eigenvalue), 고유벡터 (Eigenvector): w, v = np.linalg.eig(x)
# 특이값 분해 (Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
# 연립방정식 해 풀기 (Solve a linear matrix equation): np.linalg.solve(a, b)
# 최소자승 해 풀기 (Compute the Least-squares solution): m, c = np.linalg.lstsq(A, y, rcond=None)[0]
#

# # 출처: https://rfriend.tistory.com/380 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]
# m = np.ones((3,3),dtype='float64')
# m = m*3
#
# m2 =np.array([[1,2,1],[0,1,1],[1,0,1]],dtype='float64')
# # print(m2)
# # print(m)
#
# # print(m+m2)
# # print(m-m2)
# # print(m*m2)
# # print(m2/m)
# #
# # print(m.dot(m2))
# # # print(np.linalg.inv(m2))
# # print(m2.T)
# # print(m2.dot(m2.T))
# # print(m+m2)
#
# m2= m+m2
# print(m2)
# for i in range(0,3):
#     for j in range(0,3):
#         print(m2[i,j])
#
# m2[2,2]=1000
# print(m2)
#

# img=cv2.imread("img/ball.jpg")
cap=cv2.VideoCapture("video/video1.mp4")
# fourcc=cv2.VideoWriter_fourcc(*"MP4V")
# frame = cv2.VideoWriter(cap,fourcc,30.0,(2736,1824)) ## 뒤의 숫자로 스케일 변환
##resizing 옵션
# cv2.namedWindow('img2')
# sobel = cv2.Sobel(img,0,1,0) ## sobel 엣지의 함수를 알아 둬야 함.
# cv2.namedWindow('video')

while True:
    img, ret = cap.read()
    #
    # if img != cv2.VideoCapture("video/video1.mp4"):
    #     print("mp4 files not open\n")


    cv2.imshow('video',img)
    c=cv2.waitKey(0)
    if c&0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# flip=cv2.flip(img)
# cv2.imshow('img2',img)
# while True:
# cv2.imshow('video',img)
#
# ### 실행 파일 자체를 불러 들일 수는 없는지 그게 궁금함.
# ###.exe파일에 접근 하는 방식을 찾는게 더 좋은 것이 그쪽에 맞는 이미지를 찾아낼 수 있음.
# key=cv2.waitKey(0)
# print(key)
    # if key==99:
    #     break
