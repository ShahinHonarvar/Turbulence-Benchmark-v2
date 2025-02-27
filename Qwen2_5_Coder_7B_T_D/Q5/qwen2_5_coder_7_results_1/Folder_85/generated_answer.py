def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 6 and i <= 8 and (x < 0)]