from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def getLayers():
    layermap = QgsMapLayerRegistry.instance().mapLayers()
    layerlist = []
    
    for name, layer in layermap.iteritems():
        print "name, layer", name, layer
        layerlist.append( unicode( layer.name() ))

    return layerlist


def getVectorLayerByName( myName ):
    layermap = QgsMapLayerRegistry.instance().mapLayers()
    for name, layer in layermap.iteritems():
        if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
            if layer.isValid():
                return layer
            else:
                return None  
            
            
def getFieldList( vlayer ):
    vprovider = vlayer.dataProvider()
    feat = QgsFeature()
    allAttrs = vprovider.attributeIndexes()
    vprovider.select( allAttrs )
    
    while vprovider.nextFeature(feat):
        #fetch geom
        #geom = feat.geometry()
        print "feat id", feat.id()
        print "Geom points", feat.geometry().asPoint()
        print "att map", feat.attributeMap() 
        atmap = feat.attributeMap()
        for key, value in atmap.iteritems():
            print "att map key, value===============", key, value.toString()
        
  
    myFields = vprovider.fields()
    return myFields      

