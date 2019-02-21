import sys
import time
import logging

from arg.PWMArg import PWMArg
from arg.ServoArg import ServoArg 
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

    def FindPeripheric2Process(self, first_argument, key):
        for arg in peripherics[key]:

            logging.debug("Are selected peripheric %s argument %s " % (key,arg))
            if arg in first_argument:
               return arg
        return None

    def do(self, argv):
        try:
            if (argv.count == 1):
                raise InvalidUsageError()

            first_argument = [x for x in argv 
                              if not any(a in x for a in peripherics["generic"])]
            
            logging.debug("first_argument=%s" % first_argument)

            if len(first_argument) == 0:
                raise InvalidUsageError()
            else:
                first_argument = first_argument[0]

            logging.debug("First argument is '%s' " % first_argument)

            periphericKey = None
            for key in peripherics:
                if key == "generic":
                    continue

                if None != self.FindPeripheric2Process(first_argument, key):
                    periphericKey = key
                    break

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
