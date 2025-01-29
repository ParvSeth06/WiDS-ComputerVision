import cv2 as cv

img = cv.imread(r"photos\toa-heftiba-edJPD9XlNpo-unsplash.jpg")
def rescaled (img, scale=0.2):
    width,height = (int(img.shape[1] *scale),int(img.shape[0] *scale) )
    dimensions = (width, height)
    return cv.resize(img, dimensions,interpolation = cv.INTER_AREA)
image = rescaled(img)

# default colour space is BGR in openCV
# BGR to HSV
hsv =  cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("hsv image", hsv)

# BGR to LAB
lab =  cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow("lab image", lab)
# similarly we can do hsv or lab to bgr as well by COLOR_HSV2BGR


cv.imshow("img", image)
cv.waitKey(0)




# blurring tchniques


