import sys
import time
import logging

sys.path.append(".\\rpy\\arg\\")
from rpy.arg.ServoArg import ServoArg

peripherics = {'generic':
                    ['gpio' ,'p', 'rpy'],
                'servo':
                    ['srv', 'sm', 'servo-move'],
                'cam':
                    ['cam', 'out']}

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
        if (argv.count == 1):
            raise 

        first_argument = [x for x in argv 
                          if not any(a in x for a in peripherics["generic"])]
        

        if first_argument.count == 0:
            raise
        else:
            first_argument = first_argument[0]

        logging.debug("First argument is '%s' " % first_argument)

        try:
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
            elif periphericKey == "cam":
                pass

            if peripheric != None:
                peripheric.load_arguments(argv)
                peripheric.do()

        except Exception as e:
            logging.error("Invalid arguments: %s" % (e))

    def show_help(self):
        with open("./README.md","r") as file:
            print(file.read())

