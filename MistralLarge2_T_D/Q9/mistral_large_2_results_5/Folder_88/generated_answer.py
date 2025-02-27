def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 4 <= i <= 8 and x % 2 != 0]