def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 29 <= i <= 79 and x % 2 != 0]