def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 31 <= i <= 72 and x < 0]