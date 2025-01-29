import cv2 as cv
import numpy as np

# Create a blank white canvas
canvas = np.ones((400, 400, 3), dtype="uint8") * 255

# Draw the yellow circular face
cv.circle(canvas, (200, 200), 150, (0, 255, 255), -1)  # Yellow face

# Draw the left eye
cv.circle(canvas, (140, 150), 15, (0, 0, 0), -1)  # Black circular left eye

# Draw the right eye (winking eye)
cv.ellipse(canvas, (240, 150), (25, 10), 0, 0, 180, (0, 0, 0), -1)  # Half ellipse for winking eye

# Draw the kissing lips
cv.ellipse(canvas, (170, 250), (25, 10), 0, 20, 160, (0, 0, 255), -1)  # Upper lip
cv.ellipse(canvas, (170, 250), (25, 10), 0, 200, 340, (0, 0, 255), -1)  # Lower lip

# Draw the heart (closer and moved upward)
# Left circle of the heart
cv.circle(canvas, (200, 240), 15, (0, 0, 255), -1)
# Right circle of the heart
cv.circle(canvas, (220, 240), 15, (0, 0, 255), -1)
# Triangle for the bottom part of the heart
pts = np.array([[190, 240], [230, 240], [210, 270]], np.int32)
cv.fillPoly(canvas, [pts], (0, 0, 255))

# Display the result
cv.imshow("Kissy Emoji", canvas)
cv.waitKey(0)
cv.destroyAllWindows()
