class Coordinate():
    def __init__(self,  id):
        """
            The class defines all variables required to match IDC Catalogue fields.
            ID is the reference number for this programme
        """
        self.id = id
        self.x = None
        self.y = None
        self.depth = None        
        self.agency = None
        self.eventid = None
        self.date = None
        self.time = None
        self.magMw = None
        self.magM = None
        self.magMB = None
        self.magME = None
        self.magML = None
        self.magMLv = None
        self.magMS = None
        self.magMb = None
        self.magMjma = None
        self.magMs = None
        self.magMs1 = None
        self.magMs7 = None
        self.magMsz = None
        self.magMwp = None
        self.magmB = None
        self.magmb = None
        self.magmb1 = None
        self.magmb1mx = None
        self.magmbtmp = None
        self.magmslmx = None
        
        
        
    def getId(self):
        return self.id
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y

    def getDepth(self):
        return self.depth 
    
    def getAgency(self):
        return self.agentcy
        
    def getEventID(self):
        return self.eventid
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    
    
    def getMagMw(self):
        return self.magMw
    def getMagM(self):
        return self.magM
    def getMagMB(self):
        return self.magMB
    def getMagME(self):
        return self.magME
    def getMagML(self):
        return self.magML
    def getMagMLv(self):
        return self.magMLv
    def getMagMS(self):
        return self.magMS
    def getMagMb(self):
        return self.magMb
    def getMagMjma(self):
        return self.magMjma
    def getMagMs(self):
        return self.magMs
    def getMagMs1(self):
        return self.magMs1
    def getMagMs7(self):
        return self.magMs7
    def getMagMsz(self):
        return self.magMsz
    def getMagMwp(self):
        return self.magMwp
    def getMagmB(self):
        return self.magmB
    def getMagmb(self):
        return self.magmb
    def getMagmb1(self):
        return self.magmb1
    def getMagmb1mx(self):
        return self.mb1mx
    def getMagmbtmp(self):
        return self.magmbtmp
    def getMagmslmx(self):
        return self.magmslmx
    
    
        
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y   
        
    def setDepth(self, depth):
        self.depth = depth   
        
    def setAgency(self,  agentcy):
        self.agentcy = agentcy
    
    def setEventID(self,  eventid):
        self.eventid = eventid
        
    def setDate(self, date):
        self.date = date
        
    def setTime(self,  time):
        self.time = time
        
    def setMagMw(self, magMw):
        self.magMw = magMw
        
    def setMagM(self, magM):
        self.magM = magM
        
    def setMagMB(self, magMB):
        self.magMB = magMB
        
    def setMagME(self, magME):
        self.magME = magME
        
    def setMagML(self, magME):
        self.magML = magME
        
    def setMagMLv(self, magMLv):
        self.magMLv = magMLv
        
    def setMagMS(self, magMS):
        self.magMS = magMS
        
    def setMagMb(self, magMb):
        self.magMb = magMb
        
    def setMagMjma(self, magMjma):
        self.magMjma = magMjma
        
    def setMagMs(self, magMs):
        self.magMs = magMs
        
    def setMagMs1(self, magMs1):
        self.magMs1 = magMs1
        
    def setMagMs7(self, magMs7):
        self.magMs7 = magMs7
        
    def setMagMsz(self, magMsz):
        self.magMsz = magMsz
        
    def setMagMwp(self, magMwp):
        self.magMwp = magMwp
        
    def setMagmB(self, magmB):
        self.magmB = magmB
        
    def setMagmb(self, magmb):
        self.magmb = magmb
        
    def setMagmb1(self, magmb1):
        self.magmb1 = magmb1
        
    def setMagmb1mx(self, mb1mx):
        self.mb1mx = mb1mx
        
    def setMagmbtmp(self, magmbtmp):
        self.magmbtmp = magmbtmp
        
    def setMagmslmx(self, magmslmx):
        self.magmslmx = magmslmx