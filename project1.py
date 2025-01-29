import cv2 as cv
import numpy as np
import mediapipe as mp
import time
# use mediapipe ,  developed by google
# handtracking : palm detection and hand landmarks
# 20 pts on palm
pTime = 0
cTime = 0

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()   # we arent giving/ changing parameters here , because lets go with the default parameters
mpDraw = mp.solutions.drawing_utils
while True : 
    success , img =  cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks : 
        for handLms in results.multi_hand_landmarks : 
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark) :
                # print(id, lm)
                h, w, c = img.shape
                cx ,cy = int(lm.x*w), int(lm.y*h)
                print(id , cx, cy)
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,255,0), thickness = 3 )

    cv.imshow("image", img)
    cv.waitKey(1)

