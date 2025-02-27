def all_neg_ints_exclusive(int_list):
    return [value for index, value in enumerate(int_list) if -100 < value < 0 and 20 < index < 200]