import cv2 as cv
import numpy as np
img = cv.imread('Images/park.jpg')
cv.imshow('Park', img)

b,r,g = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Red', r)
cv.imshow('Green', g)

#print the sahpe and dimension of image
print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

marged = cv.merge([b,r,g])
cv.imshow('marged', marged)


#create a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')  

blue = cv.merge([b, blank, blank])
red = cv.merge([blank, r, blank])
green =  cv.merge([blank, blank, g])

cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)



cv.waitKey(0)