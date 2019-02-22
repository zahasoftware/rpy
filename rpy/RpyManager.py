import sys
import time
import logging

from arg.ServoArg import ServoArg 
from arg.PWMArg import PWMArg
from arg.InvalidUsageError import InvalidUsageError 

peripherics = {'generic': ['gpio' ,'pin' ,'p', 'rpy', 'help'],
                'servo': ['srv', 'sm', 'servo-move'],
                'cam': ['cam', 'out'],
                'pwm': ['state','value'],
                'dig': ['state','value']
                }

class RpyManager(object):
    """ Raspberry Python Manager """
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

    def do(self, argv):
        try:
            if (argv.count == 1):
                raise InvalidUsageError()

            first_argument = argv[1]
            
            if len(first_argument) == 0:
                raise InvalidUsageError()

            periphericKey = None
            for key in peripherics:
                if key == "generic":
                    continue

                if key == first_argument:
                    periphericKey = key
                    break

            if (periphericKey == None):
                raise InvalidUsageError()
                
            logging.info("Selected peripherics are: %s" % periphericKey)

            peripheric = None
            if periphericKey == "servo":
                peripheric = ServoArg()

            elif periphericKey == "pwm":
                peripheric = PWMArg()

            elif periphericKey == "cam":
                pass

            if peripheric != None:
                peripheric.load_arguments(argv)
                peripheric.do()

        except InvalidUsageError as ie:
            self.show_help()

        except Exception as e:
            logging.exception("Invalid arguments, detail: %s" % e)

    def show_help(self):
        with open("./man.txt","r") as file:
            print(file.read())
