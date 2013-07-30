# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'captureImageTool.ui'
#
# Created: Tue Jul 16 16:53:55 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8  # @UndefinedVariable
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CaptureImageBox(object):
    def setupUi(self, CaptureImageBox):
        CaptureImageBox.setObjectName(_fromUtf8("CaptureImageBox"))
        CaptureImageBox.resize(693, 579)
        CaptureImageBox.setMinimumSize(QtCore.QSize(693, 579))
        CaptureImageBox.setMaximumSize(QtCore.QSize(693, 579))
        self.verticalLayout = QtGui.QVBoxLayout(CaptureImageBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(CaptureImageBox)
        self.frame.setMinimumSize(QtCore.QSize(661, 481))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.line = QtGui.QFrame(CaptureImageBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(CaptureImageBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(CaptureImageBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(CaptureImageBox)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CaptureImageBox)
        QtCore.QMetaObject.connectSlotsByName(CaptureImageBox)

    def retranslateUi(self, CaptureImageBox):
        CaptureImageBox.setWindowTitle(QtGui.QApplication.translate("CaptureImageBox", "Capture Image Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("CaptureImageBox", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("CaptureImageBox", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("CaptureImageBox", "Finish", None, QtGui.QApplication.UnicodeUTF8))

