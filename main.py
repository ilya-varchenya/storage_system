from electronics import get_data_from_wage_module, indicate_activation, indicate_error, indicate_cell
from speech_recognition_module import input_voice_command
from excel_adapter import find_item, remove_item, find_free_cell_or_add_to_similar_item
from text_parser import parse_command

from constants import SYSTEM_WAGE, ADD_ITEM, DELETE_ITEM, SEARCH_ITEM, UPDATE_ITEM

wage_of_parts = 0


def run():
    current_wage = get_data_from_wage_module()
    if SYSTEM_WAGE + wage_of_parts != current_wage:
        indicate_activation()

        command = input_voice_command()
        if command == 1:
            indicate_error()
        else:
            action, item, number = parse_command(command)
            if action == SEARCH_ITEM:
                line, column = find_item(item)
                indicate_cell(line, column)
            elif action == ADD_ITEM or action == UPDATE_ITEM:
                cell = find_free_cell_or_add_to_similar_item(item)
                # indicate_cell(cell)
            elif action == DELETE_ITEM:
                cell = remove_item(item)
                # indicate_cell(cell)
            else:
                indicate_error()


if __name__ == '__main__':
    while True:
        run()
