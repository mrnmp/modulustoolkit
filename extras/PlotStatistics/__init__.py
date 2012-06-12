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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Plot Statistics"
def description():
    return "Qgis plugin tool for seismic plot statistics"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load PlotStatistics class from file PlotStatistics
    from plotstatistics import PlotStatistics
    return PlotStatistics(iface)
