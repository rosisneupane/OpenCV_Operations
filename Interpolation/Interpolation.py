import cv2

image=cv2.imread('small.jpg')
image_resized=cv2.resize(image,(300,300))
# # resizing using interpolation methods

image_linear=cv2.resize(image,None,fx=5.5,fy=5.5,interpolation=cv2.INTER_LINEAR)
image_cubic=cv2.resize(image,None,fx=5.5,fy=5.5,interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original',image)
cv2.imshow('Linear',image_linear)
cv2.imshow('Cubic',image_cubic)

cv2.waitKey(0)
cv2.destroyAllWindows()
