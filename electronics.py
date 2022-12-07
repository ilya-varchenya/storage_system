import RPi.GPIO as GPIO
from time import sleep

from constants import LEDS


def indicate_error():
    blink(3, 0.25)


def indicate_cell(line, column, pause_time=5, n=1):
    while n > 0:
        n -= 1
        GPIO.output(LEDS[line - 1][column - 1], GPIO.HIGH)
        sleep(pause_time)
        GPIO.output(LEDS[line - 1][column - 1], GPIO.LOW)
        sleep(pause_time)
    

def blink(n=1, pause_time=0.2):
    while n > 0:
        n -= 1
        for lines in LEDS:
            for element in lines:
                GPIO.output(element, GPIO.HIGH)
        sleep(pause_time)
        for lines in LEDS:
            for element in lines:
                GPIO.output(element, GPIO.LOW)
        sleep(pause_time)


def indicate_activation():
    pause_time = 0.05
    for lines in LEDS:
        for element in lines:
            GPIO.output(element, GPIO.HIGH)
            sleep(pause_time)
            
    for lines in LEDS:
        for element in lines:
            GPIO.output(element, GPIO.LOW)
    
    blink(1)


if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    
    for i in LEDS:
        GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
    
    # indicate_activation()
    # indicate_error()
    indicate_cell(1, 1, 1, 5)
