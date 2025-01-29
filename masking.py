import cv2 as cv
import numpy as np

img = cv.imread(r'photos\rescaled1.jpg')
blank = np.zeros(img.shape[:2], dtype= 'uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255 , -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

cv.imshow('blank', blank)
cv.imshow("img", img)
cv.waitKey(0)