import cv2
import numpy as np

image=cv2.imread('test.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#edge detection
gradient_sobelx=cv2.Sobel(image,-1,1,0)
gradient_sobely=cv2.Sobel(image,-1,0,1)
gradient_sobelxy=cv2.addWeighted(gradient_sobelx,0.5,gradient_sobely,0.5,0)

gradient_laplacian=cv2.Laplacian(image,-1)

canny_output=cv2.Canny(image,80,150)

cv2.imshow('Sobel x', gradient_sobelx)
cv2.imshow('Sobel y', gradient_sobely)
cv2.imshow('Sobel X+y', gradient_sobelxy)
cv2.imshow('laplacian', gradient_laplacian)
cv2.imshow('Canny', canny_output)
cv2.waitKey(0)
cv2.destroyAllWindows()