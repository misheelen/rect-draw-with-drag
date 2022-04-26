import sys

import cv2  # Opencv ver 4.5.5 
import numpy as np
import pickle

# Set recursion limit
sys.setrecursionlimit(10 ** 9)

file_name = "sample.pkl"

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to  
ix, iy = -1, -1

im_width = 640
im_height = 480
image = np.ones([im_height, im_width, 3], dtype=np.uint8)  # OR read an image using imread()
image *= 255
clone = image.copy()

class Rect:
    x1 = None
    y1 = None
    x2 = None 
    y2 = None 

def rectAssign(x1, y1, x2, y2):
    temp_rect = Rect()
    temp_rect.x1,temp_rect.y1 = x1,y1
    temp_rect.x2,temp_rect.y2 = x2,y2

    return temp_rect 

def onMouse(event, x, y, flags, param):
    global ix,iy,drawing,mode,image,clone,rect_list

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            image = clone.copy()
            if mode == True:
                cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),1)
            else:
                cv2.circle(image,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),1)
            new_rect = rectAssign(ix,iy,x,y)
            rects.append(new_rect)
        else:
            cv2.circle(image,(x,y),5,(0,0,255),-1)

open_file = open(file_name,"rb")
if open_file is None:
    rects = []
else:
    rects = pickle.load(open_file)
    print(rects[0])


# Initialize the  drag object
w_name = "select region"

cv2.namedWindow(w_name)
cv2.setMouseCallback(w_name, onMouse)

# keep looping until rectangle finalized
while True:

    # draw save rectangles on the image 
    for rect in rects:
        cv2.rectangle(image,(rect.x1,rect.y1),(rect.x2,rect.y2),(0,255,0),1)

    # display the image
    cv2.imshow(w_name, image)
    key = cv2.waitKey(1) & 0xFF

    # return if 'Esc' key clicked
    if key == ord('m'):
        mode = not mode
    elif key == ord('s'):
        open_file = open(file_name,"wb")
        pickle.dump(rects,open_file)
        open_file.close()
    elif key == 0x1b:
        break

# close all open windows
cv2.destroyAllWindows()
