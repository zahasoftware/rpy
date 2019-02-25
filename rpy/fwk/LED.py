import time
from distutils import sys
from fwk import GPIOManager
import RPi.GPIO as GPIO   
import logging

#https://sourceforge.net/p/raspberry-gpio-python/wiki/LED/
class LED(object):

    def __init__(self, **kwargs):
        logging.debug("LED.__init__")
        self.__gpio = 1
        self.value = 1

        GPIO.setmode(GPIO.BCM)

    #Property gpio
    def set_gpio(self, value):
        GPIOManager.setup(value)
        self.__gpio = value

    def execute(self):
        logging.debug("execute led with gpio=" + str(self.gpio) + " value=" + str(self.value))
        GPIO.output(self.gpio, self.value) 

    def get_gpio(self):
        return self.__gpio
    
    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("clean up LED")
