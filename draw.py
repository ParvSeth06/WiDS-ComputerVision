import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')   # uint8 is the datatype of image , 500,500,3 = height,width,no of colour channels
# def rescaleFrame(frame, scale = 0.2) :
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0]* scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# img = cv.imread('photos\daniil-silantev--z3oVKe1Vtk-unsplash.jpg')
# resize_img =  rescaleFrame(img)
blank[200:300, 300:400] = 0,0,0   # this colours a certain part of img
#blank[:]=0,0,0
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)      # or instead of cv.FILLED we can write -1
# cv.imshow('blank', blank)
# cv.imshow('christmas', resize_img)
# cv.waitKey(0)

# drawing circles


cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2) , 50, (0,0,255), thickness = 3)
#cv.imshow("circle", blank)
#cv.waitKey(0)

cv.line(blank, (100,0), (blank.shape[0]//2 , blank.shape[1]//2), (0,255,0), thickness = 2)
# cv.imshow("line", blank)
# cv.waitKey(0)


# writing text on img
cv.putText(blank,"Fuck", (255,255), cv.FONT_HERSHEY_TRIPLEX, 2.0 , (0,255,0), 2)   # there are many other fonts
cv.imshow("TExt", blank)
cv.waitKey(0)