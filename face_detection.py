import cv2 as cv
import numpy as np

img = cv.imread(r"photos\bollywood.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.imshow("face detection", img)

haar_cascade =cv.CascadeClassifier('haar_face.xml')    # cascade classifier is very sensitive to noise, it mufght detect neck or stomach too as face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)   # increased minNeighbors to 6 , coz there as noise 
print(f'number of faces detected = {len(faces_rect)}')
# increasing the size of image also changes result
for (x,y,w,h) in faces_rect :
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow("marked", img)
cv.waitKey(0)


