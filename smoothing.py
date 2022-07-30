import cv2 as cv
import numpy as np

img = cv.imread('photos/monkey.jpg')
cv.imshow('Animal', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur',median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img, 50, 55, 85)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)