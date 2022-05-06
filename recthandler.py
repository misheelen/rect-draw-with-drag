import cv2  # Opencv ver 4.5.5 

class Rect:
    sBlk = 2

    # Marker flags by positions
    TL = False
    TR = False
    BL = False
    BR = False

    # Set rect to zero width and height
    outX = 0
    outY = 0
    outW = 0
    outH = 0

    # Set anchor rect 
    anchorX = 0
    anchorY = 0
    anchorW = 0
    anchorH = 0

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

def calcDragCorner(eX,eY,dragObj):
    if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                dragObj.outRect.y - dragObj.sBlk,
                dragObj.sBlk * 2, dragObj.sBlk * 2):
        dragObj.TL = True
        return
    if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                dragObj.outRect.y - dragObj.sBlk,
                dragObj.sBlk * 2, dragObj.sBlk * 2):
        dragObj.TR = True
        return
    if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                dragObj.sBlk * 2, dragObj.sBlk * 2):
        dragObj.BL = True
        return
    if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                dragObj.sBlk * 2, dragObj.sBlk * 2):
        dragObj.BR = True
        return

    # # This has to be below all of the other conditions
    # if recthandler.pointInRect(eX, eY, dragObj.outRect.x, dragObj.outRect.y, dragObj.outRect.w, dragObj.outRect.h):
    #     dragObj.anchor.x = eX - dragObj.outRect.x
    #     dragObj.anchor.w = dragObj.outRect.w - dragObj.anchor.x
    #     dragObj.anchor.y = eY - dragObj.outRect.y
    #     dragObj.anchor.h = dragObj.outRect.h - dragObj.anchor.y
    #     dragObj.hold = True

def drawSelectMarkers(image, dragRect):
    """
    Draw markers on the dragged rectangle
    """
    # Top-Left
    cv2.rectangle(image, (dragRect.x1 - dragRect.sBlk,
                          dragRect.y1 - dragRect.sBlk),
                  (dragRect.x1 + dragRect.sBlk,
                   dragRect.y1 + dragRect.sBlk),
                  (0, 255, 0), 2)
    # Top-Right
    cv2.rectangle(image, (dragRect.x2 - dragRect.sBlk,
                          dragRect.y1 - dragRect.sBlk),
                  (dragRect.x2 + dragRect.sBlk,
                   dragRect.y1 + dragRect.sBlk),
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