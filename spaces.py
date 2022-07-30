import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/monkey.jpg')
cv.imshow('Animal', img)


#plt.imshow(img)
#plt.show()


#BGR to GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv -> bgr', hsv_bgr)

#L*a*b to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab -> bgr', lab_bgr)

cv.waitKey(0)
