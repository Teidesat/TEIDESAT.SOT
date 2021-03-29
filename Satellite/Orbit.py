'''
TEIDESAT
SPACECRAFT OPERATIONS

ORBIT MODEL

@author: Elías Gabriel Ferrer Jorge
@author:

----------------------------------------------------------------------------
TOOLS:
https://pypi.org/project/TLE-tools/
https://pypi.org/project/orbit-predictor/

REFERENCE'S API
https://rhodesmill.org/skyfield/earth-satellites.html

----------------------------------------------------------------------------
EXAMPLE OF TLE:

source = """ISS (ZARYA)
1 25544U 98067A   19249.04864348  .00001909  00000-0  40858-4 0  9990
2 25544  51.6464 320.1755 0007999  10.9066  53.2893 15.50437522187805"""

'''


from skyfield.api import load, wgs84, EarthSatellite



class Orbit:
    def __init__(self):
        self.tle   = None
        self.id    = None
        self.line1 = None
        self.line2 = None
        self.url = None
        self.satellites = None
        self.observer = None
        self.ts = load.timescale()
        self.alt = None
        self.az  = None
        self.distance = None

    def __str__(self):
        temp = "TLE\n"
        temp += 69*"-"
        temp += self.id
        temp += self.line1
        temp += self.line2
        return temp

    def loadTLE(self, tle):
        '''

        :param tle:
        :return:
        '''
        self.tle = tle
        self.id    = self.tle[0]
        self.line1 = self.tle[1]
        self.line2 = self.tle[2]
        return self.id,self.line1,self.line2

    def loadSatellites(self):
        '''

        :return:
        '''
        self.satellites = load.tle_file(self.url)
        return

    def loadSatfromTLE(self,tle):
        '''

        :param tle:
        TLE EXAMPLE
        tle = """
        GOCE
        1 34602U 09013A   13314.96046236  .14220718  20669-5  50412-4 0   930
        2 34602 096.5717 344.5256 0009826 296.2811 064.0942 16.58673376272979
        """

        :return:
        '''

        lines = tle.strip().splitlines()
        self.satellites = EarthSatellite(lines[1],lines[2],lines[0])
        return



    def loadObserver(self, lat, long):
        '''

        :param lat:
        :param long:
        :return:
        '''
        self.observer = wgs84.latlon(lat,long)
        return

    def setURL(self,url):
        '''

        :param url:
        :return:
        '''
        self.url = url
        return

    def currentTime(self):
        '''

        :return:
        '''
        return self.ts.now()

    def showSatellite(self):
        '''

        :return:
        '''
        print(self.satellite)
        return

    def setTime(self, year, month, day):
        '''

        :param year:
        :param month:
        :param day:
        :return:
        '''
        t = self.ts.utc(year, month, day)
        return t

    def findRiseSets(self, timedate_init, timedate_final, altitude_degrees):
        '''

        :param timedate_init:
        :param timedate_final:
        :param altitude_degrees:
        :return:
        '''
        t0 = self.setTime(timedate_init)
        t1 = self.setTime(timedate_final)
        t, events = self.satellites.find_events(self.observer, t0, t1, altitude_degrees)
        for ti, event in zip(t, events):
            name = ('rise above'+str(altitude_degrees), 'culminate', 'set below'+ str(altitude_degrees))[event]
            print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
        return

    def checkSatEpoch(self):
        '''

        :return:
        '''
        self.epoch = self.satellites.epoch.utc_jpl()
        print(self.epoch)
        return

    def checkSatellitePosition(self):
        '''

        :return:
        '''
        return self.satellites.at(self.currentTime())

    def getSatfromYours(self):
        '''

        :return:
        '''
        return print(self.satellites - self.observer)

    def getObservation(self):
        '''

        :return:
        '''
        self.alt, self.az, self.distance = self.getSatfromYours()

        if self.alt.degrees > 0:
            print(str(self.satellites.name) + " is above the horizon")

        print(self.alt)
        print(self.az)
        print(self.int(self.distance.km), 'km')
        return