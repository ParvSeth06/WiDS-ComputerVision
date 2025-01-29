import cv2
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw=True):
        if img is None:
            return None, []  # Handle case where the frame is empty

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                
                if draw:
                    img = self.fancyDraw(img, bbox)
                    cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                                (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_PLAIN,
                                2, (255, 0, 255), 2)
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=5, rt=1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h

        cv2.rectangle(img, bbox, (255, 0, 255), rt)
        # Drawing corner lines
        corner_color = (255, 0, 255)

        # Top Left
        cv2.line(img, (x, y), (x + l, y), corner_color, t)
        cv2.line(img, (x, y), (x, y + l), corner_color, t)

        # Top Right
        cv2.line(img, (x1, y), (x1 - l, y), corner_color, t)
        cv2.line(img, (x1, y), (x1, y + l), corner_color, t)

        # Bottom Left
        cv2.line(img, (x, y1), (x + l, y1), corner_color, t)
        cv2.line(img, (x, y1), (x, y1 - l), corner_color, t)

        # Bottom Right
        cv2.line(img, (x1, y1), (x1 - l, y1), corner_color, t)
        cv2.line(img, (x1, y1), (x1, y1 - l), corner_color, t)
        
        return img

def main():
    cap = cv2.VideoCapture(r"photos\rescaled_video.mp4")
    pTime = time.time()
    detector = FaceDetector()

    while cap.isOpened():
        success, img = cap.read()

        if not success or img is None:
            print("End of video or cannot read frame.")
            break  # Exit the loop when the video ends

        img, bboxs = detector.findFaces(img)
        print(bboxs)

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0  # Avoid division by zero
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        cv2.imshow("Face Detection", img)

        # Press 'q' to exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
