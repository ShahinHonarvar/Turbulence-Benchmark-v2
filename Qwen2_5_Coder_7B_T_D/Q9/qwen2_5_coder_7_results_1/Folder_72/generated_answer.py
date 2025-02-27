def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 29 and i <= 51 and (x % 2 != 0)]