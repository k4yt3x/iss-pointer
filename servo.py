import RPi.GPIO as GPIO
import time


class Servo:

    def __init__(self, pin):
        self.pin = pin
        self._setup()

    def _setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pin = GPIO.PWM(self.pin, 50)
        self.pin.start(7.5)

    def _convert_angle(self, angle):
        return (angle * (1 / 18)) + 2.5

    def servo_change(self, angle):
        self.pin.ChangeDutyCycle(self._convert_angle(angle))
        time.sleep(1)


if __name__ == "__main__":
    servo = Servo(16)
    while True:
        servo.servo_change(int(input("Angle: ")) + 90)
