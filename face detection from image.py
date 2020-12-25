import cv2
import sys
# Create the haar cascade
facecascade = cv2.CascadeClassifier(r'C:\Users\nezac\Desktop\DAB\Sem3\ML\Project\haarcascade_frontalface_default.xml')
image = cv2.imread(r'C:\Users\nezac\Desktop\DAB\Sem3\ML\Project\face.jpg')
# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = facecascade.detectMultiScale(gray, 
	scaleFactor=1.1, 
	minNeighbors=4,
	minSize = (30, 30),
	flags = cv2.CASCADE_SCALE_IMAGE)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('output', image)
cv2.waitKey()