import cv2 as cv


def rescaleFrame (frame, scale = 0.1) :
    # works for images , videos and live videos
    width = int (frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions= (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) 

def changeRes (width, height) :
    # only works for live video
    capture.set(3, width)
    capture.set(4, height)    
    # 3 and 4 are the properties of the capture class, 10 represents brightness

capture =  cv.VideoCapture('photos\854982-hd_1280_720_25fps.mp4')
while True : 
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame)
    cv.imshow('MyKitty', frame)
    cv.imshow('MyKitty Resized', resized_frame)
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break
capture.release()
capture.destroyAllWindows()



# img = cv.imread(r'photos\freestocks-5867BKGyCu4-unsplash.jpg')
# resized_img =  rescaleFrame(img)

# cv.imshow('Christmas', resized_img)

# cv.waitKey(0)
