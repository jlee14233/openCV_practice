## openCV 3 6/6 video canny

import cv2
import numpy as np

def onChange(x):
    pass

cap= cv2.VideoCapture(0)
cv2.namedWindow('cap')

cv2.createTrackbar('Trackbar', 'cap', 0, 255, onChange)
cv2.setTrackbarPos('Trackbar','cap', 7)

while cv2.waitKey(1)!=ord('q'):
    ret, frame= cap.read(cv2.IMREAD_GRAYSCALE)

    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #canny edges는 흑백만 가능
    track = cv2.getTrackbarPos('Trackbar', 'cap')
    # blur= cv2.GaussianBlur(gray,(5,5),1.5)
    ##blur의 사이즈는 홀수의 정방행렬만 가능.
    edges = cv2.Canny(gray,track,255)

    cv2.imshow('cap',edges)



cap.release()
cv2.destroyAllWindows()