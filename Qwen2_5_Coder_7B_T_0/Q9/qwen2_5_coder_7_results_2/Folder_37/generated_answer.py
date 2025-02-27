def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 1 <= i <= 5 and x % 2 != 0]