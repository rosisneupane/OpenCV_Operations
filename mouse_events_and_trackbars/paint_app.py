import cv2
import numpy as np

draw = False
mode = True
a, b = -1, -1


def on_change(value):
    global mode
    if value == 0:
        mode = True
    else:
        mode = False


def draw_circle(event, x, y, flags, params):
    global draw, mode, a, b
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        a, b = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            if mode == True:
                cv2.rectangle(img, (a, b), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (a, b), (a-x), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        if mode == True:
            cv2.rectangle(img, (a, b), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (a, b), (a-x), (0, 255, 0), -1)


cv2.namedWindow('track')
cv2.createTrackbar('shape', 'track', 0, 1, on_change)
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif (k == 27):
        break
cv2.destroyAllWindows()
