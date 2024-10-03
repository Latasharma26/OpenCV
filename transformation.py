import cv2 as cv
import numpy as np

img=cv.imread("Photos/cat.jpg")
cv.imshow('Cat',img)

#translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


# -x left
# -y up
# y down
# x right

translated=translate(img,100,100)
cv.imshow('translated',translated)

translated=translate(img,-100,100)
cv.imshow('translated',translated)



# Rotation

def rotate(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint is None:
        rotpoint=(width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

# rotate=rotate(img,45)
# cv.imshow('rotated',rotate)
rotate=rotate(img,-45)
cv.imshow('rotated',rotate)


# flipping
flip=cv.flip(img,-1)
cv.imshow('flip',flip)

# cropping

cropped=img[200:400, 300:400]
cv.imshow("cropped",cropped)
cv.waitKey(0)
