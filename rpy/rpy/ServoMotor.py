import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO

class ServoMotor(object):
    """description of class"""

    def __init__(self, **kwargs):
        GPIO.setmode(GPIO.BCM)
        self.__pulse_by_seconds = 100
        self.__gpio = 1
        self.pwm  = None
        return super().__init__(**kwargs)

    def move(self, grade):
        max_position = 11 - 2.5
        grades_division = max_position / float(180)
        duty_cycle = float(grade) * grades_division + 2.5
        print ("duty=", duty_cycle)
        self.pwm.ChangeDutyCycle(duty_cycle)

    #Property gpio 
    def set_gpio(self, value):
        print("ServoMotor.set_gpio=", value, "pulse=", self.__pulse_by_seconds)
        self.__gpio = value

        GPIO.setup(self.gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio, self.__pulse_by_seconds)

    def get_gpio(self):
        return self.__gpio

    gpio = property(get_gpio, set_gpio)

    def cleanup(self):
        GPIO.cleanup()