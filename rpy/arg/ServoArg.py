import sys
import time
import logging

from fwk.ServoMotor import ServoMotor
from arg.BaseArg import BaseArg

class ServoArg(BaseArg):
    """Servo arg for manager arguments"""

    def __init__(self):
        self.grade = 0

    def load_arguments(self, argv):
        for i in range(len(argv))[1:]:

            arg, val = self.get_argument(argv, i)

            if arg == "gpio" or arg == "p":
                self.gpio = int(val)

            if arg == "servo-move" or arg == "sm":
                self.grade = val

    def do(self):
        self.validate()

        if self.grade != 0:
            servoMotor = ServoMotor()
            try:
                servoMotor.gpio = self.gpio
                servoMotor.move(self.grade)
            finally:
                servoMotor.cleanup()

   
