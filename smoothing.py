import cv2 as cv
import numpy as np

img = cv.imread(r'photos\rescaled.jpg')   # the r tag is imp

# averaging : method 1
average = cv.blur(img, (7,7)) # applies the average method

# gaussian blur: weighted average : get less blur
gauss  = cv.GaussianBlur(img,(7,7),0)  # 3rd argument is standard deviation

# median blur
median =  cv.medianBlur(img, 7)


bilateral = cv.bilateralFilter(img, 5, 15 ,15)
cv.imshow("bilateral blur", bilateral)
cv.imshow("median", median)
cv.imshow("gauss", gauss)
cv.imshow("img", average )
cv.waitKey(0)