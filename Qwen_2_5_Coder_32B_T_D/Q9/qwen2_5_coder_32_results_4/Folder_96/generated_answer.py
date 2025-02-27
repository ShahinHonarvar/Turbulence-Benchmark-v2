def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 50 <= i <= 200 and x % 2 == 1]