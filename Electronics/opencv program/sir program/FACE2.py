import numpy as np
import cv2
import serial
import time
import struct
ser = serial.Serial('COM6',9600)
time.sleep(2)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=3,     
        minSize=(25, 25)
    )

   # display the image
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cx=int(x+w/2)
        cy=int(y+h/4)
        print(cx)
        print(cy)
        t1=cv2.line(img,(cx,0),(cx,720),(255,0,0),3)
        t2=cv2.line(img,(0,cy),(1280,cy),(255,0,0),3)
        #print(t1)
        #print(t2)
        ser.write(struct.pack('>BB', cx,cy))
                      
        
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]  
        cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
