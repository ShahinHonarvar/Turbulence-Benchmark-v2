def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:7]) if i >= 0 and i <= 6 and (x < 0)]