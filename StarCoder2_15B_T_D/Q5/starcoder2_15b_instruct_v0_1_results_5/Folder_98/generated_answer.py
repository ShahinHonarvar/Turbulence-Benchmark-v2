def all_neg_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst) if idx <= 6 and num < 0]