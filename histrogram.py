import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# Histrogarm is use to analyze the distrbution of pixles 
# intensity weather it is gray sacle or color Images


#Gray Histrogarm

# img = cv.imread('Images/park.jpg')
# cv.imshow("Cat", img)

# blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2) , 100, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask = circle)
# cv.imshow('Msak', mask)


# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title('GrayScale Histrogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histrogram
img = cv.imread('Images/cat.jpg')
cv.imshow("Cat", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2) , 100, 255, -1)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Msak', masked)
plt.figure()
plt.title('Color Histrogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()
