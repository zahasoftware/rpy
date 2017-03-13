import sys
import time
sys.path.append(".\\rpy\\")

from rpy.ServoMotor import ServoMotor

class RpyManager(object):
    """Raspberry Python Manager"""

    def __init__(self):
        self.gpi = 1
        self.grade = 0

    def init(self, argv):
        try:
            print("RpyManager.init")

            for i in range(len(argv)):
                arg_splited = argv[i].split("=")

                if i == 0:
                    continue

                if i != 0 and len(arg_splited) != 2:
                    raise Exception("Invalid argument ", arg_splited)

                arg = arg_splited[0]
                val = arg_splited[1]

                if arg == "gpi":
                    self.gpi = val

                if arg == "servo-move" or arg == "sm":
                    self.grade = val

        except Exception as e:
            print("Invalid arguments: ",e)
            self.show_help()

    def do(self):
        if self.gpi == 0:
            raise Exception("You have to choice a gpio value for pin.")

        if self.grade != 0:
            try:
                servoMotor = ServoMotor()
                servoMotor.gpio = 18
                servoMotor.move(self.grade)
                time.sleep(1)
            finally:
                servoMotor.cleanup()

    def show_help(self):
        print("\n"
              "Example of use:\n"
              "rpy gpio=<pin> [servo-move=<0-180>]"
              "\n")
