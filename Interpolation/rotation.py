import cv2
image=cv2.imread('small.jpg')
height,width=image.shape[:2]

matrix=cv2.getRotationMatrix2D((width,height),10,1)

rotated=cv2.warpAffine(image,matrix,(width,height))
cv2.imshow('rotated',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()