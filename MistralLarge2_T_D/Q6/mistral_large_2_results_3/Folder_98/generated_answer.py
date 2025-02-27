def all_neg_ints_exclusive(int_list):
    return [i for idx, i in enumerate(int_list) if 0 < idx < 6 and i < 0]