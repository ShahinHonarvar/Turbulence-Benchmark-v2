def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 64 < i < 80 and x < 0]