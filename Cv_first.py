import cv2 as cv

# img = cv.imread('photos\lo-lindo-qDYEWEDtaTI-unsplash.jpg')

# cv.imshow('christmas', img)

capture =  cv.VideoCapture('photos\854982-hd_1280_720_25fps.mp4')
while True : 
    isTrue, frame = capture.read()
    cv.imshow('MyKitty', frame)
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break
capture.release()
capture.destroyAllWindows()
#cv.waitKey(0) # 0 means waiting for infinite time


# large images will go offscreen if the large img is  greater than the PC's screen


