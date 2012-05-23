# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modulustoolkit.ui'
#
# Created: Wed May  2 16:26:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ModulusToolKit(object):
    def setupUi(self, ModulusToolKit):
        ModulusToolKit.setObjectName(_fromUtf8("ModulusToolKit"))
        ModulusToolKit.resize(310, 238)
        ModulusToolKit.setWindowTitle(QtGui.QApplication.translate("ModulusToolKit", "ModulusToolKit", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(ModulusToolKit)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.commentlabel = QtGui.QLabel(ModulusToolKit)
        self.commentlabel.setText(QtGui.QApplication.translate("ModulusToolKit", "Geoscience Seismic Activity Analyse Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.commentlabel.setObjectName(_fromUtf8("commentlabel"))
        self.gridLayout.addWidget(self.commentlabel, 0, 0, 1, 5)
        self.fileLabel = QtGui.QLabel(ModulusToolKit)
        self.fileLabel.setText(QtGui.QApplication.translate("ModulusToolKit", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.gridLayout.addWidget(self.fileLabel, 1, 0, 1, 1)
        self.inFile = QtGui.QLineEdit(ModulusToolKit)
        self.inFile.setObjectName(_fromUtf8("inFile"))
        self.gridLayout.addWidget(self.inFile, 1, 1, 1, 3)
        self.btnBrowse = QtGui.QPushButton(ModulusToolKit)
        self.btnBrowse.setText(QtGui.QApplication.translate("ModulusToolKit", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout.addWidget(self.btnBrowse, 1, 4, 1, 2)
        self.agentcyLabel = QtGui.QLabel(ModulusToolKit)
        self.agentcyLabel.setText(QtGui.QApplication.translate("ModulusToolKit", "Agentcy", None, QtGui.QApplication.UnicodeUTF8))
        self.agentcyLabel.setObjectName(_fromUtf8("agentcyLabel"))
        self.gridLayout.addWidget(self.agentcyLabel, 2, 0, 1, 1)
        self.agentcyBox = QtGui.QComboBox(ModulusToolKit)
        self.agentcyBox.setObjectName(_fromUtf8("agentcyBox"))
        self.gridLayout.addWidget(self.agentcyBox, 2, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(142, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 3)
        self.magLabel = QtGui.QLabel(ModulusToolKit)
        self.magLabel.setText(QtGui.QApplication.translate("ModulusToolKit", "Magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.magLabel.setObjectName(_fromUtf8("magLabel"))
        self.gridLayout.addWidget(self.magLabel, 3, 0, 1, 1)
        self.magnitudeBox = QtGui.QComboBox(ModulusToolKit)
        self.magnitudeBox.setObjectName(_fromUtf8("magnitudeBox"))
        self.gridLayout.addWidget(self.magnitudeBox, 3, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(97, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(97, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(ModulusToolKit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(37, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(98, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 2)
        self.loadDataButton = QtGui.QPushButton(ModulusToolKit)
        self.loadDataButton.setText(QtGui.QApplication.translate("ModulusToolKit", "Load Data", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataButton.setObjectName(_fromUtf8("loadDataButton"))
        self.gridLayout.addWidget(self.loadDataButton, 5, 2, 1, 3)
        spacerItem5 = QtGui.QSpacerItem(37, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 5, 1, 1)

        self.retranslateUi(ModulusToolKit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ModulusToolKit.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ModulusToolKit.reject)
        QtCore.QObject.connect(self.agentcyBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), ModulusToolKit.open)
        QtCore.QMetaObject.connectSlotsByName(ModulusToolKit)

    def retranslateUi(self, ModulusToolKit):
        pass

