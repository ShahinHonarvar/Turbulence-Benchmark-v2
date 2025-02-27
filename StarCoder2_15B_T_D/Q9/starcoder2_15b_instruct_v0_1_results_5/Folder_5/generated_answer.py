def all_odd_ints_inclusive(input_list):
    return [value for index, value in enumerate(input_list) if 8 <= index <= 9 and value % 2 == 1]