# MATRIX  계산
##
# 단위행렬 (Unit matrix): np.eye(n)
# 대각행렬 (Diagonal matrix): np.diag(x)
# 내적 (Dot product, Inner product): np.dot(a, b)
# 대각합 (Trace): np.trace(x)
# 행렬식 (Matrix Determinant): np.linalg.det(x)
# 역행렬 (Inverse of a matrix): np.linalg.inv(x)


import numpy as np
import cv2
print('7/9')
#
# a= np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.eye(3)
#
# print(a)
# print(b)
#
# print(a*b)
# print(np.dot(a,b))

##dot -> 내적,
##cross -> 외적.
##vector
# va=np.array([1,2,3])
# vb=np.array([0,0,1])
# #vc=np.array([,,])
#
# print(np.dot(va,vb))
# print(np.cross(va,vb))
#
# c= a.T
# print(c)
#
# # 대각합 (Trace): np.trace(x)
# print(np.trace(a))
#
# # 행렬식 (Matrix Determinant): np.linalg.det(x)
# print(np.linalg.det(a))
# # 역행렬 (Inverse of a matrix): np.linalg.inv(x)
# mb2=np.array([[1,3,1],[3,1,2],[1,2,3]])
# mc=np.linalg.inv(mb2)
#
# print(mb2)
# print(mc)
print('8/9')


# 연립방정식 해 풀기 (Solve a linear matrix equation): np.linalg.solve(a, b)
# 최소자승 해 풀기 (Compute the Least-squares solution): m, c = np.linalg.lstsq(A, y, rcond=None)[0]

###비동차 방정식 해 찾기

# a= np.array([[1,2,3],[4,5,2],[7,8,9]])
# b= np.array([14,32,52])
# x = np.linalg.solve(a, b)
# print(x)
# print(np.dot(a,x))

##여기 다시한번 해보기
# 고유값 (Eigenvalue), 고유벡터 (Eigenvector): w, v = np.linalg.eig(x)

f11=np.array([1,0.446,-0.56,0.446,1,-0.239,-0.56,-.239,1],dtype="float64")
data= np.reshape(f11,(3,3))
# print(data)
# w,v=np.linalg.eig(data) ##  w 고유값 v 고유벡터
# print(w)
# print(v)
# #
# b=np.eye(3)
# lamda=w*b
# print(lamda)
# print(data*lamda)
# print(v*w)

# 특이값 분해 (Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
u,s,vh=np.linalg.svd(data)
print(u)
print(s)
print(vh)
print()
# ???????????????????? 왜 안댐???
