import cv2
import numpy as np
image =cv2.imread('nature.jpg')

# filters
kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
blurring_kernel_3=np.ones((3,3),dtype=np.float32) / 9.0
blurring_kernel_11 = np.ones((11,11),dtype=np.float32) / 121.0

#apply filters

output1=cv2.filter2D(image,-1,kernel)
output2=cv2.filter2D(image,-1,blurring_kernel_3)
output3=cv2.filter2D(image,-1,blurring_kernel_11)

# show images
cv2.imshow('output',output1)
cv2.imshow('output 3 blur',output2)
cv2.imshow('output 11 blur',output3)
cv2.waitKey(0)
cv2.destroyAllWindows()

