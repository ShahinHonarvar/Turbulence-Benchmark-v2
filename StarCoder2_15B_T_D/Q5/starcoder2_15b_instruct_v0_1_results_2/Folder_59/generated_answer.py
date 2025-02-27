def all_neg_ints_inclusive(ints):
    return [i for i in ints if i < 0 and 0 <= ints.index(i) <= 9]