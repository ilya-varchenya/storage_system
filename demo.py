import sys
from time import sleep
import RPi.GPIO as GPIO

from hx711 import HX711
from electronics import indicate_activation, indicate_error, indicate_cell, setup_gpio

from constants import HX711_DT, HX711_SCK, HX711_REFERENCE_UNIT, HX711_FAULT

count = 0


def run(c):
    sleep(2.5)
    if c == 0:
        indicate_cell(1, 0)
        c += 1
    elif c == 1:
        indicate_cell(1, 0)
        c += 1
    elif c == 2:
        indicate_error()
        c = 0
    return c


if __name__ == '__main__':
    setup_gpio()
    hx = HX711(HX711_DT, HX711_SCK)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(HX711_REFERENCE_UNIT)
    hx.reset()
    hx.tare()
    weight = hx.get_weight()
    current_weight = 0

    try:
        while True:
            current_weight = hx.get_weight()
            print("abs({} - {}) > {}".format(current_weight, weight, HX711_FAULT))
            if abs(current_weight - weight) > HX711_FAULT:
                indicate_activation()
                count = run(count)

            hx.power_down()
            hx.power_up()
            sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
