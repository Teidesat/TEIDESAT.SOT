'''
TEIDESAT
SPACECRAFT OPERATIONS

SUBSYSTEM MODEL

@author: Elías Gabriel Ferrer Jorge
@author:
'''

class Subsystem:

    def __init__(self, name, ID, version):
        '''
        Constructor method Subsystem
        :param name:
        :param ID:
        :param version:
        '''

        self.name              = name
        self.ID                = ID
        self.version           = version
        self.power_consumption = None
        self.mass              = None
        self.operation_mode    = None
        return

    def __str__(self):
        temp = "-------------" + len(self.name) * "-" + "\n"
        temp += "INFORMATION: " + self.name          + "\n"
        temp += "-------------" + len(self.name)*"-" + "\n"
        temp += "Name   : " + self.name              + "\n"
        temp += "ID     : " + self.ID                + "\n"
        temp += "version: " + self.version           + "\n"
        return temp
