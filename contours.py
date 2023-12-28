import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Method-1 it use canny
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny', canny)
# contour, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contour)} contour(s) found!')

# Method-2
#threshlod take the image and convert it into binary from
red, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
contour, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contour)} contour(s) found!')


#creating the blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)
cv.drawContours(blank, contour, -1, (0,0,255), 1)
cv.imshow('contour drawn', blank)

cv.waitKey(0)