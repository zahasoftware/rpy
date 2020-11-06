import sys
from fwk import GPIOManager
import time
import logging

from arg.LEDArg import LEDArg
from arg.PWMArg import PWMArg
from arg.InvalidUsageError import InvalidUsageError 

peripherics = { 'generic': ['gpio' ,'pin' ,'p', 'rpy', 'help'],
                'pwm': ['state','value',],
                'led': ['state','value'],
                'exit': [''],
                'help': ['']
                }

class RwyManager(object):
    """ Raspberry Python Manager """
    def __init__(self):
        pass

    def do(self, argv):


        if "debug" in argv:
            logging.basicConfig(level=logging.DEBUG)
        else :
            logging.basicConfig(level=logging.INFO)

        logging.debug("Argv = %s " % argv)

        pwmArg = PWMArg()
        ledArg = LEDArg()

        try:

            if (argv.count == 1):
                raise InvalidUsageError()

            GPIOManager.init()

            while True:
                try:

                    print("Enter command:")

                    args_string = input()
                    args = args_string.split(" ")
                    first_argument = args[0]

                    logging.debug("First argument = %s " % first_argument)
                    
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
                        
                    logging.debug("Selected peripherics are: %s" % periphericKey)

                    peripheric = None
                    if periphericKey == "pwm":
                        peripheric = pwmArg
                    elif periphericKey == "led":
                        peripheric = ledArg

                    elif periphericKey == "help":
                       self.show_help() 

                    if peripheric != None:
                        peripheric.load_arguments(args)
                        peripheric.do()

                except InvalidUsageError as ie:
                    logging.info("Invalid input, for more information write help")

        except Exception as e:
            logging.exception("Error: %s" % e)

        finally:
            GPIOManager.cleanup()
            for x in pwmArg.pwm.threads:
               if x != None: 
                   x.clean()
                   x.stop()

    def show_help(self):
        with open("./man.txt","r") as file:
            print(file.read())
