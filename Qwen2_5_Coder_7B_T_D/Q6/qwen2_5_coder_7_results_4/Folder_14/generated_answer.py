def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < i < 8 and x < 0]