def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 42 < i < 87 and x < 0]