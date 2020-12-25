import cv2

cv2.namedWindow("preview")
video = cv2.VideoCapture(0)


if video.isOpened(): 
    rval, frame = video.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = video.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")