import cv2 as cv

# def changeRes(width, height):
#     #only live videos
#     capture.set(3, width)
#     capture.set(4, height)

# function of resize
# this can apply on all type of videos
def resacleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    deimensions = (width,height) 
    return cv.resize(frame, deimensions, interpolation=cv.INTER_AREA)

#read image
# img = cv.imread('Images/cat.jpg')
# cv.imshow('Cat', img)
# resized_image = resacleFrame(img)
# cv.imshow('Cat_resized', resized_image)
# cv.waitKey(0)


#read video
# capture = cv.VideoCapture('Videos/mobile.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = resacleFrame(frame, scale=0.2)

#     # frame_resized = resacleFrame(frame)

#     cv.imshow('video', frame)
#     cv.imshow('video_Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


