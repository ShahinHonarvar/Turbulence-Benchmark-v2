def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 0 and i < 6 and (x < 0)]