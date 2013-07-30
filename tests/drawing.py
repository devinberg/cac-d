'''
Created on Jul 28, 2013

@author: student
'''
from PyQt4 import QtGui



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
        
        rect = scene.addRect(250,250, 50, 50, pen, blueBrush)   
       
        point.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)     
        
        
        view.setScene(scene)
        view.setMaximumSize(400, 400)
        view.setBackgroundBrush(backgroundBrush)
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(view)
        #view.setMaximumSize()

        

  
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = drawing()
    window.setupUI()
    window.show()
    sys.exit(app.exec_())
        