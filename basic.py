import cv2 as cv

img = cv.imread('Images/park.jpg')
cv.imshow('Park', img)

#1. convert to graysacle
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#2. blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#3. edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#4. dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilated', dilated)

#5.eroding
eroded = cv.erode(dilated, (7,7), iterations=5)
cv.imshow('Eroded', eroded)

#6. resize
resized = cv.resize(img, (500, 500))
cv.imshow('resized', resized)

#7. croping
croped = img[20:400, 20:400]
cv.imshow('croped', croped)

cv.waitKey(0)
