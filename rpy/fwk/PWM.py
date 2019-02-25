import time
from distutils import sys
from time import sleep
import threading
from fwk import GPIOManager
import RPi.GPIO as GPIO   
import logging

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
        GPIOManager.setup(value)
        self.__gpio = value

    def get_gpio(self):
        return self.__gpio

    def execute(self):
        logging.debug("execute pwm with gpio=" + str(self.gpio) + " value=" + str(self.value) + " and pulse=" + str(self.hertz))

        firstPwmThread = next((x for x in self.threads if x.gpio == self.gpio),None)
        if (firstPwmThread == None):
            logging.debug("first start of thread with pin = %s" % self.gpio)
            pwmThread = PWMThread()
            pwmThread.gpio = self.gpio
            pwmThread.value = self.value
            pwmThread.hertz = self.hertz
            self.threads.append(pwmThread)
            pwmThread.start()
        else:
            logging.debug("stopping thread %s" % self.gpio)
            firstPwmThread.stop()
            firstPwmThread = PWMThread()
            firstPwmThread.gpio = self.gpio
            firstPwmThread.value = self.value
            firstPwmThread.hertz = self.hertz
            firstPwmThread.start()

    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("clean up PWM")

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def is_stopped(self):
        isStopped = self._stop_event.is_set()
        return 


class PWMThread(StoppableThread):
    def __init__(self):
        super(PWMThread, self).__init__()
        self.gpio = 1
        self.hertz = 50
        self.value = 0
        self.pwm = None
        self.daemon = True

    def run(self):
        self.pwm = GPIO.PWM(self.gpio, self.hertz) 
        self.pwm.start(self.value) 

        while(not self.is_stopped()):
            sleep(1)

        self.clean()
        logging.debug("thread with gpio=%s stopped" % self.gpio)

    def clean(self):
        if (self.pwm != None):
            self.pwm.stop()
            self.pwm = None