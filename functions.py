import cv2 as cv
import numpy as np

img = cv.imread(r'photos\toa-heftiba-edJPD9XlNpo-unsplash.jpg')
def rescaling (frame, scale = 0.2) : 
    width= int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
image = rescaling(img)

cv.imshow("christmas", image)



gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   # FIRST FUNCTION
#cv.imshow("christmas", gray)
#blur = cv.GaussianBlur(image, (3,3), cv.BORDER_DEFAULT) # SECOND FUNCTION : the blur can be increased by increasing the kernel size , but it has to be odd number
canny = cv.Canny(image, 125,175)   # THIRD FUNCTION
#cv.imshow("edges", canny)
#cv.imshow("blurred", blur)
#dilated =  cv.dilate(canny, (3,3), iterations = 1)  # 4th function
eroded = cv.erode(canny,(3,3), iterations = 1)    # 5th : it is opposite of dilute
#cv.imshow("eroded", eroded)
#cv.imshow("Dilated", dilated)

# resizing image
resized = cv.resize(image, (800,800), interpolation = cv.INTER_CUBIC)  # 6th function

cropped = image[50:200, 300:500]    # 7th function: cropping

#cv.imshow("cropped", cropped)

def translate (img, x, y) :             # translation of image 
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x  --> left
# -y  --> up
# x  --> right
# y  --> down

translated  = translate(image, 100 , 100)
#cv.imshow("Translated", translated)

def rotation (img, angle , rotPoint =  None)  :
    height , width =  img.shape[:2]
    dimensions = (width, height)
    if rotPoint == None :
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotation(image, 90 )
cv.imshow("Rotated" , rotated)

# resizing
resized = cv.resize(image, (500,500), interpolation = cv.INTER_AREA)
cv.imshow("resized", resized)

# flipping
flipped =  cv.flip(image, 1)   # the second attribute in this is : 0, 1 or -1

# 0  --> vertical flip
# 1  --> horizontal flip
# -1  --> vertical and horizontal flip

cv.imshow("Flipped", flipped)
    

cv.waitKey(0)
