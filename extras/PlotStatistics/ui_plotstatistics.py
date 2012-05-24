# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plotstatistics.ui'
#
# Created: Fri May  4 10:39:32 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PlotStatistics(object):
    def setupUi(self, PlotStatistics):
        PlotStatistics.setObjectName(_fromUtf8("PlotStatistics"))
        PlotStatistics.resize(300, 188)
        PlotStatistics.setWindowTitle(QtGui.QApplication.translate("PlotStatistics", "PlotStatistics", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(PlotStatistics)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblLayer = QtGui.QLabel(PlotStatistics)
        self.lblLayer.setText(QtGui.QApplication.translate("PlotStatistics", "Seclect Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLayer.setObjectName(_fromUtf8("lblLayer"))
        self.gridLayout.addWidget(self.lblLayer, 0, 0, 1, 1)
        self.cmbBoxLayer = QtGui.QComboBox(PlotStatistics)
        self.cmbBoxLayer.setObjectName(_fromUtf8("cmbBoxLayer"))
        self.gridLayout.addWidget(self.cmbBoxLayer, 0, 1, 1, 2)
        self.lblFileName = QtGui.QLabel(PlotStatistics)
        self.lblFileName.setText(QtGui.QApplication.translate("PlotStatistics", "Output File Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFileName.setObjectName(_fromUtf8("lblFileName"))
        self.gridLayout.addWidget(self.lblFileName, 1, 0, 1, 1)
        self.outFileName = QtGui.QLineEdit(PlotStatistics)
        self.outFileName.setObjectName(_fromUtf8("outFileName"))
        self.gridLayout.addWidget(self.outFileName, 1, 1, 1, 2)
        self.lblPath = QtGui.QLabel(PlotStatistics)
        self.lblPath.setText(QtGui.QApplication.translate("PlotStatistics", "Output File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPath.setObjectName(_fromUtf8("lblPath"))
        self.gridLayout.addWidget(self.lblPath, 2, 0, 1, 1)
        self.outPathName = QtGui.QLineEdit(PlotStatistics)
        self.outPathName.setObjectName(_fromUtf8("outPathName"))
        self.gridLayout.addWidget(self.outPathName, 2, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(143, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.btnBrowse = QtGui.QPushButton(PlotStatistics)
        self.btnBrowse.setText(QtGui.QApplication.translate("PlotStatistics", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout.addWidget(self.btnBrowse, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(168, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(214, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PlotStatistics)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 2)

        self.retranslateUi(PlotStatistics)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PlotStatistics.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PlotStatistics.reject)
        QtCore.QMetaObject.connectSlotsByName(PlotStatistics)

    def retranslateUi(self, PlotStatistics):
        pass

