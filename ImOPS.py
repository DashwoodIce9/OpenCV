import numpy as np
import cv2

img = cv2.imread('Wallpaper.jpg', cv2.IMREAD_COLOR)

px = img[670,176]
print(px)
img[670,176]=[255,255,255]
print(px)   

ROI = img[100:150, 100:150]
img[100:150, 100:150] = [255,255,255]
print(ROI)

copy_area = img[500:600, 600:700]
img[0:100, 0:100] = copy_area

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

