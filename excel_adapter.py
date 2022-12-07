from random import randint
import xlrd
from xlutils.copy import copy
from constants import UPPER_LEFT, BOTTOM_RIGHT
from text_parser import parse_cell_data
from electronics import indicate_error

file_name = "storage.xls"


def read_cell(line, column):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(0)
    print("Cell ({0}, {1}) contains: {2}".format(line, column, sh.cell_value(rowx=line, colx=column)))
    data = parse_cell_data(sh.cell_value(line, column))
    return data


def write_info(line, column, data):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    workbook = copy(book)
    sheet = workbook.get_sheet(0)

    data_string = ""
    for key, value in data.items():
        data_string += "{0}: {1}\n".format(key, value)
    data_string = data_string[0:-1]

    sheet.write(line, column, data_string)
    workbook.save(file_name)


def find_item(item):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(0)

    for line in range(BOTTOM_RIGHT[0] - UPPER_LEFT[0] + 1):
        for column in range(BOTTOM_RIGHT[1] - UPPER_LEFT[1] + 1):
            cell_value = parse_cell_data(sh.cell_value(rowx=line, colx=column))
            for key in cell_value.keys():
                if key == item:
                    print("Item is in cell ({}, {})".format(line, column))
                    return line, column
    else:
        return None, None


def add_or_update_item(item, number):
    line, column = find_free_cell_or_add_to_similar_item(item)
    data = read_cell(line, column)
    if data == '':
        data.setdefault(item, number)
    else:
        for key, value in data.items():
            if key == item:
                data[key] = value + number
    write_info(line, column, data)


def remove_item(item):
    line, column = find_item(item)
    if line is None and column is None:
        indicate_error()
    else:
        data = read_cell(line, column)
        del data[item]
        write_info(line, column, data)
        return line, column


def find_free_cell_or_add_to_similar_item(item):
    # find cell with item
    cell_with_item = find_item(item)
    if cell_with_item != [None, None]:
        return cell_with_item
    else:
        # find empty cell
        empty_cell_line, empty_cell_column = find_item('')
        if empty_cell_line is not None and empty_cell_column is not None:
            # get random cell
            line = randint(UPPER_LEFT[0], BOTTOM_RIGHT[0])
            column = randint(UPPER_LEFT[1], BOTTOM_RIGHT[1])
            return line, column
        else:
            return empty_cell_line, empty_cell_column


if __name__ == '__main__':
    # read_cell(0, 0)
    # write_info([0, 1], {'mew': 5})
    # print(find_item('mew'))
    # print(find_item('bark'))
    # add_or_update_item("mew", 10)
    # read_cell(0, 1)
    remove_item("mew")
