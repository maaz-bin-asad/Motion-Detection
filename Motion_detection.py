
import cv2
import numpy
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
_,frame1=cap.read()
_,frame2=cap.read()
cv2.namedWindow('Track')
cv2.createTrackbar('Thresh','Track',0,255,nothing)
cv2.createTrackbar('Threshh','Track',0,255,nothing)
while True:
    temp = cv2.absdiff(frame1, frame2)
    gray=cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
    blurr=cv2.GaussianBlur(gray,(5,5),0)
    pos1=cv2.getTrackbarPos('x','Track')
    pos2=cv2.getTrackbarPos('y','Track')
    _,thresh=cv2.threshold(gray,pos1,pos2,0)
    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,contours,-1,(0,0,512),3)
    cv2.imshow('Motion Detection',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()









