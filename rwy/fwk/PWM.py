import time
from distutils import sys
from time import sleep
import threading
from fwk import GPIOManager
import logging
import wiringpi

#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
class PWM(object):

    def __init__(self, **kwargs):
        logging.debug("PWM.__init__")
        self.__gpio = 1
        self.value = 1
        self.hertz = 50 
        self.threads = list()

    #Property gpio
    def set_gpio(self, value):
        wiringpi.pinMode(value, 2)#1 = OUTPUT, 0 = INPUT, 2 = PWM
        self.__gpio = value

    def get_gpio(self):
        return self.__gpio


    def execute(self):
        logging.debug("execute pwm with gpio=" + str(self.gpio) + " value=" + str(self.value) + " and pulse=" + str(self.hertz))
        #Value must be between 0 and 1024
        wiringpi.pwmWrite(self.gpio, self.value)

    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("clean up PWM")

