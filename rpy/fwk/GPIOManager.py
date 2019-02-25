import time
import RPi.GPIO as GPIO   
import logging

#https://sourceforge.net/p/raspberry-gpio-python/wiki/LED/
#class GPIOManager(object):
GPIOManager_gpios = []

def init():
    logging.debug("GPIOManager.__init__")
    GPIO.setmode(GPIO.BCM)


def setup(pin):
    if  not pin in GPIOManager_gpios :
        logging.debug("setup pin=" + str(pin))
        GPIO.setup(pin, GPIO.OUT)
        GPIOManager_gpios.append(pin)

def cleanup():
    logging.debug("clean up gpios")
    GPIO.cleanup()