import numpy as np
import cv2
image=cv2.imread('nature.jpg')

gaussian_blur=cv2.GaussianBlur(image,(7,7),2)

# sharpening

sharpened_1 = cv2.addWeighted(image,1.5,gaussian_blur,-0.5,0)
sharpened_2 = cv2.addWeighted(image,3.5,gaussian_blur,-2.5,0)
sharpened_3 = cv2.addWeighted(image,7.5,gaussian_blur,-6.5,0)

cv2.imshow('sharp1',sharpened_1)
cv2.imshow('sharp2',sharpened_2)
cv2.imshow('sharp3',sharpened_3)

cv2.waitKey(0)
cv2.destroyAllWindows()
