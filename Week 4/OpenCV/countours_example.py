import cv2
import numpy

image = cv2.imread('shapes.png')

cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
for contour in contours:
    if i == 0:
        i += 1
        continue

    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(image, [contour], 0, (0, 0, 255), 5)

    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    l = len(approx)
    if l == 3:
        cv2.putText(image, 'Triangle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    elif l == 4:
        cv2.putText(image, 'Quadrilateral', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    elif l == 5:
        cv2.putText(image, 'Pentagon', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    elif l == 6:
        cv2.putText(image, 'Hexagon', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    else:
        cv2.putText(image, 'Circle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

cv2.imshow('Detected figure', image)
cv2.waitKey(0)
cv2.destroyAllWindows()