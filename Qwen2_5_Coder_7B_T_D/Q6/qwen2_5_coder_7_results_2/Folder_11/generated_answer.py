def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 15 < i < 100 and x < 0]