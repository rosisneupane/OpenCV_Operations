import  cv2
import numpy as np
image=cv2.imread('nature.jpg')
size=15

kernel=np.zeros((size,size))
kernel[int((size-1)/2),:]=np.ones(size)
kernel=kernel/size

print(kernel)

output=cv2.filter2D(image,-1,kernel)
cv2.imshow('orig',image)
cv2.imshow('motion blur',output)
cv2.waitKey(0)
cv2.destroyAllWindows()