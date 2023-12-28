import cv2 as cv
import numpy as np

#crete a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
# uint8 is the datatype or data set of image
# cv.imshow('Blank', blank)

#1. paint the image by color    
# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

#color a certin portion  (200:330 and 300:400) are the range of pixles
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('boxred', blank)

#-------------------------------------------

#2. draw a rectangule
# cv.rectangle(blank, (10,0), (250, 250), (0,0,255), thickness=2) #thickness is the boder thvkness it will fill color to the boder
# cv.imshow('Rec', blank)

# cv.rectangle(blank, (0,0), (250, 500), (0,255,0), thickness=cv.FILLED) #this will filled the box also using -1
# cv.imshow('colorRec', blank)

#perfect shape
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1 )
# cv.imshow('colorRec', blank)

# img = cv.imread('Images/cat.jpg')
# cv.imshow('cat', img)

#-------------------------------------------

#3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,255,0), thickness=-1)
# cv.imshow('circle', blank)

#4. draw a line
# cv.line(blank, (100,300), (200, 300), (255, 255, 255), thickness=3)
# cv.imshow('line', blank)

#5. add text
cv.putText(blank, 'Hello world', (0, 255), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)


cv.waitKey(0)
