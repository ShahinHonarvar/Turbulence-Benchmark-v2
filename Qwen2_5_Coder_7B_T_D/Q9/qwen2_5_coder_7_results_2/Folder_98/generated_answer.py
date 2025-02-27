def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i <= 6 and x % 2 != 0]