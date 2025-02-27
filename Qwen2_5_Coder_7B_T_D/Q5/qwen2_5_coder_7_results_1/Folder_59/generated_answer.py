def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:10]) if x < 0]