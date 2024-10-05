import cv2

# Load the pre-trained Haar Cascade classifier for smile detection
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Read the input image
img = cv2.imread('Photos/group 2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect smiles
smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=5)

# Draw rectangles around the smiles
for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the output
cv2.imshow('Smile Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
