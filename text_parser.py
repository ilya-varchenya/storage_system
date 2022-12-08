from constants import ADD_ITEM, DELETE_ITEM, UPDATE_ITEM, SEARCH_ITEM, AMOUNT


def parse_command(text):
    text = text.lower()
    actions = [ADD_ITEM, DELETE_ITEM, UPDATE_ITEM, SEARCH_ITEM]
    words = text.split(" ")

    if len(words) < 1 and words[0] not in actions:
        return 1
    else:
        try:
            action = words[0]
            item = words[1]
            amount = None if words[2] != AMOUNT else words[3]
            return action, item, amount
        except IndexError():
            return 1


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
    # print(parse_cell_data("конденсатор: 1\nрезистор: 2\nлампочка: 3"))
    print(parse_command("добавить резистор количество 1"))
