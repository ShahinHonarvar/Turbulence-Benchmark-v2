def all_neg_ints_inclusive(lst):
    return [x for x in lst if x < 0 and 0 <= lst.index(x) <= 7]