# using opencv read the video file anf run it frame 
#by frame 
# in python environment
import cv2
import numpy as np
# copy the path of the video
#path = 'C:\\Users\\pc\\vid_mpeg4.mp4'
path = r"C:\Users\pc\Downloads\Day-13\VIRAT_S_050201_05_000890_000944.mp4";
# mouse click event 
def mouseRGB (event, x,y,flag,param):
    if(event==cv2.EVENT_FLAG_LBUTTON):
        colorB = frame[x,y,0]
        colorG = frame[x,y,1]
        colorR = frame[x,y,2]
        print('BGR values:',colorB,colorG,colorR)
        print('corr:',x,y)

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouseRGB)
# create the video reader object
vid = cv2.VideoCapture(path)
print(vid)
print(vid.isOpened())
frame_counter=0
val,frame=vid.read()
image_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.imshow('Frame',image_hsv)

# ROI - region of interest Bmin - 71 , Bmax = 142
# Gmin - 94 , Gmax 218
# R min=120 R max = 235
while(1):        
    if(cv2.waitKey(1)==ord('q')):
        break
    
vid.release() # close the object
cv2.destroyAllWindows()
        
print(frame_counter)    
