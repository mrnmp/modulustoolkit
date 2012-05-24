"""
/***************************************************************************
 PlotStatistics
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
import utils
# Import the code for the dialog
from plotstatisticsdialog import PlotStatisticsDialog
import numpy as np
import matplotlib.pylab as plt


class PlotStatistics:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
              
        self.canvas = self.iface.mapCanvas()
        self.mainWindow = self.iface.mainWindow()
        
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/plotstatistics/icon.png"), \
            "plot statistics", self.mainWindow)
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&plot statistics", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&plot statistics",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        """
        This initialise process called when QGIS started
        """
        # create and show the dialog
        self.dlg = PlotStatisticsDialog()
        # show the dialog
        self.dlg.show()       
        QObject.connect(self.dlg, SIGNAL("okClicked(QString, QString)"), self.readData) 
        
        
    def readData(self, layerName, outFile):
        """
        selected layer and output file name are passed in from dialog box, from the layer
        its attribute values are extracted to plot diagrams.
        Note this function currently extract data from Vector layer only.  
        """
        dateTimeList = []
        magList = []
        depList = []
           
        vlayer = utils.getVectorLayerByName( layerName )
              
        vprovider = vlayer.dataProvider()
        feat = QgsFeature()
        allAttrs = vprovider.attributeIndexes()
        vprovider.select( allAttrs )
        
        # field description
        myFields = vprovider.fields()
    
        while vprovider.nextFeature(feat):
            atmap = feat.attributeMap()
            for key, value in atmap.iteritems():
                if key == 6:
                    dateTime = "%-22s" % atmap[key].toString()
                    dateTimeList.append(dateTime)
                elif key == 3:
                    #mag = "%-22s" % atmap[key].toString()
                    mag = "%-22s" % atmap[key].toString()
                    magList.append(mag)
                elif key == 4: 
                    dep = "%-22s" % atmap[key].toString()
                    depList.append(dep)
                else:
                    pass
        
        self.plotTimes(dateTimeList,magList, depList, outFile)
        
                    
    def plotTimes(self, dateTimeList,magList, depList, outFile):
        """
        This function plots following diagrams calculating Bin/histogram values
        - date vs Frequency 
        - time vs Frequency
        - magnitude vs Frequency
        - depth vs Frequency
        """
        outputfile = str(outFile) + "_date_freq.png"
        timeoutputfile = str(outFile) + "_time_freq.png"
        magoutputfile = str(outFile) + "_mag_freq.png"
        depoutputfile = str(outFile) + "_dep_freq.png"
        
        yearList = []
        timeList = []
        magOutList = []
        depOutList = []
        
        for mag in magList:       
            mag_en = float(mag)  
            magOutList.append(mag_en)
            
        for dep in depList:       
            dep_en = float(dep)
            depOutList.append(dep_en)
        
        for dateTime in dateTimeList:
            year = dateTime[:4]
            time = dateTime[11:13]

            year_e = int(year)
            time_e = int(time)  
           
            yearList.append(year_e)
            timeList.append(time_e)
            
        # Frequency vs Year plot    
        startYear = min(yearList)
        endYear = max(yearList)
 
        step = 1 #bin width
        
        bins = np.arange(startYear, endYear, step)
        hist, edges = np.histogram(yearList, bins)
        
        plt.figure()
        plt.bar(bins[:-1]+0.5,hist, width=1, color='k')
        #plt.bar(bins[:-1]+0.02,hist, width=0.8, color='k')
        plt.axis([startYear, endYear, 0, 100])
        plt.ylabel('Number of Eruptions per Year')
        plt.xlabel('Year')
        plt.savefig(outputfile)
        
        
        # Frequency vs Time plot    
        startTime = min(timeList)
        endTime = max(timeList)
        step = 1 #bin width
      
        bins = np.arange(startTime, endTime, step)  
        hist, edges = np.histogram(timeList, bins)
        
        plt.figure()
        plt.bar(bins[:-1]+0.5,hist, width=1, color='k')
        plt.axis([startTime, endTime, 0, 100])
        plt.ylabel('Number of Eruptions per Time')
        plt.xlabel('Time')
        plt.savefig(timeoutputfile)        
        
              
        # Frequency vs Mag plot    
        startMag = min(magOutList)
        endMag = max(magOutList)
        
        step = 1 #bin width
        
        bins = np.arange(startMag, endMag, step)
        hist, edges = np.histogram(magOutList, bins)
        
        plt.figure()
        plt.bar(bins[:-1]+0.5,hist, width=0.8, color='k')
        plt.axis([startMag, endMag, 0, 50])
        plt.ylabel('Number of Eruptions ')
        plt.xlabel('Mag')
        plt.savefig(magoutputfile)  
        
        
        # Frequency vs Dep plot    
        startDep = min(depOutList)
        endDep = max(depOutList)
        step = 1 #bin width
        
        bins = np.arange(startDep, endDep, step)
        hist, edges = np.histogram(depOutList, bins)
        
        plt.figure()
        plt.bar(bins[:-1]+0.5,hist, width=0.8, color='k')
        #plt.bar(bins[:-1]+0.02,hist, width=0.8, color='k')
        plt.axis([startDep, endDep, 0, 50])
        plt.ylabel('Number of Eruptions')
        plt.xlabel('Depth')
        plt.savefig(depoutputfile)  
    
