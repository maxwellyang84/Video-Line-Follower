import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cap = cv.VideoCapture('raw_video_feed.mp4')

if cap.isOpened() == False:
    print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter('outpy.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while(True):
    ret, frame = cap.read()
    if ret == True:
        ret, frame = cv.threshold(frame, 100, 255, cv.THRESH_BINARY)
        x,y,z = frame.shape   
       
        grid = np.indices((1,y))
        
        center_x = np.sum((255-frame[x-1,:,0])*grid[1])/np.sum((255-frame[x-1, :,0]))
        
        cv.circle(frame, (int(center_x),int(frame_height)), 10, (0,0, 255), -1)
        out.write(frame)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()



