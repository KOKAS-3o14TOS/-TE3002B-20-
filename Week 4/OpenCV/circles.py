import cv2
import numpy as np

image = cv2.imread('DetectCirclesExample_01.png')

cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# color verde
# lower = np.array([61, 67, 73])
# upper = np.array([102, 255, 255])

# amarillo
# lower = np.array([20, 100, 100])
# upper = np.array([30, 255, 255])

#rojo
lower = np.array([136, 87, 111])
upper = np.array([180, 255, 255])

hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsvFrame, lower, upper)
detected_output = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Masked image', detected_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(detected_output, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
canny = cv2.Canny(blur, 75, 250)

cv2.imshow('Canny image', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1.2, 50,
                           param1=10, param2=30, minRadius = 0, maxRadius=50)
circles = np.squeeze(circles).astype(int)

for c in circles:
    cv2.circle(image, (c[0], c[1]), c[2], (255, 0, 0), 2)
    cv2.circle(image, (c[0], c[1]), 2, (0, 255, 0), 5)

cv2.imshow('Detections', image)
cv2.waitKey(0)
cv2.destroyAllWindows()