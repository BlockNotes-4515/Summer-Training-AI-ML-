import joblib;
import cv2 ;
import numpy as np;
import matplotlib.pyplot as plt;

cam = cv2.VideoCapture(1)
path = "C:\\AIML\\datafiles\\haarcascade_frontalface_default (Practice).xml";
# face detector .
face_detector = cv2.CascadeClassifier(path).

model_path = 'C:\\AIML\datafiles\\orl_face_model_2.xml';
face_model = joblib.load(model_path);

frame=True;
count = 0;
while(frame):
    ret,im = cam.read();
    im_new = cv2.resize(im, (512,512));

    # covert the color (BGR) into grayscale
    gray_im = cv2.cvtColor(im_new,cv2.COLOR_BGR2GRAY);

    # run your classifier on the image.
    faces = face_detector.detectMultiScale(gray_im,scaleFactor=1.1,minNeighbors=10);

    # disply the bounding box on all the faces.
    for (dx,dy,w,h) in faces:
        cv2.rectangle(im_new, (dx,dy),(dx+w,dy+h),(0,0,255),2);
        cropped_im = cv2.resize((gray_im[dy-20:(dy+h)+40,dx:(dx+w)]),(92,112));
        lb = face_model.predict((cropped_im.reshape(1,-1)));
        cv2.putText(im_new,'user: '+str(lb[0]),(dx-5,dy-5),cv2.FONT_HERSHEY_SIMPLEX,1,color=(255,0,0),thickness=2)


    cv2.imshow('camera live feed', im_new)
    # desired button of your choice .
    if cv2.waitKey(1) & 0xFF == ord('q'):
        frame=False;
        break;
  

cam.release();
cv2.destroyAllWindows();