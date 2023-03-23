import cv2
filename='OG1.jpg'
def detect (filename):
 face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
 img = cv2.imread(filename)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(gray, 1.3,2)
 for(x,y,w,h) in faces:
   img=cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
 cv2.namedWindow('BTS Detected!!')
 cv2.imshow('BTS Detected!!', img)
# cv2.imwrite('./OG.jpg',img)
 cv2.waitKey(0)
 

detect(filename)

