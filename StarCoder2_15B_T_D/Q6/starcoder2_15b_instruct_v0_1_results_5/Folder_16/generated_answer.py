def all_neg_ints_exclusive(lst):
    neg_ints = [x for x in lst if x < 0]
    if len(neg_ints) >= 90 - 86:
        return neg_ints[86:90]
    else:
        return []