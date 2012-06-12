from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from coordinate import Coordinate

class SciPk(QObject):    
    def __init__(self):
        QObject.__init__(self)
        self.coords = []
        self.title = None

    def read(self,  file):
        """
        Reads formated data file and populate coordinate object.
        
        Following example show reading data from a formatted data input file. 
        This is produced when catalogue is passed through strip script
        1 2010/08/03 11:05:04.70 DJA 128.77 2.39 15.0 15054272 4.9 5.0 6.6 5.4 5.1   
        """
        try:
            first = True
            for line in open(file):
                if first:
                    self.title = line[4:]
                    first = False
                    continue
                
                self.data_val = line[11:21]
                self.agency_val = line[34:40]
                self.agency_val  = self.agency_val.strip()
                   
                coord = Coordinate(line[0:9])
                coord.setDate(self.data_val)
                coord.setTime(line[22:33])
                coord.setAgency(self.agency_val)
                coord.setX(line[41:50])
                coord.setY(line[51:61])
                coord.setDepth(line[63:68])
                coord.setEventID(line[70:78])
                coord.setMagMw(line[80:84])
                coord.setMagM(line[86:90])
                coord.setMagMB(line[92:96])
                coord.setMagME(line[98:102])
                coord.setMagML(line[104:108])
                coord.setMagMLv(line[110:114])
                coord.setMagMS(line[116:120])
                coord.setMagMb(line[122:126])
                coord.setMagMjma(line[128:132])
                coord.setMagMs(line[134:138])
                coord.setMagMs1(line[140:144])
                coord.setMagMs7(line[146:150])
                coord.setMagMsz(line[152:156])
                coord.setMagMwp(line[158:162])
                coord.setMagmB(line[164:168])
                coord.setMagmb(line[170:174])
                coord.setMagmb1(line[176:180])
                coord.setMagmb1mx(line[182:186])
                coord.setMagmbtmp(line[188:192])
                coord.setMagmslmx(line[194:198])
                                                  
                self.coords.append(coord)
                
            return True
                
        except IOError:
            QMessageBox.critical(None, "Import", str("Could not open file!")) 
            return  None    
          
    def getAttributeList(self):
        attrList = [ 
                        QgsField("EventId",  QVariant.String), 
                        QgsField("X Coordinate",  QVariant.Double), 
                        QgsField("Y Coordinate",  QVariant.Double),
                        QgsField("Magnitude",  QVariant.String),
                        QgsField("Depth",  QVariant.String),
                        QgsField("Agency",  QVariant.String),
                        QgsField("DateTime",  QVariant.String)
                    ]
        return attrList
 
    
    def getFeatures(self, datalist, agencyName, magType):
        """
        populates Qgis data with QGis attribute mapping detail
        """
        features = []    
        if magType:
            self.cmdstr = "coord.getMag" + str(magType) + "()"
                  
        for coord in datalist:
            mag = eval(self.cmdstr)
            if ( not mag.isspace() and coord.getAgency() == agencyName):  
                date_time = coord.getDate() + ":" + coord.getTime()  
               
                try:
                    feat = QgsFeature()
                    feat.setGeometry( QgsGeometry.fromPoint(QgsPoint(float(coord.getX()),  float(coord.getY()))) )
                    
                    feat.setAttributeMap( { 0 : QVariant(str(coord.getEventID())), 
                                                        1 : QVariant(float(coord.getX())), 
                                                        2 : QVariant(float(coord.getY())),
                                                        3 : QVariant(mag),
                                                        4 : QVariant(str(coord.getDepth())),
                                                        5 : QVariant(str(coord.getAgency())),
                                                        6 : QVariant(str(date_time)) })
                    features.append(feat)
                except ValueError:
                    continue
        return features
    
    def getCoords(self):
        return self.coords
        

