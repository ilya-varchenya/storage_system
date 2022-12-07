import sys

from hx711 import HX711
from electronics import indicate_activation, indicate_error, indicate_cell, setup_gpio
from speech_recognition_module import input_voice_command
from excel_adapter import find_item, remove_item, find_free_cell_or_add_to_similar_item
from text_parser import parse_command

from constants import ADD_ITEM, DELETE_ITEM, SEARCH_ITEM, UPDATE_ITEM, \
    HX711_DT, HX711_SCK, HX711_REFERENCE_UNIT, HX711_FAULT

hx = HX711(HX711_DT, HX711_SCK)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(HX711_REFERENCE_UNIT)
hx.reset()
hx.tare()
weight = hx.get_weight()
current_weight = 0


def run():
    command = input_voice_command()
    if command == 1:
        indicate_error()
    else:
        action, item, number = parse_command(command)
        if action == SEARCH_ITEM:
            line, column = find_item(item)
            indicate_cell(line, column)
        elif action == ADD_ITEM or action == UPDATE_ITEM:
            line, column = find_free_cell_or_add_to_similar_item(item)
            indicate_cell(line, column)
        elif action == DELETE_ITEM:
            line, column = remove_item(item)
            indicate_cell(line, column)
        else:
            action, item, number = parse_command(command)
            if action == SEARCH_ITEM:
                line, column = find_item(item)
                indicate_cell(line, column)
            elif action == ADD_ITEM or action == UPDATE_ITEM:
                line, column = find_free_cell_or_add_to_similar_item(item)
                indicate_cell(line, column)
            elif action == DELETE_ITEM:
                line, column = remove_item(item)
                indicate_cell(line, column)
            else:
                indicate_error()


if __name__ == '__main__':
    setup_gpio()
    try:
        while True:
            current_weight = hx.get_weight()
            if (current_weight - weight) < HX711_FAULT:
                indicate_activation()
                run()

            hx.power_down()
            hx.power_up()
            # time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
