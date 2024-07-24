# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:24:44 2024

@author: student
"""
import cv2;
import numpy as np;

#Copy the Path of the Vedio.
path = r"C:\Users\pc\Downloads\Day-13\vid_mpeg4.mp4";

#Create the Vedio Reader Object.
vid=cv2.VideoCapture(path);

print(vid);
print(vid.isOpened());

while(vid.isOpened()):
    val,frame=vid.read();
    #If the frame is found to be captured.
    if(val):

        gray_im=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
        ycrcb_im=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb);
        hsv_im=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
    
    cv2.imshow('Frame',gray_im);
    cv2.imshow('HSV',hsv_im);
    cv2.imshow('YCrCb',ycrcb_im);
    cv2.imshow('Original',frame);
    if(cv2.waitKey(1)==ord('q')):
        break;
        
#Close the Values of the Objects.
vid.release();
cv2.destroyAllWindows();
print(frame_counter());