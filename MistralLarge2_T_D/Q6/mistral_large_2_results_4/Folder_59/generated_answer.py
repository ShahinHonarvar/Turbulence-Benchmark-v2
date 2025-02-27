def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if x < 0 and 0 < i < 9]