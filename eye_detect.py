import cv2

# Load the pre-trained Haar Cascade classifier for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Read the input image
img = cv2.imread('Photos/lady.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect eyes
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

# Draw rectangles around the eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the output
cv2.imshow('Eye Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
