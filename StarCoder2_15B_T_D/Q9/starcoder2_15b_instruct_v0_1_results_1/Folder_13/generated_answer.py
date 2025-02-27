def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 25 and i <= 87 and (x % 2 == 1)]