'''

TEIDESAT
SPACECRAFT OPERATIONS

TEIDESAT . SPACECRAFT OPERATION TOOL
  _______ ______ _____ _____  ______  _____      _______        _____  ____ _______
 |__   __|  ____|_   _|  __ \|  ____|/ ____|  /\|__   __|      / ____|/ __ \__   __|
    | |  | |__    | | | |  | | |__  | (___   /  \  | |        | (___ | |  | | | |
    | |  |  __|   | | | |  | |  __|  \___ \ / /\ \ | |         \___ \| |  | | | |
    | |  | |____ _| |_| |__| | |____ ____) / ____ \| |     _   ____) | |__| | | |
    |_|  |______|_____|_____/|______|_____/_/    \_\_|    (_) |_____/ \____/  |_|




@author: Elías Gabriel Ferrer Jorge
@author:
(IN DEVELOPMENT)
'''
import Satellite.Sat as sat
import Satellite.Subsystem as sub

#Satellite
teidesat = sat.Sat()

#Subsystems
aocs      = sub.Subsystem(name = "AOCS",       ID = "AOCS0" , version = "0")
obc       = sub.Subsystem(name = "OBC" ,       ID = "OBC0"  , version = "0")
structure = sub.Subsystem(name = "STRUCTURE" , ID = "STRUC0", version = "0")
power     = sub.Subsystem(name = "POWER" ,     ID = "POW1"  , version = "0")
payload   = sub.Subsystem(name = "PAYLOAD" ,   ID = "OBC1"  , version = "0")

def main():
    print(teidesat)
    print(aocs)
    print(obc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
