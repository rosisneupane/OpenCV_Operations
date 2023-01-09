import cv2
import  numpy as np

image=cv2.imread('noisy.jpg')
rows,cols=image.shape[:2]

# kernel blurring
kernel_25 = np.ones((25,25),np.float32) / 625.0
output_kernel=cv2.filter2D(image,-1,kernel_25)

# Box filtering and blur function
output_blur=cv2.blur(image,(25,25))
output_box=cv2.boxFilter(image,-1,(5,5),normalize=False)

# Gaussian Blur
output_gaus=cv2.GaussianBlur(image,(5,5),0)
# Median Blur (reduction of noise)
output_median = cv2.medianBlur(image,5)

# Bilateral filtering (noise reduction and edge preservation)
output_bil = cv2.bilateralFilter(image,5 ,6,6)


# outputs
cv2.imshow('orginal',image)
cv2.imshow('kernel blurring',output_kernel)
cv2.imshow('kernel blurring',output_kernel)
cv2.imshow('blur_filter',output_blur)
cv2.imshow('box filter',output_box)
cv2.imshow('gaussian',output_gaus)
cv2.imshow('median',output_median)
cv2.imshow('bilateral',output_bil)


cv2.waitKey(0)
cv2.destroyAllWindows()
