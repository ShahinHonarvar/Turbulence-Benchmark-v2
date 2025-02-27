def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 10 <= i <= 66 and x % 2 != 0]