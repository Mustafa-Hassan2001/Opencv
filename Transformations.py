import cv2 as cv
import numpy as np

img = cv.imread('Images/park.jpg')
cv.imshow('park', img)

#1) translation shifting the images
#  --x --> left
#  --y --> up
#    x --> right
#    y --> down

def translation(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
  
# Translated = translation(img, -100, 100)
# cv.imshow('translated', Translated)

#2) rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) # 45 degree anti-clockwise

crotaed = rotate(img, -45) #45 degree clockwise

cv.imshow('rotated', rotated)
cv.imshow('crotated', crotaed)

rotated_rotated = rotate(crotaed, -45)
cv.imshow('rotated_roatated', rotated_rotated)

#3) resizing 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#4) flipping
# 0 --> filp vertically
# 1 --> flip horizontally
# -1 --> flip both vertically and horizontally

flip = cv.flip(img, -1)
cv.imshow('0flip', flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)




cv.waitKey(0)