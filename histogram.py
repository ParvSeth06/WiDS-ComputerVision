import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img  =cv.imread(r"photos\rescaled1.jpg") 
blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle =  cv.rectangle(blank, (150,150), (600,400), 255,thickness = -1)
mask = cv.bitwise_and(img, img,mask = rectangle)
cv.imshow("img", img)
# cv.imshow("mask", mask)

# gray_hist=  cv.calcHist([gray],[0], mask, [256], [0,256] ) 

# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('no of pixels')
# plt.plot(gray_hist )
# plt.xlim([0,256])
# plt.show()
# cv.imshow("img", img)
# cv.waitKey(0)

# color histogram

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)


