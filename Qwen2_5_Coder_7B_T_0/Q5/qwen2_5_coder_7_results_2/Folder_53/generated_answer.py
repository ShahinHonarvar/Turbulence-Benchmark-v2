def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 100 <= i <= 200 and x < 0]