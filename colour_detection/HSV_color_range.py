import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("hue_min","Trackbars",0,179,empty)
cv2.createTrackbar("hue_max","Trackbars",179,179,empty)
cv2.createTrackbar("sat_min","Trackbars",0,255,empty)
cv2.createTrackbar("sat_max","Trackbars",255,255,empty)
cv2.createTrackbar("val_min","Trackbars",0,255,empty)
cv2.createTrackbar("val_max","Trackbars",255,255,empty)
cap=cv2.VideoCapture(0)
while True:
    #img=cv2.imread('face_filter.jpeg')
    #img=cv2.resize(img,(0,0),None,0.4,0.4)
    suc,img=cap.read()
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",imghsv)
    h_min=cv2.getTrackbarPos("hue_min","Trackbars")
    h_max = cv2.getTrackbarPos("hue_max", "Trackbars")
    s_min = cv2.getTrackbarPos("sat_min", "Trackbars")
    s_max = cv2.getTrackbarPos("sat_max", "Trackbars")
    v_min = cv2.getTrackbarPos("val_min", "Trackbars")
    v_max = cv2.getTrackbarPos("val_max", "Trackbars")
    lower=np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask=cv2.inRange(imghsv,lower,upper)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("result",res)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break



