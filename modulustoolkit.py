"""
/***************************************************************************
 ModulusToolKit
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialise QT resources from file resources.py
import resources
from toolkitdialog import ToolkitDialog
from scipk import SciPk

import re


class ModulusToolKit:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.agencyDict = {}
        self.datalist = []
        

    def initGui(self):
    
        self.canvas = self.iface.mapCanvas()
        self.mainWindow = self.iface.mainWindow()

        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/modulustoolkit/icon.png"),"Modulus toolkit", self.mainWindow)
               
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Modulus toolkit", self.action)



    def unload(self):
        """
        Remove the plugin menu item and icon
        """
        self.iface.removePluginMenu("&Modulus ToolKit",self.action)
        self.iface.removeToolBarIcon(self.action)
        

    def loadMags(self, value1):
        """
        When Agency Combo box populated this method is called to list all available magnitude values
        """
        self.dlg.magnitudeBox.clear()
        self.value_selected_list = str(value1) 
        self.dlg.magnitudeBox.addItems(QStringList(self.agencyDict[self.value_selected_list]))
        
    
    
    def loadData(self, value1, value2):
        """
        This method is call when "oK" button from dialog to load data file 
        """
        self.selectedAgentcy = value1
        self.selectedMag     = value2
        self.SciPk = SciPk()
        # implement loading
        
        if (value1 and value2):
                file = self.dlg.inFile.text()
                fileInfo = QFileInfo(file)
                fileName = fileInfo.fileName()
                vl = QgsVectorLayer("Point", str(fileName), "memory")
                pr = vl.dataProvider()
                pr.addAttributes(self.SciPk.getAttributeList())
                pr.addFeatures(self.SciPk.getFeatures(self.datalist, value1, value2))
                vl.updateExtents()
                QgsMapLayerRegistry().instance().addMapLayer(vl, True)
                self.canvas.refresh()
                
        else:
                QMessageBox.warning(None, "Import", str("Error occured while reading file."))
        
            

    # run method that performs all the real work
    def run(self):

        # create and show the dialog
        self.dlg = ToolkitDialog(self.mainWindow)
        # show the dialog
        self.dlg.initGui()
        self.dlg.show()
  
        QObject.connect(self.dlg, SIGNAL("okClicked()"), self.readData) 
        QObject.connect(self.dlg, SIGNAL("agentcySelected"), self.loadMags) 
        QObject.connect(self.dlg, SIGNAL("loadClicked"), self.loadData)
 

    def readData(self):
        """
        Basically, the dictionary is created with agency has a Key and magnitude as value list 
        and populated throughout the iteration loop. 
        """
        
        self.SciPk = SciPk()
        try:
            file = self.dlg.inFile.text()
            
            fh = open(file)
            line = fh.readline()
            fh.close()

            type = line[0:2]
            
            if  len(type) > 0:
                           
                readfile = False
                readfile = self.SciPk.read(file)
                
                if readfile == True:
                
                    self.datalist = self.SciPk.getCoords()
                    for data in self.datalist:
                        
                        self.magList = []
                        self.agency = data.getAgency()

                        self.magList.append('Mw') if  not data.getMagMw().isspace() else None
                        self.magList.append('M')  if  not data.getMagM().isspace() else None
                        self.magList.append('MB') if  not data.getMagMB().isspace() else None
                        self.magList.append('ME') if  not data.getMagME().isspace() else None
                        self.magList.append('ML') if  not data.getMagML().isspace() else None
                        self.magList.append('MLv') if  not data.getMagMLv().isspace() else None
                        self.magList.append('MS') if  not data.getMagMS().isspace() else None
                        self.magList.append('Mb') if  not data.getMagMb().isspace() else None
                        self.magList.append('Mjma') if  not data.getMagMjma().isspace() else None
                        self.magList.append('Ms') if  not data.getMagMs().isspace() else None
                        self.magList.append('Ms1') if  not data.getMagMs1().isspace() else None
                        self.magList.append('Ms7') if  not data.getMagMs7().isspace() else None
                        self.magList.append('Msz') if  not data.getMagMsz().isspace() else None
                        self.magList.append('Mwp') if  not data.getMagMwp().isspace() else None
                        self.magList.append('mB') if  not data.getMagmB().isspace() else None
                        self.magList.append('mb') if  not data.getMagmb().isspace() else None
                        self.magList.append('mb1') if  not data.getMagmb1().isspace() else None
                        self.magList.append('mb1mx') if  not data.getMagmb1mx().isspace() else None
                        self.magList.append('mb1tmp') if  not data.getMagmbtmp().isspace() else None
                        self.magList.append('mslmx') if  not data.getMagmslmx().isspace() else None
                                            
                                         
                        if self.agencyDict.has_key(self.agency):
                            self.oldList = self.agencyDict[self.agency]
                               
                            for mag in self.magList:
                                if mag not in self.oldList:
                                    self.oldList.append(mag)     
                            self.agencyDict[self.agency] = self.oldList
                        else:
                            if len(self.agency) > 1:
                                self.agencyDict[self.agency] = self.magList
                                                                                                                   
                    for dictKey in self.agencyDict.keys():
                        self.dlg.agentcyBox.addItem(dictKey)
                                      
            else:
                QMessageBox.warning(None, "Import", str("Unknown format."))
                return
 

        except IOError:
            
            QMessageBox.critical(None, "Import", str("Could not open file!"))
            return
        
    def main(self):
        run(self)
        pass
           
    
if __name__ == '__main__':
    pass
    #main()
