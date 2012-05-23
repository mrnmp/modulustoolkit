"""
/***************************************************************************
 
 ModulusToolKit                                A QGIS plugin
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
 This script initializes the plugin, making it known to QGIS.
"""
from modulustoolkit import ModulusToolKit

def name():
    return "this is a ModulusToolKit plugin"
def description():
    return "my first plugin"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load ModulusToolKit class from file ModulusToolKit
    return ModulusToolKit(iface)
