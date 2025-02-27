def all_neg_ints_inclusive(lst):
    return [x for x in lst if x < 0 and lst.index(x) in range(0, 4)]