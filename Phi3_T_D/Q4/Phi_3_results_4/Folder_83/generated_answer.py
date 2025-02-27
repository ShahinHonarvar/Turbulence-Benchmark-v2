def all_pos_ints_exclusive(int_list):
    return [value for index, value in enumerate(int_list) if 90 < index < 200 and value > 0]