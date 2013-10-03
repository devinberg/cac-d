'''
Created on Jul 31, 2013

@author: student
'''
from PyQt4 import QtGui, Qt

class cornerGrabber(QtGui.QGraphicsObject):
    
#Public
    mouseDownX = None
    mouseDownY = None
    
    graphicsItem = None
    
    kMouseReleased = 0
    kMouseDown = 1
    kMouseMoving = 2
#private
    _outerBorderColor = None
    _outerBorderPen = None
    _width = None
    _height = None
    _corner = None #is either 0,1,2, or 3
    _mouseButtonState = None 

    
   
    def __init__(self, parent = 0, corner = 0):
        self.mouseDownX = 0
        self.mouseDownY = 0
        self.graphicsItem = parent
        self._outerBorderColor(Qt.QColor.black())
        self._outerBorderPen = QtGui.QPen()
        self._width = 6
        self._height = 6
        self._corner = corner
        self._mouseButtonState = self.kMouseReleased
        
        self.setParentItem(parent)
        self._outerBorderPen.setWidth(2)
        self._outerBorderPen.setColor(self._outerBorderColor)
        
    def setMouseState(self, s):
        self._mouseButtonState = s
        
    def getMouseState(self):
        return self._mouseButtonState
    
    
    def getCorner(self):
        return self._corner
    
    

    
        