# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 01:04:37 2021

@author: 1520a
"""


import cv2

face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_classifier=cv2.CascadeClassifier("haarcascade_eye.xml")
smile_classifier=cv2.CascadeClassifier("haarcascade_smile.xml")

#It will read the first frame/image of the video
video=cv2.VideoCapture(0)

frame_width = int(video.get(3))
frame_height = int(video.get(4))
out = cv2.VideoWriter('output_FACE.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while True:
    #capture the first frame
    check,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #detect the faces from the video using detectMultiScale function
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    eyes=eye_classifier.detectMultiScale(gray,1.3,5)
    smile = smile_classifier.detectMultiScale(gray,1.3,10)
    print(faces)
    
    #drawing rectangle boundries for the detected face
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('Face detection', frame)
        out.write(frame)
        #picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        #cv2.imwrite(picname+".jpg",frame)
        
    #drawing rectangle boundries for the detected eyes
    for(ex,ey,ew,eh) in eyes:
        cv2.circle(frame, (ex+ew//2,ey+eh//2), ew//2 , (0,255,0), 3)
        cv2.imshow('Face detection', frame)
        out.write(frame)
    
    for(sx,sy,sw,sh) in smile:
        cv2.rectangle(frame, (sx,sy), (sx+sw,sy+sh), (0,0,255), 2)
        cv2.imshow('Face detection', frame)
        out.write(frame)
    for(sx,sy,sw,sh) in smile:
        cv2.rectangle(frame, (sx,sy), (sx+sw,sy+sh), (255,255,0), 2)
        cv2.imshow('Face detection', frame)
        out.write(frame)
    
    #waitKey(1)- for every 1 millisecond new frame will be captured
    Key=cv2.waitKey(1)
    if Key==ord('q'):
        #release the camera
        video.release()
        out.release()
        #destroy all windows
        cv2.destroyAllWindows()
        break