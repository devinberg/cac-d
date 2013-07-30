from PyQt4 import QtGui

import cncUI

import sys

app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
window.show()
GUI = cncUI.Ui_MainWindow()
GUI.setupUi(window)
sys.exit(app.exec_())
