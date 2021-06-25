import cv2

cap = cv2.VideoCapture('video/video1.mp4')

while(True):
    ret, img = cap.read(1)

    if ret == False:
        break

    # cv2.imshow("video",img)
    sobel = cv2.Sobel(img,0,1,0)
    cv2.imshow("sobel",sobel)


    if cv2.waitKey(1)&0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()