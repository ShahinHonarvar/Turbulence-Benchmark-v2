def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 5 <= i <= 7 and x % 2 != 0]