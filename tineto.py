import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    bgr_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low_red = np.array([155,100,81])
    upper_red = np.array([179,255,255])
    red_mask = cv2.inRange(bgr_frame,low_red,upper_red)
    red = cv2.bitwise_and(frame,frame, mask=red_mask)

    low_green = np.array([25,52,72])
    upper_green = np.array([102,255,255])
    green_mask = cv2.inRange(bgr_frame,low_green,upper_green)
    green = cv2.bitwise_and(frame,frame,mask=green_mask)

    low_blue = np.array([94,80,2])
    upp_blue = np.array([126,255,255])
    blue_mask = cv2.inRange(bgr_frame,low_blue,upp_blue)
    blue = cv2.bitwise_and(frame,frame,mask=blue_mask)


    cv2.imshow("vedio" ,frame)
    cv2.imshow("red", red)
    cv2.imshow("blue", blue)
    cv2.imshow("green", green)
    #cv2.imshow("RGB_video",rgb_frame)
    #cv2.imshow("BGR_video",bgr_frame)
    key =cv2.waitKey(1)
    if key == ord("q"):
        break
