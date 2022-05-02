import cv2  # Opencv ver 4.5.5 

class Rect:
    sBlk = 2
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 
        self.y2 = y2
         

def pointInRect(pX, pY, rect):
    if rect.x1 <= pX <= rect.x2 and rect.y1 <= pY <= rect.y2:
        return True
    else:
        return False

def drawSelectMarkers(image, dragRect):
    """
    Draw markers on the dragged rectangle
    """
    # Top-Left
    cv2.rectangle(image, (dragRect.x1 - dragRect.sBlk,
                          dragRect.y1 - dragRect.sBlk),
                  (dragRect.x1 - dragRect.sBlk + dragRect.sBlk * 2,
                   dragRect.y1 - dragRect.sBlk + dragRect.sBlk * 2),
                  (0, 255, 0), 2)
    # Top-Right
    cv2.rectangle(image, (dragRect.x2 - dragRect.sBlk,
                          dragRect.y1 - dragRect.sBlk),
                  (dragRect.x2 - dragRect.sBlk + dragRect.sBlk * 2,
                   dragRect.y2 - dragRect.sBlk + dragRect.sBlk * 2),
                  (0, 255, 0), 2)
    # Bottom-Left
    cv2.rectangle(image, (dragRect.x1 - dragRect.sBlk,
                          dragRect.y2 - dragRect.sBlk),
                  (dragRect.x1 - dragRect.sBlk + dragRect.sBlk * 2,
                   dragRect.y2 - dragRect.sBlk + dragRect.sBlk * 2),
                  (0, 255, 0), 2)
    # Bottom-Right
    cv2.rectangle(image, (dragRect.x2 - dragRect.sBlk,
                          dragRect.y2 - dragRect.sBlk),
                  (dragRect.x2 - dragRect.sBlk + dragRect.sBlk * 2,
                   dragRect.y2 - dragRect.sBlk + dragRect.sBlk * 2),
                  (0, 255, 0), 2)
    return image