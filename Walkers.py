
# Create our body classifier
# Initiate video capture for video file
# Loop once video is successfully loaded
# Read first frame
#Convert Each Frame into Grayscale
# Pass frame to our body classifier
# Extract bounding boxes for any bodies identifiedimport cv2

import cv2
face_cascade = cv2.CascadeClassifier("/Users/abhijoy/Desktop/Visual Studio: Coding/Python/faceDetection/PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml")


cap = cv2.VideoCapture('/Users/abhijoy/Desktop/Visual Studio: Coding/Python/faceDetection/PRO-106-ProjectTemplate-main/walking.avi')


while True:
    
    
    ret, frame = cap.read()
    greyScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(greyScale, 1.2, 3)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow("image", frame)
        cv2.waitKey(0)

   
    
    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
