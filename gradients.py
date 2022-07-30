import cv2 as cv
import numpy as np

img = cv.imread('photos/monkey.jpg')
cv.imshow('Animal', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Laplaction
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel Combined',combined_sobel)
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y', sobely)

#canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)