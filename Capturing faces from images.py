import cv2
import sys
# set image path
imgPath = r'C:\Users\nezac\Desktop\DAB\Sem3\ML\Project\face.JPG'

img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# haarcascade classifier for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# defining hyper parameter for cascade
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

# Drawing ractangle around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    # Saving all the face images to local system
    cv2.imwrite(str(w) + str(h) + '_facesML.jpg', roi_color)

status = cv2.imwrite('faces_detected.jpg', img)