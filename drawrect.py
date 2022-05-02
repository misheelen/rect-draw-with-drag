import numpy as np
import cv2
import pickle
from os.path import exists
import sys

from recthandler import Rect 
import recthandler

file_name = "sample.pkl"

drawing = False # true if mouse is pressed
shape_mode = True # if True, draw rectangle. Press 'm' to  
box_selected = False 
active_rect = -1
ix, iy = -1, -1
current_id = 0

im_width = 640
im_height = 480
image = np.ones([im_height, im_width, 3], dtype=np.uint8)  # OR read an image using imread()
image *= 255
clone = image.copy()

def rectAssign(x1, y1, x2, y2):
    temp_rect = Rect(x1,y1,x2,y2)
    return temp_rect 

def onMouse(event, x, y, flags, param):
    global ix,iy,drawing,shape_mode,active_rect,image,clone,rect_list,current_id,box_selected

    if event == cv2.EVENT_LBUTTONDOWN:
        box_selected = False
        for i, rect in enumerate(rects): 
            is_inside = recthandler.pointInRect(x,y,rect)

            if is_inside:
                box_selected = True
                active_rect = i
                
            #     image = clone.copy()
            #     image = recthandler.drawSelectMarkers(image,rect)

        if box_selected == True:
            print("inside box:",active_rect)
        else:
            drawing = True
            ix,iy = x,y
            
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            image = clone.copy()
            if shape_mode == True:
                cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),1)
            else:
                cv2.circle(image,(x,y),5,(0,0,255),-1)

    if event == cv2.EVENT_LBUTTONUP:
        if drawing == True:
            if ix != x and iy != y:
                if shape_mode == True:
                    cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),1)
                    # cv2.putText(image,str(current_id),(ix,iy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,00),2,cv2.LINE_4)
                    new_rect = rectAssign(ix,iy,x,y)
                    rects.append(new_rect)
                else:
                    cv2.circle(image,(x,y),5,(0,0,255),-1)
        else:
            if box_selected:
                print("box select")
            else:
                print("empty select")
        drawing = False
    
        

if exists(file_name):
    open_file = open(file_name,"rb")
    if open_file is None:
        rects = []
    else: 
        rects = pickle.load(open_file)
else:
    rects = []
    


# Initialize the  drag object
w_name = "select region"

cv2.namedWindow(w_name)
cv2.setMouseCallback(w_name, onMouse)

# keep looping until rectangle finalized
while True:

    # draw save rectangles on the image 
    for id,rect in enumerate(rects):
        if active_rect == id:
            cv2.rectangle(image,(rect.x1,rect.y1),(rect.x2,rect.y2),(0,0,255),1)
            cv2.putText(image,str(id),(rect.x2,rect.y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_4)
        else:
            cv2.rectangle(image,(rect.x1,rect.y1),(rect.x2,rect.y2),(0,255,0),1)
            cv2.putText(image,str(id),(rect.x2,rect.y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_4)
        current_id = id

    # display the image
    cv2.imshow(w_name, image)
    
    # 
    key = cv2.waitKey(1) & 0xFF
    # return if 'Esc' key clicked
    if key == ord('m'):
        shape_mode = not shape_mode
        print("Drawing mode has changed")
    if key == ord('d'):
        print("Delete box")
        if box_selected:
            rects.pop(active_rect)
            active_rect = -1 
            box_selected = False
            image = clone.copy()
    elif key == ord('s'):
        open_file = open(file_name,"wb")
        pickle.dump(rects,open_file)
        open_file.close()
        print("Data has successfully saved to sample.pkl")
    elif key == 0x1b:
        print("Program has sucessfully finished")
        break

# close all open windows
cv2.destroyAllWindows()
