def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 661 and i <= 924 and (x % 2 != 0)]