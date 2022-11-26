def parse_command():
    pass


def parse_cell_data(data_string):
    data = {}
    items = data_string.split('\n')
    for i in items:
        if i == "":
            # empty cell
            break
        else:
            item, number = i.split(': ')
            data.setdefault(item, int(number))
    return data


if __name__ == '__main__':
    print(parse_cell_data("конденсатор: 1\nрезистор: 2\nлампочка: 3"))
