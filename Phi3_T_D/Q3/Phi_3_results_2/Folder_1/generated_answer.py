def all_pos_ints_inclusive(integer_list):
    return [value for index, value in enumerate(integer_list) if 31 <= index <= 72 and value > 0]