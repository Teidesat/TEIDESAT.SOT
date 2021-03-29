'''
TEIDESAT
SPACECRAFT OPERATIONS

SATELLITE MODEL

@author: Elías Gabriel Ferrer Jorge
@author:
'''

class Sat:

    def __init__(self, name = "TEIDESAT", ID="TEIDESAT-I"):
        '''
        Constructor method Sat
        :param name: Name of Space Mission
        :param ID: ID of Satellite
        '''

        self.name  = name
        self.ID    = ID

        self.Orbit = []
        self.time  = 0

        self.Subsystems = []
        return

    def __str__(self):
        temp  = "INFORMATION: " + self.name          + "\n"
        temp += "-------------" + len(self.name)*"-" + "\n"
        temp += "Name   : " + self.name              + "\n"
        temp += "ID     : " + self.ID                + "\n"
        return temp

    def setOrbit(self, Orbit):
        self.Orbit = Orbit

