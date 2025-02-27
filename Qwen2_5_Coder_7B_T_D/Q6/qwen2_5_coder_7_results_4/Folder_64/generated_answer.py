def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[:5]) if i != 0 and i != 4 and (x < 0)]