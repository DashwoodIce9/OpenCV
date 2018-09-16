import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")
retval, threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(greyscaled, 15, 255, cv2.THRESH_BINARY)
retval3, otsu = cv2.threshold(greyscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
gauss = cv2.adaptiveThreshold(
    greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1
)


cv2.imshow("original", img)
cv2.imshow("threshold", threshold)
cv2.imshow("Greyscaled", threshold2)
cv2.imshow("Gauss", gauss)
cv2.imshow("Otsu", otsu)
cv2.waitKey(0)