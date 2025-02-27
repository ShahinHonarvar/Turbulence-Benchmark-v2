def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:11]) if x < 0]