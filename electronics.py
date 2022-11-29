import RPi.GPIO as GPIO
from time import sleep

from constants import LEDS


def get_data_from_wage_module():
    pass


def indicate_error():
    pause_time = 0.2
    count = 3
    leds = LEDS.copy()
    for line in range(len(LEDS)):
        for column in range(len(LEDS)):
            leds[column][line] = leds[line][column]

    while count >= 0:
        for lines in leds:
            for element in lines:
                GPIO.output(element, GPIO.HIGH)
        sleep(pause_time)
        for lines in leds:
            for element in lines:
                GPIO.output(element, GPIO.LOW)
        count -= 1


def indicate_cell(line, column):
    pause_time = 2
    GPIO.output(LEDS[line - 1][column - 1], GPIO.HIGH)
    sleep(pause_time)
    GPIO.output(LEDS[line - 1][column - 1], GPIO.LOW)


def indicate_activation():
    pause_time = 0.5
    count = 3
    while count >= 0:
        for lines in LEDS:
            for element in lines:
                GPIO.output(element, GPIO.HIGH)
        sleep(pause_time)
        for lines in LEDS:
            for element in lines:
                GPIO.output(element, GPIO.LOW)
        count -= 1


if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    
    for i in LEDS:
        GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
    
    indicate_activation()

