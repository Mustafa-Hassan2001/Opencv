import cv2 as cv

img = cv.imread('Images/park.jpg')
cv.imshow('Park', img)

#Blurrinig techniques

#Averaging Blur: it make  a window andd find center throught average of all pixels in window
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#Gaussian Blur: it is used to remove gaussian noise is is less effective than average in bluring but it is natual average
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#Mediam Blur: it is used to remove salt and pepper noise
median = cv.medianBlur(img, 7)
cv.imshow('median Blur', median)

#bilatral Blur: it is used to keep the edges sharp
bilatral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilatral Blur', bilatral)

cv.waitKey(0)