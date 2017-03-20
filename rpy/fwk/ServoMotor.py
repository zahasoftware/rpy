import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import logging

class ServoMotor(object):
    """ RPi.GPIO Wrapper Class """

    def __init__(self, **kwargs):
        logging.debug("ServoMotor.__init__")
        GPIO.setmode(GPIO.BCM)
        self.__pulse_by_seconds = 50
        self.__gpio = 1
        self.pwm = None

    def move(self, grade):
        max_position = 11 - 2.5
        grades_division = max_position / float(180)
        duty_cycle = float(grade) * grades_division + 2.5
        logging.debug("ServoMotor.set_gpio=%s, duty=%s, pulse=%s " % (self.gpio,
                                                                      duty_cycle, 
                                                                      self.__pulse_by_seconds))
        self.pwm.ChangeDutyCycle(duty_cycle)

    #Property gpio
    def set_gpio(self, value):
        self.__gpio = value

        GPIO.setup(self.gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio, self.__pulse_by_seconds)
        self.pwm.start(2.5)

    def get_gpio(self):
        return self.__gpio

    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        logging.debug("ServoMortor clean up")
        GPIO.cleanup()