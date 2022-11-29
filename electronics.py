import RPi.GPIO as GPIO
from time import sleep

from constants import LEDS, BOTTOM_RIGHT

def get_data_from_wage_module():
    pass


def indicate_error():
    pass


def indicate_cell(line, column):
    pause_time = 2
    GPIO.output(LEDS[0], GPIO.HIGH)
    sleep(pause_time)
    GPIO.output(LEDS[0], GPIO.HIGH)


def indicate_activation():
    pause_time = 0.5
    GPIO.output(LEDS[0], GPIO.HIGH)
    GPIO.output(LEDS[1], GPIO.HIGH)
    GPIO.output(LEDS[2], GPIO.HIGH)
    GPIO.output(LEDS[3], GPIO.HIGH)
    GPIO.output(LEDS[12], GPIO.HIGH)
    GPIO.output(LEDS[13], GPIO.HIGH)
    GPIO.output(LEDS[14], GPIO.HIGH)
    GPIO.output(LEDS[15], GPIO.HIGH)
    sleep(pause_time)
    GPIO.output(LEDS[0], GPIO.LOW)
    GPIO.output(LEDS[1], GPIO.LOW)
    GPIO.output(LEDS[2], GPIO.LOW)
    GPIO.output(LEDS[3], GPIO.LOW)
    GPIO.output(LEDS[12], GPIO.LOW)
    GPIO.output(LEDS[13], GPIO.LOW)
    GPIO.output(LEDS[14], GPIO.LOW)
    GPIO.output(LEDS[15], GPIO.LOW)
    
    GPIO.output(LEDS[4], GPIO.HIGH)
    GPIO.output(LEDS[5], GPIO.HIGH)
    GPIO.output(LEDS[6], GPIO.HIGH)
    GPIO.output(LEDS[7], GPIO.HIGH)
    GPIO.output(LEDS[8], GPIO.HIGH)
    GPIO.output(LEDS[9], GPIO.HIGH)
    GPIO.output(LEDS[10], GPIO.HIGH)
    GPIO.output(LEDS[11], GPIO.HIGH)
    sleep(pause_time)
    GPIO.output(LEDS[4], GPIO.LOW)
    GPIO.output(LEDS[5], GPIO.LOW)
    GPIO.output(LEDS[6], GPIO.LOW)
    GPIO.output(LEDS[7], GPIO.LOW)
    GPIO.output(LEDS[8], GPIO.LOW)
    GPIO.output(LEDS[9], GPIO.LOW)
    GPIO.output(LEDS[10], GPIO.LOW)
    GPIO.output(LEDS[11], GPIO.LOW)
    
if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    
    for i in LEDS:
        GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
    
    indicate_activation()

