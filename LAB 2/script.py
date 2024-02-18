import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

def draw_circle(event,x,y,flags,param):
     if event == cv2.EVENT_RBUTTONDOWN:
         cv2.circle(img,(x,y),50,(0,0,255))
        
cv2.namedWindow(winname='drawing')
cv2.setMouseCallback('drawing',draw_circle)

while True:
    cv2.imshow('drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()