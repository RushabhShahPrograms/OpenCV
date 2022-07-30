import cv2 as cv


#for images
img = cv.imread('photos/monkey.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

#for videos
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()