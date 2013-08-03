'''
Created on Jul 28, 2013

@author: student
'''
from PyQt4 import QtGui, QtCore



class drawing(QtGui.QWidget):
    ##Testing eGIT
    
    def setupUI(self):
        self.setMinimumSize(250,250)
        
        button = QtGui.QPushButton(self)
        button.setText("HELLO")
        
        view = QtGui.QGraphicsView()
        view.setMinimumSize(50,50)
        
        scene = QtGui.QGraphicsScene()
        
        
        redBrush = QtGui.QBrush(7,1)
        blueBrush = QtGui.QBrush(9,4)
        backgroundBrush = QtGui.QBrush(4,1)
        pen = QtGui.QPen(1)
        pen.setWidth(6)
        
        
        pim = QtGui.QPixmap('CAC-D.jpg')
        background = QtGui.QGraphicsPixmapItem(pim)
        background.setScale(.5)

        scene.addItem(background)
        
        
       
        
        
        scene.addEllipse(10,10,100,100, pen, redBrush)
        
        point = scene.addEllipse(1,1,1,1, pen, redBrush)
        
        rect2 = myRect(220,220,30,30)
        rect2.setPen(pen)
        rect2.setBrush(redBrush)
        rect2.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        scene.addItem(rect2)
        
        rect = scene.addRect(250,250, 50, 50, pen, blueBrush)   
       
        point.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
          
       
        
        view.setScene(scene)
        view.setMaximumSize(400, 400)
        view.setBackgroundBrush(backgroundBrush)
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(view)
        #view.setMaximumSize()
    
class myRect(QtGui.QGraphicsRectItem):
    resize = False
    move = False
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    
    def __init__(self, x,y,x2,y2):
        super(myRect, self).__init__(x, y, x2, y2)
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        
        self.update(x,y, x2, y2)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.resize = True
            print("true")
        if event.button() == QtCore.Qt.LeftButton:
            self.move = True
    
    
    
    
    def mouseMoveEvent(self, event):
        if self.resize == True:
            print("dragging")
            #self.update(self.x(),self.y(), event.scenePos().x(), event.scenePos().y())
            self.setRect(self.x,self.y, event.scenePos().x() - self.x, event.scenePos().y() - self.y)
            self.y2 = event.scenePos().y() - self.y
            self.x2 = event.scenePos().x() - self.x
            
        
        if self.move == True:
            self.setRect(event.scenePos().x(),event.scenePos().y(), self.x2, self.y2)
            self.x = event.scenePos().x()
            self.y = event.scenePos().y()
            
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.resize = False
            print("false")
        if event.button() == QtCore.Qt.LeftButton:
            self.move = False

        

  
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = drawing()
    window.setupUI()
    window.show()
    sys.exit(app.exec_())
        