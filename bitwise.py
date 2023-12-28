import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle= cv.circle(blank.copy(), (200,200), 200, 255, -1)


cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


#bitwise AND  -> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_AND', bitwise_and)


#bitwise OR -> non and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_or', bitwise_or)

#bitwise XOR -> non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_xor', bitwise_xor)

#bitwise_not -> invert the bianry color
# bitwise_not = cv.bitwise_not(rectangle)
# cv.imshow('Bitwise_not', bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise_not', bitwise_not)




cv.waitKey(0)