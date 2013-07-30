from PyQt4 import QtGui

import cncUI

import sys
from cncBase import cncBase

app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
window.show()
base = cncBase()
GUI = cncUI.Ui_MainWindow(base)
GUI.setupUi(window)
sys.exit(app.exec_())
