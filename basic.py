import cv2 as cv
from cv2 import resize

img = cv.imread('photos/monkey.jpg')
cv.imshow('Animal', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=2)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroding', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropped = img[50:200 ,200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)