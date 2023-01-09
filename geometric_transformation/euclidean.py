import cv2
import numpy as np
image=cv2.imread('small.jpg')
# Euclidean-subset of affine
#    Same application process as affine transform

matrix=np.float32([[1,0,100],[0,1,100]])
# apply to image
euc_image=cv2.warpAffine(image,matrix,(image.shape[1]+100,image.shape[0]+100))
cv2.imshow('orig',image)
cv2.imshow('euc',euc_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


