import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank', blank)

# mask = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)
# masked = cv.bitwise_and(img, img, mask = mask)
# cv.imshow('Masked Image', masked)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('werid shape', weird_shape)

masked = cv.bitwise_and(img, img, mask = weird_shape)
cv.imshow('Werid Masked Image', masked)

cv.waitKey(0)