import sys
import time
import logging

from fwk.ServoMotor import ServoMotor
from arg.BaseArg import BaseArg

class ServoArg(BaseArg):
    """Servo arg for manager arguments"""

    def __init__(self):
        selft.pwm = PWM()

    def load_arguments(self, argv):
        for i in range(len(argv))[1:]:

            arg, val = self.get_argument(argv, i)

            if arg == "gpio" or arg == "pin" or arg == "p":
                self.pwm.wpm.gpio = int(val)

            if arg == "value" or arg == "val":
                self.pwm.value = int(val)

    def do(self):
        self.validate()

        if self.grade != 0:
            try:
                self.pwm.execute()
                time.sleep(0.5)
            finally:
                servoMotor.cleanup()
