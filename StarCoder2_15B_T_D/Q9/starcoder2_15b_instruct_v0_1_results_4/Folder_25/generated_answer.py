def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 29 and i <= 93 and (x % 2 == 1)]