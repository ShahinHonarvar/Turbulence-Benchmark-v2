def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 12 and i < 70 and (x < 0)]