import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Red colour
    low_red=np.array([161,155,84])
    high_red=np.array([179,255,255])
    red_mask=cv2.inRange(hsv_frame,low_red,high_red)
    red=cv2.bitwise_and(frame,frame,mask=red_mask)
    
        
    #blue colour
    low_blue=np.array([94,80,2])
    high_blue=np.array([126,255,255])
    blue_mask=cv2.inRange(hsv_frame,low_blue,high_blue)
    blue=cv2.bitwise_and(frame,frame,mask=blue_mask)
    
        
    #yellow colour
    low_yellow=np.array([20,100,100])
    high_yellow=np.array([30,255,255])
    yellow_mask=cv2.inRange(hsv_frame,low_yellow,high_yellow)
    yellow=cv2.bitwise_and(frame,frame,mask=yellow_mask)
    
        
    #green colour
    low_green=np.array([25,52,72])
    high_green=np.array([102,255,255])
    green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    green=cv2.bitwise_and(frame,frame,mask=green_mask)
    
    #red,blue,green and yellow
    RB=cv2.bitwise_or(red,blue)
    RBG=cv2.bitwise_or(RB,green)
    RGBY=cv2.bitwise_or(RBG,yellow)
    
    cv2.rectangle(red,(0,0),(640,55),(0,0,255),cv2.FILLED)
    cv2.putText(red,"RED FILTER",(130,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    
    cv2.rectangle(blue,(0,0),(640,55),(255,0,0),cv2.FILLED)
    cv2.putText(blue,"BLUE FILTER",(130,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    
    cv2.rectangle(green,(0,0),(640,55),(0,255,0),cv2.FILLED)
    cv2.putText(green,"GREEN FILTER",(130,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    
    cv2.rectangle(yellow,(0,0),(640,55),(0,255,255),cv2.FILLED)
    cv2.putText(yellow,"YELLOW FILTER",(130,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    
    cv2.rectangle(RGBY,(0,0),(640,55),(255,255,255),cv2.FILLED)
    cv2.putText(RGBY,"RGBY FILTER",(130,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    
    cv2.imshow("RGBY",RGBY)
    cv2.imshow("original image",frame)
    cv2.imshow("red_mask",red)
    cv2.imshow("blue_mask",blue)
    cv2.imshow("green_mask",green)
    cv2.imshow("yellow_mask",yellow)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
