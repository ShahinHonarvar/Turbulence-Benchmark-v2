def all_neg_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 0 < idx < 8 and num < 0]