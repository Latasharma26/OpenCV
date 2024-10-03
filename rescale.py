import cv2 as cv
# Reading image 
img=cv.imread("Photos/cat.jpg")
cv.imshow('Cat',img)
#resize of image
def rescaleFrame(frame,scale=0.75):
    # this method is for images, videos and live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)  
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    # for live video
    Capture.set(3,width)
    Capture.set(4,height)


# Reading videos
Capture=cv.VideoCapture("videos/dog.mp4")
while True:
    isTrue,frame=Capture.read()

    frame_resized=rescaleFrame(frame,scale=.2)#yha se size manage hogya frame ka scale=.2 mtlb sbse chota size
    cv.imshow('video',frame)
    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d') :
        break
Capture.release()
cv.destroyAllWindows()

cv.waitKey(0)