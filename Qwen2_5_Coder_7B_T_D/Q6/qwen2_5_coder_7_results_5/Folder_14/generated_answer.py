def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 1 < i < 8 and x < 0]