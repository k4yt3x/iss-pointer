"""
Name: RPi Servo Controller
Project: ISS Pointer
Dev: DJGood
Date Created: Dec 16, 2017
Last Modfied: Dec 18, 2017

Dev: K4YT3X IZAYOI
Last Modified: Jan 16, 2018
"""
import avalon_framework as avl
import RPi.GPIO as GPIO
import time

VERSION = "1.0 beta"


class Servo:

    def __init__(self, pin):
        self.pin = pin  # Sets control pin

    def __del__(self):
        GPIO.cleanup()

    def _setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, 50)

    def _convert_angle(self, angle):
        """
        Modify this according to the accepted
        frequency of the servo. In our setup,
        our servo accepted frequency from
        0.5Hz to 2.5Hz
        """
        return (angle * 1 / 18) + 2.5

    def set_angle(self, angle):
        """
        Dev: K4YT3X IZAYOI
        Date Created: Jan 16, 2018
        Last Modified: Jan 16, 2018

        This method sets the servo to a certain
        angle whereL
        MAX = 90 deg
        MIN = -90 deg
        Neutral = 0 deg (horizon)

        This method is designed to take an input
        of an angle of the dgree above horizon,
        aka the elevation.
        """
        angle *= -1
        angle += 90
        self._setup()
        self.p.start(self._convert_angle(angle))
        time.sleep(1)
        self.p.stop()


# --------------------------------- Begin Self Testing
"""
The code below is for self-testing when this file
is ran independently. It takes an angle and sets
the servo to that angle.
"""

if __name__ == "__main__":
    servo = Servo(16)  # Using pin 16 (BOARD)
    while True:
        servo.set_angle(float(avl.gets("Angle")))
