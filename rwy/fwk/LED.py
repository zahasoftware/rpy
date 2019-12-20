import time
from distutils import sys
import logging
import wiringpi

#https://sourceforge.net/p/raspberry-gpio-python/wiki/LED/
class LED(object):

    def __init__(self, **kwargs):
        logging.debug("LED.__init__")
        self.__gpio = 1
        self.value = 1


    #Property gpio
    def set_gpio(self, value):
        self.__gpio = value
        wiringpi.pinMode(value, 1)#1 = OUTPUT, 0 = INPUT, 2 = PWM

    def execute(self):
        logging.debug("execute led with gpio=" + str(self.gpio) + " value=" + str(self.value))
        wiringpi.digitalWrite(self.gpio, self.value)

    def get_gpio(self):
        return self.__gpio
    
    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("clean up LED")
