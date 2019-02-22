import time
import RPi.GPIO as GPIO   
import logging

#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
class PWM(object):

    def __init__(self, **kwargs):
        logging.debug("PWM.__init__")
        self.pulse_by_seconds = 50
        self.__gpio = 1
        self.value = 1

        GPIO.setmode(GPIO.BCM)

    #Property gpio
    def set_gpio(self, value):
        logging.debug("try to set gpio=" + str(value))
        self.__gpio = value

    def execute(self):
        logging.debug("execute pwm with gpio=" + str(self.gpio) + " value=" + str(self.value) + " and pulse=" + str(self.pulse_by_seconds))
        GPIO.setup(self.gpio, GPIO.OUT)
        pwm = GPIO.PWM(self.gpio, self.pulse_by_seconds) 

        pwm.start(self.value) 

        while True: 
            time.sleep(1000)
        

    def get_gpio(self):
        return self.__gpio
    
    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("clean up PWM")
        #GPIO.cleanup()