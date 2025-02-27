def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 12 and i <= 92 and (x % 2 == 1)]