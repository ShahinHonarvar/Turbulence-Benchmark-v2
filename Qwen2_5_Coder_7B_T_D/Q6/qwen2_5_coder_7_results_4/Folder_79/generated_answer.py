def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 2 < i < 9 and x < 0]