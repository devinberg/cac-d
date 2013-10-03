class stateBox():
#public
    text = ""
    
    def __init__():
        pass
    def setGridSpace(space):
        pass

#private
    _outerBorderColor = Qt.QColor.Black
    _outerBorderPen = QPen
    _location = [0,0]
    _dragStart = [0,0]
    _width = 250
    _height = 200

    _cornerDragStart = [0,0]
    _XcornerGrabBuffer = 20
    _YcornerGrabBuffer = 20
    _drawingWidth = _width - _XcornerGrabBuffer
    _drawingHeight = _height - _YcornerGrabBuffer
    _drawingOrigenX = _XcornerGrabBuffer
    _drawingOrigenY = _YcornerGrabBuffer

    _corners = [1, 2, 3, 4] #There are four corners that will be instantiated
    
    def boundingRect(self):
        #must re-implement this method
        pass
    def paint(self,painter, option, widget):
        #must re-implement this method
        pass
    def hoverEnterEvent(self, event):
        #must re-implement this method
        pass
    def hoverLeaveEvent(self, event):
        #must re-implement this method
        pass

    def mouseMoveEvent(self,event):
        #must re-implement this method
        pass
    def mousePressEvent(self, event):
        #must re-implement this method
        pass

    def sceneEventFilter(self, watched, event):
        corner = watched #watched is a cornergrabber
        if(corner == None):
            return False

        if event == None:
            return False

        if event.type() == QtGui.QEvent.GraphicsSceneMousePress:
            corner.setMouseState(cornerGrabber.kMouseDown)
            corner.mouseDownX() = event.pos().x()
            corner.mouseDownY() = event.pos().y()
        #elif event.type() == 
        

    def setCornerPositions():
        pass

    def adjustSize(x, y):
        self._width += x
        self._height += y

        self._drawingWidth = self._width - self.XcornerGrabBuffer
        self._drawingHeight = self._height - self.YcornerGrabBuffer
