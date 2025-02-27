def all_neg_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 48 and i < 74 and (x < 0)]