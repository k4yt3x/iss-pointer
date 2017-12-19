class Direction(object):

    def __init__(self, azimuth, altitude):
        self.azimuth = azimuth
        self.altitude = altitude

class Pointer(object):

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def run(self):
        pass
        # while running:
            # direction = calculate_direction()
            # calculate change in direction from pointing direction and desired direction
            # if alt change > 1 degree:
                # update servo pos
                # pointing direction is now set to latest update
            # if az change > 0.9 degrees:
                # move stepper one step and update pointing direction

    def calculate_direction(self, direction): 
        # returns az, alt
        pass

    def move_stepper(self, steps):
        # code from stepper.py
        pass

    def set_servo_position(self, angle):
        # code from servo.py
        pass
            

if __name__ == '__main__':
    pointer = Pointer()
    pointer.run()
