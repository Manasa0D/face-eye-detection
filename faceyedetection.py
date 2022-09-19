#FACE DETECTION

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')#here we are importing haarcascade
img = cv2.imread('xxx.jpg')

while 1:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2,15)#1.2,15 tuning parameters

    for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#cv2.rectangle(src,start,pt,end,pt,color,thickness)
       
     eyes = eye_cascade.detectMultiScale(gray,1.1,15)#1.2,15 tuning parameters

     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,255,255),2)

    cv2.imshow('img',img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

    
