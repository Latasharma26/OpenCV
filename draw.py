import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# Paint the image a certain color
# blank[:]=0,255,0 #rgb value 
# cv.imshow('Green',blank)

# # Paint the image a certain column
# blank[200:300 , 300:400]=0,0,255 #rgb value 
# cv.imshow('Red ',blank)

#draw a rectangle 
# cv.rectangle(img,p1,p2,rgb_value,thickness)
# cv.rectangle(blank,(0,0),(250,500),(250,0,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(250,0,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)

#draw a circle
# cv.circle(blank,(250,250),40,(0,0,250),thickness=2)
# cv.imshow('Circle',blank)

# draw a line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(250,0,0),thickness=3)
# cv.imshow("Line",blank)


# Write text
cv.putText(blank,"hello",(0,255),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Line',blank)

cv.waitKey(0)