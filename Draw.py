import numpy as np
import cv2

img = cv2.imread('Wallpaper.jpg', cv2.IMREAD_COLOR)


cv2.circle(img, (225,225), 74, (255,0,0), -1)
cv2.rectangle(img, (150,150), (300,300), (128,64,192), (5))
cv2.line(img, (150,150), (300,300), (128,64,192), (5))
pts = np.array([[200,300], [66,50], [400,150], [150,400], [900,900]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3) #True is to connect the first and last point

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'This polygon is shit', (400,130), font, 1, (128, 255, 64), 1, cv2.LINE_AA)



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
