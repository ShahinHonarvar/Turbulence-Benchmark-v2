def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 43 and i <= 86 and (x % 2 == 1)]