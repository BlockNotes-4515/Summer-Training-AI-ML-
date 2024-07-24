# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:24:44 2024

@author: student
"""

#=========================================== Using the KNN! ===============================================

import cv2;
import numpy as np;
import imutils;

#Copy the Path of the Vedio.
path = r"C:\Users\pc\Downloads\Day-13\VIRAT_S_050201_05_000890_000944.mp4";
                                                                                                                                                              
#Backgroud Substractor.
#bsck_gd = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3));
back_substractor = cv2.createBackgroundSubtractorKNN(dist2Threshold=8000);

#Create the Vedio Reader Object.
vid=cv2.VideoCapture(path);
print(vid);
print(vid.isOpened());
frame_counter=0;
#while(vid.isOpened()):
f=0;
while(f<=1000):
    f=f+1;
    val,frame=vid.read();
    #Vedio Background Substractions.
    mask_image = back_substractor.apply(frame);
    cnts=cv2.findContours(mask_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE);
    final_contours=imutils.grab_contours(cnts);

    for c in final_contours:
        area=cv2.contourArea(c);
        if(area>250):
            print(area);
            M=cv2.moments(c);
            cx=int(M['m10']/M['m00']);
            cy=int(M['m01']/M['m00']);
            cv2.drawContours(frame,[c],-1,(0,0,255));
            cv2.circle(frame,(cx,cy),4,(0,255,0));
    
    cv2.imshow('mask',mask_image);
    cv2.imshow('original',frame);
    if(cv2.waitKey(1)==ord('q')):
        break;
        
#Close the Values of the Objects.
vid.release();
cv2.destroyAllWindows();
print(frame_counter());
