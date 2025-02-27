def all_neg_ints_inclusive(lst):
    neg_ints = [x for x in lst if x < 0]
    if len(neg_ints) >= 55:
        return neg_ints[50:55]
    else:
        return []