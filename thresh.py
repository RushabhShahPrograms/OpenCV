import cv2 as cv
from cv2 import threshold

img = cv.imread('photos/monkey.jpg')
cv.imshow('Animal', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive',adaptive_thresh)

cv.waitKey(0)