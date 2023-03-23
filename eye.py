import cv2
import numpy as np

face= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eyes_casacada = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml_')
if face_cascade.empty()
    raise I0Error('No se cargo tu bello rostro')
if eye_cascade.empty()
    raise I0Error('No se cargaron los oclayos')
    
cap=cv2.VideoCapture(0)
ds_factor = 0.5
while True:
    te, fame = cap read()
    frame= cv2.resize(frame,None, fx= ds_factor,
    gray = cv2.cvtColor(frame, cv2.Color_BGR2GRAY)
    faces= face_cascade.detect5Multiscale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        roi_gray = [y:y+h, x:x+w]
        roi_color= frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiscale(roy_gray)
        for (x_eye, y_eye, w_eye, h_eye) in eyes:
            center = (int(x_eye+0.5*w_eye + h_eye))
            radius = int(0.3 * (w_eye +h_eye))
            color = (0,255,0)
            thickness = 3
            cv2.circle(roi_color, center, radius, color, thicknes
    cv2.imshow('Detector de ojos', frame)
    c = cv2.waitKey(1)
    if c ==27:
        break
cap.release()
cv2.destroyAllWindows()
