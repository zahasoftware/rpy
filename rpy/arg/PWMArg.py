import sys
import time
import logging

from fwk.PWM import PWM 
from arg.BaseArg import BaseArg

class PWMArg(BaseArg):
    """PWMArg arg for manager arguments"""

    def __init__(self):
        self.pwm = PWM()
        super(PWMArg, self).__init__()

    def load_arguments(self, argv):
        for i in range(len(argv))[1:]:

            arg, val = self.get_argument(argv, i)

            if arg == "gpio" or arg == "pin" or arg == "p":
                self.pwm.gpio = int(val)

            if arg == "hertz" or arg == "hz" :
                self.pwm.hertz = int(val)

            if arg == "value" or arg == "val" or arg == "v": 
                self.pwm.value = int(val)

    def do(self):
        self.validate()

        try:
            self.pwm.execute()
            time.sleep(0.5)
        finally:
            self.pwm.cleanup()
