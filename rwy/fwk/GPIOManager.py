import time
import logging
import wiringpi

#https://sourceforge.net/p/raspberry-gpio-python/wiki/LED/
#class GPIOManager(object):
GPIOManager_gpios = []

def init():
    logging.debug("GPIOManager.__init__")
    wiringpi.wiringPiSetupGpio()


def setup(pin):
    logging.debug("setup")


def cleanup():
    logging.debug("clean up gpios")