import cv2
import numpy as np

img1 = cv2.imread('Batman.png')
img2 = cv2.imread('Joker.jpg')
img3 = cv2.imread('Joker Card.png')
print(type(img1))

add = img1+img2

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

add = cv2.add(img1,img2)

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

weighted = cv2.addWeighted(img1, 1.1, img2, 0.7, 5)

cv2.imshow('Weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows3,cols3,channels3 = img3.shape
rows2,cols2,channels2 = img2.shape
"""roi = img2[rows2-rows3:rows2,0:cols3]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 150, 255, cv2.THRESH_BINARY_INV)

#cv2.imshow('mask',mask)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img2_fg)"""
img2[rows2-rows3:rows2,0:cols3] = img3

cv2.imshow('res', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
