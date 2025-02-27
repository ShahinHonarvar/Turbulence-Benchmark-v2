def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 22 and i <= 88 and (x % 2 == 1)]