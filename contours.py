import cv2 as cv
import numpy as np

img = cv.imread("photos\jon-flobrant-yFKkFPvUgXc-unsplash.jpg")
def rescaling(img , scale=0.15) :
    width =  int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation = cv.INTER_AREA)
rescaled = rescaling(img)
cv.imshow("img", rescaled)
#cv.imwrite("rescaled.jpg", rescaled) # this command is used for saving the img
gray = cv.cvtColor(rescaled, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175 )
cv.imshow("canny", canny)

ret,thresh = cv.threshold(rescaled,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours), " Contours found !")

blank = np.zeros(rescaled.shape, dtype='uint8')
cv.imshow("Blank", blank)
# we will draw contours on the blank sheet to visualize
cv.drawContours(blank, contours, -1,(0,0,255) ,2 )  # first attribute is the image over which contours will be drawn , 2nd is the list of contours, 3rd is the no of contours, 4th is colour, 5th is thickness
cv.imshow("drawn contours", blank)
cv.waitKey(0)
