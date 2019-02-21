import RPi.GPIO as GPIO   
import logging

#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
class PWM(object):

    def __init__(self, **kwargs):
        logging.debug("ServoMotor.__init__")
        #GPIO.setmode(GPIO.BCM)
        self.pulse_by_seconds = 50
        self.__gpio = 1
        self.value = 1

        GPIO.setmode(GPIO.BOARD)

    def execute(self):
        logging.debug("execute pwm")
        pwm = GPIO.PWM(self.__value, self.pulse_by_seconds) 
        pwm.start(0) 
        pwm.ChangeDutyCycle(self.value)

    #Property gpio
    def set_gpio(self, value):
        GPIO.setup(value, GPIO.OUT)
        self.__gpio = value

    def get_gpio(self):
        return self.__gpio
    
    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("Clean up PWM")
        GPIO.cleanup()