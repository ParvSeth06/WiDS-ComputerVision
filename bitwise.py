import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255 , -1)
circle = cv.circle(blank.copy(), (200,200), 200 , 255, -1)   # color has to be denoted by one colour , not (x,y,z)
cv.imshow("rectanle", rectangle)
cv.imshow("circle",circle )
bitwise_and =cv.bitwise_and(rectangle, circle)

cv.imshow("and", bitwise_and)

# similarly do for the bitwise_or and bitwise_xor  and bitwise_not
#cv.imshow("blank", blank)


# MASKING

img = cv.imread(r"photos\rescaled.jpg")
blank1 = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow("img", img)
rect= cv.rectangle(blank1,(100,130), (600,480),255, -1 )
#cv.imshow("rectangle", rectangle)
masked = cv.bitwise_and(img, img,mask = rect)
cv.imshow("masked", masked)



cv.waitKey(0)