import unittest
from pointer.stepper import Stepper, DIRECTION
from pointer.exception import InvalidDirectionError
from pointer.wiringpi import wiringPiSetupGpio


class TestStepperMotor(unittest.TestCase):

    DIR_PIN = 23
    STEP_PIN = 24
    MS1_PIN = 17
    MS2_PIN = 27

    def setUp(self):
        self.test_stepper = Stepper(
            self.DIR_PIN,
            self.STEP_PIN,
            self.MS1_PIN,
            self.MS2_PIN
        )

    def test_direction_changes(self):
        self.test_stepper.direction = DIRECTION.CW
        self.assertEquals(
            self.test_stepper._direction,
            DIRECTION.CW,
            'Direction not set sucessfully. Got {}, expected {}'.format(
                self.test_stepper._direction,
                DIRECTION.CW
            )
        )
    
    def test_microstep_resolution_changes(self):
        self.test_stepper.microstep_resolution = 'full'
        self.assertEquals(
            self.test_stepper._microstep_resolution,
            'full',
            'Microstep resolution not set successfully. Got "{}", expected "{}"'.format(
                self.test_stepper._microstep_resolution,
                'full'
            )
        )

    def test_default_step(self):
        self.test_stepper.step()
        azimuth = self.test_stepper.azimuth
        self.assertEquals(
            azimuth, 
            0.28125, 
            'Unexpected rotation. Got {}, expected {}'.format(
                azimuth,
                0.28125
            )
        )

    def test_100_full_steps_cw(self):
        self.test_stepper.microstep_resolution = 'full'
        for _x in xrange(100):
            self.test_stepper.step()
        azimuth = self.test_stepper.azimuth
        self.assertAlmostEquals(
            azimuth, 
            225.0,
            msg='Unexpected rotation. Got {}, expected {}'.format(
                azimuth,
                225.0
            )
        )
    
    def test_100_full_steps_ccw(self):
        self.test_stepper.microstep_resolution = 'full'
        self.test_stepper.direction = DIRECTION.CCW
        for _x in xrange(100):
            self.test_stepper.step()
        azimuth = self.test_stepper.azimuth
        self.assertAlmostEquals(
            azimuth,
            -225.0,
            msg='Unexpected rotation. Got {}, expected {}'.format(
                azimuth,
                -225.0
            )
        )
    
    def test_1600_quarter_steps_cw(self):
        self.test_stepper.microstep_resolution = 'quarter'
        for _x in xrange(1600):
            self.test_stepper.step()
        azimuth = self.test_stepper.azimuth
        self.assertAlmostEquals(
            azimuth,
            900.0,
            msg='Unexpected rotation. Got {}, expected {}'.format(
                azimuth,
                900.0
            )
        )
 
    
    def test_valid_direction(self):
        self.test_stepper.direction = DIRECTION.CW
        direction = self.test_stepper.direction
        self.assertEquals(
            direction,
            DIRECTION.CW,
            'Direction not set successfully. Stepper was set to {}.'.format(direction)
        )

    def test_set_invalid_direction(self):
        with self.assertRaises(InvalidDirectionError) as cm:
            self.test_stepper.direction = 'forwards!!'
    


if __name__ == '__main__':
    unittest.main()
