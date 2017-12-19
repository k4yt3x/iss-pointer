import wiringpi as wp
from enum import Enum
from time import sleep
from exception import InvalidDirectionError


class GPIO(Enum):
    HIGH = 1
    LOW = 0


class DIRECTION(Enum):
    CW = 1
    CCW = 0


class Stepper(object):

    GEAR_RATIO = 2.5

    MICROSTEP_TRUTH_TABLE = {
        # resolution: (ms1, ms2)
        'full': (0, 0),
        'half': (1, 0),
        'quarter': (0, 1),
        'eigth': (1, 1)
    }

    MICROSTEP_RESOLUTION_MULTIPLIER = {
        'full': 1,
        'half': 0.5,
        'quarter': 0.25,
        'eigth': 0.125
    }

    def __init__(self, dir_pin, step_pin, ms1_pin, ms2_pin):
        self.dir_pin = dir_pin
        self.ms2_pin = ms2_pin
        self.step_delay = 0.001
        self._microstep_resolution = 'eigth'
        self._direction = DIRECTION.CW
        self._azimuth = 0.0  # in degrees from true north

        self.setup()

    def __del__(self):
        self.teardown()

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if isinstance(direction, DIRECTION):
            self._direction = direction
        else:
            raise InvalidDirectionError

    @property
    def microstep_resolution(self):
        return self._microstep_resolution

    @microstep_resolution.setter
    def microstep_resolution(self, resolution):
        if resolution not in self.MICROSTEP_TRUTH_TABLE.keys():
            self._microstep_resolution = 'eigth'
        else:
            self._microstep_resolution = resolution
        self.set_microstep_resolution_in_easydriver()

    @property
    def azimuth(self):
        return self._azimuth

    def set_microstep_resolution_in_easydriver(self):
        ms1, ms2 = self.MICROSTEP_TRUTH_TABLE[self._microstep_resolution]
        wp.digitalWrite(self.ms1_pin, ms1)
        wp.digitalWrite(self.ms2_pin, ms2)

    def setup(self):
        wp.pinMode(self.dir_pin, wp.GPIO.OUTPUT)
        wp.pinMode(self.step_pin, wp.GPIO.OUTPUT)
        wp.pinMode(self.ms1_pin, wp.GPIO.OUTPUT)
        wp.pinMode(self.ms2_pin, wp.GPIO.OUTPUT)

    def step(self):
        # 0.9 degrees per step * resolution * gear_ratio
        # This is probably the wrong way to do this but it works. It would be
        # good to rethink how this could work.
        degrees_moved = 0.9 * \
            self.MICROSTEP_RESOLUTION_MULTIPLIER[self._microstep_resolution] * \
            self.GEAR_RATIO
        if self._direction == DIRECTION.CCW:
            degrees_moved = -degrees_moved
        self._azimuth += degrees_moved
        wp.digitalWrite(self.step_pin, 1)
        sleep(self.step_delay)
        wp.digitalWrite(self.step_pin, 0)
        sleep(self.step_delay)

    def teardown(self):
        wp.pinMode(self.dir_pin, wp.GPIO.INPUT)
        wp.pinMode(self.step_pin, wp.GPIO.INPUT)
        wp.pinMode(self.ms1_pin, wp.GPIO.INPUT)
        wp.pinMode(self.ms2_pin, wp.GPIO.INPUT)


if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(24, wp.GPIO.OUTPUT)
    wp.pinMode(17, wp.GPIO.OUTPUT)
    wp.pinMode(27, wp.GPIO.OUTPUT)
    # Microstepping pins
    wp.digitalWrite(17, 1)
    wp.digitalWrite(27, 1)
    # Rotate
    for i in range(0, int(8 * 400 * 2.5)):
        wp.digitalWrite(24, 1)
        sleep(0.0005)
        wp.digitalWrite(24, 0)
    wp.pinMode(24, wp.GPIO.INPUT)
    wp.pinMode(17, wp.GPIO.INPUT)
    wp.pinMode(27, wp.GPIO.INPUT)
