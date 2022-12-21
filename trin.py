import cv2
import numpy as np 


img = cv2.imread("picturs/baloons.jpg",-1)
img = cv2.resize(img,(500,500))



hsv_fram = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

low_red = np.array([155,100,81])
high_red = np.array([179,255,255])
red_mask = cv2.inRange(hsv_fram, low_red, high_red)
red = cv2.bitwise_and(img,img , mask=red_mask)



low_green = np.array([30, 52, 72])
high_green = np.array([102,255,255])
green_mask = cv2.inRange(hsv_fram, low_green, high_green)
green = cv2.bitwise_and(img,img , mask=green_mask)

low_blue = np.array([94, 80, 2])
high_blue = np.array([126,255,255])
blue_mask = cv2.inRange(hsv_fram, low_blue, high_blue)
blue = cv2.bitwise_and(img,img , mask=blue_mask)

low = np.array([0, 42, 0])
high = np.array([179,255,255])
mask = cv2.inRange(hsv_fram, low, high)
result = cv2.bitwise_and(img,img , mask=mask)


cv2.imshow("images",img)
cv2.imshow("red", red)
# #cv2.imshow("red_mask", red_mask)
# cv2.imshow("blue",blue)
cv2.imshow("green", green)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()