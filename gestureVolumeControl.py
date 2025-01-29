import cv2
import time
import numpy as np
import handTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Set camera width and height
wCam, hCam = 640, 480

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Check if camera is opened properly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

pTime = 0  # Previous time for FPS calculation
detector = htm.handDetector(detectionCon=0.7)  # Initialize hand detector

# Initialize audio settings
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]  # Min and max volume levels

vol, volBar, volPer = 0, 400, 0  # Initialize volume variables

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Warning: Empty frame received, skipping...")
        continue  # Prevents errors if the frame is empty

    img = detector.findHands(img)  # Detect hands
    lmList = detector.findPosition(img, draw=False)  # Get landmarks

    if len(lmList) >= 9:  # Ensure that required landmarks exist
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]  # Index finger tip
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Center point between fingers

        # Draw circles and line on fingers
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        # Calculate distance between thumb and index finger
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert hand distance to volume range
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])

        # Set system volume
        volume.SetMasterVolumeLevel(vol, None)

        # Change color to green when fingers are close
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    else:
        print("Warning: Hand not detected properly.")

    # Draw volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime - pTime > 0 else 0
    pTime = cTime

    # Display FPS
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # Show output image
    cv2.imshow("Volume Control", img)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
