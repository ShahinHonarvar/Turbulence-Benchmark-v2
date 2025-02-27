def all_neg_ints_exclusive(int_list):
    start, end = (8, 10)
    return [x for x in int_list[start:end] if x < 0]