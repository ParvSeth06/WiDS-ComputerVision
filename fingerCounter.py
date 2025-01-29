import cv2
import time
import os
import handTrackingModule as htm

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "fingers"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

# Load images into overlayList
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(f"Loaded {len(overlayList)} images.")

pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        fingers = []
        
        # Check thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        # Check other fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalFingers = fingers.count(1)
        print(totalFingers)
        
        # Ensure overlay image exists for total fingers
        if totalFingers > 0 and totalFingers <= len(overlayList):
            overlay = overlayList[totalFingers - 1]
            
            # Get dimensions of overlay and resize it to fit the frame
            h, w, c = overlay.shape
            img_resized = cv2.resize(overlay, (wCam, hCam))  # Resize overlay to match frame size
            
            # Overlay the resized image
            img[0:hCam, 0:wCam] = img_resized  # Place the overlay image into the frame

            # Show the number of fingers detected on screen
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
    
    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime - pTime > 0 else 0
    pTime = cTime
    
    # Display FPS
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    # Show the image
    cv2.imshow("Image", img)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
