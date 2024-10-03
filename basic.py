import cv2 as cv
img=cv.imread("Photos/cat.jpg")
cv.imshow('Cat',img)

# Basic function of opencv

# coverting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny edges',canny)

# dilating the image 
dilated=cv.dilate(canny,(3,3),iterations=2)
cv.imshow("dilated",dilated)



#  eroded
eroded=cv.erode(dilated,(3,3),iterations=2)
cv.imshow("eroded",eroded)


# resize used in shrining the image

# resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA) #by default-shrink the image
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) #high quality return 
cv.imshow('resized',resized)

# cropping
cropped=img[50:200,200:400]
cv.imshow("cropped",cropped)
cv.waitKey(0)