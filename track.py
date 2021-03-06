import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
cap.set(cv2.CAP_PROP_FPS,120)
print("FPS", cap.get(cv2.CAP_PROP_FPS))

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([90,64,98])
    upper_blue = np.array([145,255,255])

    lower_red = np.array([0, 0, 0])
    upper_red = np.array([19, 255, 255])

    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    mask = red_mask + blue_mask
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
