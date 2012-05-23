"""
/***************************************************************************
 ToolkitDialog
                                 A QGIS plugin
 my first plugin
                             -------------------
        begin                : 2012-04-03
        copyright            : (C) 2012 by nimal m
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_modulustoolkit import Ui_ModulusToolKit
import os, sys


# create the dialog for zoom to point

class ToolkitDialog(QDialog, Ui_ModulusToolKit):

    def __init__(self, parent):

        QDialog.__init__(self, parent)
        self.setupUi(self)

        ## Get the params from last session.
        self.settings = QSettings("CatAIS","modulustoolkit")
        self.dirpath = self.settings.value("gui/dirpath")

    def initGui(self):
        pass
    
    def accept(self):
        
        if(self.inFile.text() == ""):
            QMessageBox.information(None, 'Information', str("Please specify a file."))
        else:          
            self.emit( SIGNAL("okClicked()") )
         
    
    @pyqtSignature("on_loadDataButton_clicked()")
    def on_loadDataButton_clicked(self):
        
        
        if(self.agentcyBox.currentText() == ""):
            QMessageBox.information(None, 'Information', str("Please select the Agentcy Type"))
        else:
            self.agentcyField = True
            
        if(self.magnitudeBox.currentText() == ""):
            QMessageBox.information(None, 'Information', str("Please select the  Magnitude Type"))
        else:
            self.magnitudeField = True
            
        if((self.agentcyField == True) and  (self.magnitudeField == True)): 

            self.emit( SIGNAL("loadClicked"), self.agentcyBox.currentText() , self.magnitudeBox.currentText() )
            
    def open(self, text):
              
            self.emit( SIGNAL("agentcySelected"), text )
            

    @pyqtSignature("on_btnBrowse_clicked()")   
    def on_btnBrowse_clicked(self):
        
        self.file = QFileDialog.getOpenFileName(self, "Import data",self.dirpath.toString(),"(*.*)")
        self.fileInfo = QFileInfo(self.file)
        self.inFile.setText(QString(self.fileInfo.absoluteFilePath()))
    
        self.settings.setValue("gui/dirpath", QVariant(self.fileInfo.absolutePath()))
	
