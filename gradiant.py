import cv2 as cv
import numpy as np

img = cv.imread(r'photos\rescaled.jpg')
gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#laplacian    : its like pencil shading and then smudged
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap) 

# sobel : its like horizontal and vertical gradiant 
sobelx =  cv.Sobel(gray, cv .CV_64F, 1, 0)
sobely =  cv.Sobel(gray, cv.CV_64F, 0, 1)
canny  = cv.Canny(gray, 150, 175)

cv.imshow("canny2", canny)
cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)

cv.imshow("gray", gray)
cv.imshow("img", img)
cv.waitKey(0)