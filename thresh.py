import cv2 as cv
import numpy as np

img = cv.imread(r'photos\rescaled.jpg')
cv.imshow("img",img)


gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#simple thresholding 
threshold , thresh = cv.threshold(gray, 150 , 255, cv.THRESH_BINARY)   # 2nd attribute is threshold value, 3rd one is the value to which it should be converted if threshold value exceed
# threshold  =  150 , thresh =  binary image
cv.imshow("thrsshold", thresh)
threshold , thresh_inv = cv.threshold(gray, 150 , 255, cv.THRESH_BINARY_INV)
cv.imshow("thrsshold", thresh_inv)


# adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV,11,3 )
cv.imshow("threshold_adaptive_mean", adaptive_thresh)   # openCV computes the mean of neighbourhood pixels and sets a threshold value accordingly
adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,3 )
cv.imshow("threshold_adaptive_gaussian", adaptive_thresh_gaussian)

cv.waitKey(0)