def all_neg_ints_exclusive(int_list):
    return [value for index, value in enumerate(int_list) if value < 0 and 48 < index < 76]