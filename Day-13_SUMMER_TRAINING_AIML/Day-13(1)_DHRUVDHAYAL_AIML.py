# Background Subtraction in a Video

import cv2

path = r'C:\Users\pc\Downloads\Day-13\vid_mpeg4.mp4'
vid = cv2.VideoCapture(path)

if not vid.isOpened():
    print("Error: Couldn't open video file.")
    exit()

back_subtractor = cv2.createBackgroundSubtractorMOG2(varThreshold=70, detectShadows=False)
back_subtractor2 = cv2.createBackgroundSubtractorKNN(dist2Threshold=5000, detectShadows=False)

while True:
    ret, frame = vid.read()

    if not ret:
        break  # No more frames to read, exit the loop

    mask_image = back_subtractor.apply(frame)
    mask2_image = back_subtractor2.apply(frame)

    cv2.imshow('mask', mask_image)
    cv2.imshow('mask2', mask2_image)
    cv2.imshow('org', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()