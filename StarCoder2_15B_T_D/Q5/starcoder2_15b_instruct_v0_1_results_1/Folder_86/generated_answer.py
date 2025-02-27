def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 31 and i <= 34 and (x < 0)]