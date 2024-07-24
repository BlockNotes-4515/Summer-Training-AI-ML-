import cv2
import numpy as np
import imutils

# Define HSV thresholds for the color of interest
lowHSV = np.array([75, 100, 119])
highHSV = np.array([142, 218, 235])

# IP Webcam server address (replace with your device's IP and port)
ip_address = '192.168.137.188';  # Example: '192.168.0.100'
port = '4747';  # Example: '8080'
url = f'http://{ip_address}:{port}/video';  # Correctly formatted URL string

# Initialize video capture from IP Webcam stream
vid = cv2.VideoCapture(url)

frame_counter = 0
xCORR = []
yCORR = []

while vid.isOpened():
    ret, frame = vid.read()
    frame_counter += 1

    if ret:
        # Convert frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask using HSV thresholds
        mask = cv2.inRange(hsv, lowHSV, highHSV)

        # Find contours in the mask
        contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        # Process each contour
        for c in contours:
            area = cv2.contourArea(c)
            if area > 200:
                M = cv2.moments(c)
                if M['m00'] != 0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    cv2.drawContours(frame, [c], -1, (0, 0, 255), 2)
                    cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)
                    xCORR.append(cx)
                    yCORR.append(cy)
                    frame[cy, cx] = (0, 0, 255)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()
