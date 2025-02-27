def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 20 < i < 51 and x < 0]