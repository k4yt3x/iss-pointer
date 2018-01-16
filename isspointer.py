#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ___   ____    ____      ____     ____
|_ _| / ___|  / ___|    |  _ \   / ___|
 | |  \___ \  \___ \    | |_) | | |
 | |   ___) |  ___) |   |  __/  | |___
|___| |____/  |____/    |_|      \____|


Name: ISS Pointer Controller
Dev: K4YT3X IZAYOI
Date Created: Jan 15, 2018
Last Modified: Jan 15, 2018

Description: This is the main script of the ISS Pointer.
It creats objects of the motor contoller and the servo controller.servo
"""

try:  # This try needs to go so we can trace errors
    from motor import Stepper
    from servo import Servo
except Exception:
    pass
from datetime import datetime
import avalon_framework as avl

import urllib.request
import json
import ephem
import time


class debug:

    def __init__(self, activated):
        self.activated = activated

    def debugger(self):
        pass


class Isspointer:
    """
    Dev: K4YT3X IZAYOI
    Date Created: Jan 15, 2018
    Last Modified: Jan 15, 2018

    This is the class that handles the iss pointer.
    Creating an object of this class will initialize and start
    the iss pointer.
    """

    def __init__(self):
        self.lat, self.lon = self._get_ISS_coordinates()
        self.motor = self._setup_motor()
        self.servo = self._setup_servo()

    def _setup_motor(self):
        return Stepper(12, 11, 13, 15)

    def _setup_servo(self):
        return Servo(16)

    def _get_ISS_coordinates(self):
        """
        Dev: K4YT3X IZAYOI
        Date Created: Jan 15, 2018
        Last Modified: Jan 15, 2018

        This method requests the current coordinate of the ISS
        from open notify in json format and parses it.

        Returns tuple (latitude, longitude)
        """
        req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
        response = urllib.request.urlopen(req)

        obj = json.loads(response.read().decode('utf-8'))
        return obj['iss_position']['latitude'], obj['iss_position']['longitude']

    def _get_iss_tle(self):
        """
        Dev: K4YT3X IZAYOI
        Date Created: Jan 15, 2018
        Last Modified: Jan 15, 2018

        This method requests a list of satellite
        TLE (the NORAD Two-Line Element format (TLE)) info.

        TLE should contain 3 lines

        returns list [tle_line_1, tle_line_2, tle_line_3]
        """
        iss_tle = []
        try:
            req = urllib.request.Request("https://www.celestrak.com/NORAD/elements/stations.txt")
            response = urllib.request.urlopen(req)
        except Exception as e:
            return False
        hit = False
        counter = 0
        for line in response.read().decode('utf-8').split('\n'):
            if "ISS (ZARYA)" in line:
                hit = True
            if hit and counter < 3:
                iss_tle.append(line)
                counter += 1
            else:
                return iss_tle

    def start(self):
        """
        Dev: K4YT3X IZAYOI
        Date Created: Jan 15, 2018
        Last Modified: Jan 15, 2018

        This method is the main ISS pointer controller
        it runs infinitively until Ctrl^C is pressed.
        """
        iss_default_tle = "ISS (ZARYA)", "1 25544U 98067A   18014.73214213  .00001932  00000-0  36199-4 0  9994", "2 25544  51.6432  63.7165 0003502  15.7107  89.3601 15.54306558 94655"
        observer = ephem.Observer()
        observer.lon, observer.lat = '43.435296', '-80.464363'
        while True:
            now = "{}/{}/{} {}:{}:{}".format(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second)
            observer.date = now
            print(now)

            iss_live_tle = self._get_iss_tle()
            if iss_live_tle:
                iss_tle = iss_live_tle
            else:
                iss_tle = iss_default_tle

            iss = ephem.readtle(iss_tle[0], iss_tle[1], iss_tle[2])
            iss.compute(observer)
            print('Elevation:{} Azimuth:{}'.format(iss.alt, iss.az))
            self.motor.set_azimuth(iss.az)
            self.servo.set_angle(iss.alt)
            time.sleep(2)


if __name__ == "__main__":
    isspointer = Isspointer()  # Creates ISS pointer object
    isspointer.start()  # Starts the pointer
else:
    avl.error("This file cannot be imported!")
    avl.error("Please run this file independently.")
