"""
/***************************************************************************
 PlotStatisticsDialog
                                 A QGIS plugin
 Qgis plugin tool for seismic plot statistics
                             -------------------
        begin                : 2012-05-03
        copyright            : (C) 2012 by Nimal M
        email                : nimal.mariampillai@ga.gov.au
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.core import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from ui_plotstatistics import Ui_PlotStatistics
import os, sys
import utils

# create the dialog for zoom to point
class PlotStatisticsDialog(QtGui.QDialog, Ui_PlotStatistics):
    
    def __init__(self):
            
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.layers = []
        self.layers = utils.getLayers()

        #for name in self.layers:
            #print "layers=", name
        self.cmbBoxLayer.addItems(sorted(self.layers))  
        
        ## Get the params from last session.
        self.settings = QSettings("ModulusToolkit","plotstatistics")
        self.dirpath = self.settings.value("gui/dirpath")
                
        
    def initGui(self):
        
        pass
        
    def accept(self):
        """
        This function is called when ok button pressed on dialog box,
        error generated when layer or output file name is empty 
        """
        if(self.cmbBoxLayer.currentText() == "" and self.fileInfo.absoluteFilePath() == ""):
            QMessageBox.information(None, 'Information', str("Layer Name or Filename, Path can not be empty"))
        else:          
            self.emit( SIGNAL("okClicked(QString, QString)"), self.cmbBoxLayer.currentText(), self.fileInfo.absoluteFilePath())
           
            
    
    @pyqtSignature("on_btnBrowse_clicked()")   
    def on_btnBrowse_clicked(self):
        """
        This function allow the user to select output file directory path
        """     
        self.dir = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.outPathName.setText(self.dir)
        
        if(self.outFileName.text() == ""):
            QMessageBox.information(None, 'Information', str("File Name can not be empty"))
        else:          
            self.file = self.outFileName.displayText()
            self.fileInfo = QFileInfo(self.file)
            self.outPathName.setText(QString(self.fileInfo.absoluteFilePath()))

    
