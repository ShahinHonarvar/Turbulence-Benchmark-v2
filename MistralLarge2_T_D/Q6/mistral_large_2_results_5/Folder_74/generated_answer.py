def all_neg_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 13 < i < 70 and num < 0]